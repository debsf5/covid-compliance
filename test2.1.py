from seirsplus2.models import *
from seirsplus2.networks import *
from seirsplus2.sim_loops import *
from seirsplus2.utilities import *
import networkx
import matplotlib.pyplot as plt
import seaborn

nodes = 10000
connections = 12
# INIT_EXPOSED = int(nodes*0.01)

beta = 0.155
sigma = 1 / 5.2
gamma = 1 / 12.39


# no superspreaders
# edges = 12
# desired_nedges = int(nodes * (edges / 2))
# baseGraph = networkx.gnm_random_graph(n=nodes, m=int(desired_nedges))

# with superspreaders
baseGraph = networkx.barabasi_albert_graph(n=nodes, m=connections)


init_I = 20
model = SEIRSNetworkModel(G=baseGraph, beta=beta, sigma=sigma, gamma=gamma, initE=20, budget='unequal')

model.run(T=13)
r0 = (nodes - model.numS[-1] - init_I) / init_I
model.run(T=1000)
print("r0 is " + str(r0))
model.figure_infections(use_seaborn=True)


# 100% compliance
model_100compliance = SEIRSNetworkModel(G=baseGraph, beta=beta, sigma=sigma, gamma=gamma, initE=20, budget='unequal', p_local=0.6, p_global= 0.05)
model_100compliance.run(T=1000)

model_100compliance.figure_infections(plot_S=False, plot_E=False, plot_I='line', plot_R='line', plot_Q_E=False, plot_Q_I=False, ylim=0.16, figsize=(5,4))
inf = 100*((nodes - model_100compliance.numS[-1])/nodes)
peak = 100*(max(model_100compliance.numI)/nodes)
print("Total percentage of infected is " + str(inf))
print("Percentage of people infected at peak is " + str(peak))


# Partial compliance (i) (comply with travelling restrictions)
model_partialcomplianceone = SEIRSNetworkModel(G=baseGraph, beta=beta, sigma=sigma, gamma=gamma, initE=20, budget='unequal', p_local=0.8, p_global=0.05)
model_partialcomplianceone.run(T=1000)

model_partialcomplianceone.figure_infections(plot_S=False, plot_E=False, plot_I='line', plot_R='line', plot_Q_E=False, plot_Q_I=False, ylim=0.16, figsize=(5,4))
inf = 100*((nodes - model_partialcomplianceone.numS[-1])/nodes)
peak = 100*(max(model_partialcomplianceone.numI)/nodes)
print("Total percentage of infected is " + str(inf))
print("Percentage of people infected at peak is " + str(peak))


# Partial compliance (ii) (comply with close contacts)
model_partialcompliancetwo = SEIRSNetworkModel(G=baseGraph, beta=beta, sigma=sigma, gamma=gamma, initE=20, budget='unequal', p_local=0.6, p_global=0.25)
model_partialcompliancetwo.run(T=1000)

model_partialcompliancetwo.figure_infections(plot_S=False, plot_E=False, plot_I='line', plot_R='line', plot_Q_E=False, plot_Q_I=False, ylim=0.16, figsize=(5,4))
inf = 100*((nodes - model_partialcompliancetwo.numS[-1])/nodes)
peak = 100*(max(model_partialcompliancetwo.numI)/nodes)
print("Total percentage of infected is " + str(inf))
print("Percentage of people infected at peak is " + str(peak))


# 0% compliance
model_nocompliance = SEIRSNetworkModel(G=baseGraph, beta=beta, sigma=sigma, gamma=gamma, initE=20, budget='unequal', p_local=1, p_global=0.3)
model_nocompliance.run(T=1000)

model_nocompliance.figure_infections(plot_S=False, plot_E=False, plot_I='line', plot_R='line', plot_Q_E=False, plot_Q_I=False, ylim=0.16, figsize=(5,4))
inf = 100*((nodes - model_nocompliance.numS[-1])/nodes)
peak = 100*(max(model_nocompliance.numI)/nodes)
print("Total percentage of infected is " + str(inf))
print("Percentage of people infected at peak is " + str(peak))


