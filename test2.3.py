from seirsplus2.models import *
from seirsplus2.networks import *
from seirsplus2.sim_loops import *
from seirsplus2.utilities import *
import networkx
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

nodes = 10000
connections = 6

beta = 0.155
sigma = 1 / 5.2
gamma = 1 / 12.39

# no superspreaders
# edges = 12
# desired_nedges = int(nodes * (edges / 2))
# baseGraph = networkx.gnm_random_graph(n=nodes, m=int(desired_nedges))

# with superspreaders
baseGraph = networkx.barabasi_albert_graph(n=nodes, m=connections)

# fig = plt.subplot()
# ax = plt.axes()

superspreaderProportion = 0.2

generalpopulationProportion = (1 - superspreaderProportion)

# Defining proportions of superspreaders vs general population
superspreaderNumber = int(superspreaderProportion * nodes)

# Number of superspreaders within the population
generalpopulationNumber = int(generalpopulationProportion * nodes)

degree_individuals = [d for n, d in baseGraph.degree()]

sorted_degree_sequence = sorted(degree_individuals)

# plt.xlabel('Degree')
# plt.ylabel('Num nodes')
# plt.title('Interactions of superspreaders')
# # plt.xlim([0,25])
# plt.hist(degree_individuals, bins=50)
# plt.show()
# degree sequence

sorted_index_individuals = np.argsort(degree_individuals)

# divide population in superspreaders and not superspreaders based on their degree (number of contacts)
superSpreaders = sorted_index_individuals[-superspreaderNumber-1:-1]
generalPopulation = sorted_index_individuals[:generalpopulationNumber]
p_local = np.zeros(nodes)
p_global = np.zeros(nodes)


# superspreaders comply (partial compliance i)
p_local[superSpreaders] = 0.8
p_global[superSpreaders] = 0.05

# others don't
p_local[generalPopulation] = 0.6
p_global[generalPopulation] = 0.25


model_partialcomplianceone = SEIRSNetworkModel(G=baseGraph, beta=beta,sigma=sigma, gamma=gamma, initE=20,budget='unequal', p_local=p_local, p_global=p_global)
model_partialcomplianceone.run(T=1000)

ax.plot(100*model_partialcomplianceone.numI/nodes, label="Partial compliance (i)" + str())


# superspreaders comply (partial compliance ii)
p_local[superSpreaders] = 0.6
p_global[superSpreaders] = 0.25

# others don't
p_local[generalPopulation] = 0.8
p_global[generalPopulation] = 0.05


model_partialcompliancetwo = SEIRSNetworkModel(G=baseGraph, beta=beta,sigma=sigma, gamma=gamma, initE=20,budget='unequal', p_local=p_local, p_global=p_global)
model_partialcompliancetwo.run(T=1000)

ax.plot(100*model_partialcompliancetwo.numI/nodes, label="Partial compliance (ii)" + str())


plt.xlabel('Timestep')
# Set the y axis label of the current axis.
plt.ylabel('% population infected')
# Set a title of the current axes.
plt.title('Levels of compliance of superspreaders')
plt.legend()
plt.show()
