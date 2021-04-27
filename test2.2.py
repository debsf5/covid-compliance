from seirsplus2.models import *
from seirsplus2.networks import *
from seirsplus2.sim_loops import *
from seirsplus2.utilities import *
import networkx
import matplotlib.pyplot as plt


# def run_model(scenario,runs,plot,outfile):

nodes = 10000
connections = 12
# INIT_EXPOSED = int(nodes*0.01)

beta = 0.155
sigma = 1 / 5.2
gamma = 1 / 12.39

# no superspreaders
edges = 12
desired_nedges = int(nodes * (edges / 2))
baseGraph = networkx.gnm_random_graph(n=nodes, m=int(desired_nedges))

# with superspreaders
# baseGraph = networkx.barabasi_albert_graph(n=nodes, m=connections)


# init_I = 20
# model = SEIRSNetworkModel(G=baseGraph, beta=beta, sigma=sigma, gamma=gamma, initE=20, budget='unequal')
#
# model.run(T=13)
# r0 = (nodes - model.numS[-1] - init_I) / init_I
# model.run(T=1000)
# print("r0 is " + str(r0))


# Partial compliance (i) (comply with travelling restrictions)
model_partialcomplianceone = SEIRSNetworkModel(G=baseGraph, beta=beta, sigma=sigma, gamma=gamma, initE=20, budget='unequal', p_local=0.8, p_global=0.05)

model_partialcomplianceone.run(T=1000)

fig = plt.figure()
ax = plt.axes()

ax.plot(100*model_partialcomplianceone.numI/nodes,label="Partial compliance (i)" + str())



# Partial compliance (ii) (comply with close contacts)
model_partialcompliancetwo = SEIRSNetworkModel(G=baseGraph, beta=beta, sigma=sigma, gamma=gamma, initE=20, budget='unequal', p_local=0.6, p_global=0.25)

model_partialcompliancetwo.run(T=1000)


ax.plot(100*model_partialcompliancetwo.numI/nodes,label="Partial compliance (ii)" + str())


# 0% compliance
model_nocompliance = SEIRSNetworkModel(G=baseGraph, beta=beta, sigma=sigma, gamma=gamma, initE=20, budget='unequal', p_local=1, p_global=0.3)

model_nocompliance.run(T=1000)

ax.plot(100*model_nocompliance.numI/nodes,label="No compliance" + str())


# 100% compliance
model_100compliance = SEIRSNetworkModel(G=baseGraph, beta=beta, sigma=sigma, gamma=gamma, initE=20, budget='unequal', p_local=0.6, p_global= 0.05)

model_100compliance.run(T=1000)

ax.plot(100*model_100compliance.numI/nodes,label="100% compliance" + str())


plt.xlabel('Timestep')
plt.ylabel('% population infected')
plt.title('Levels of compliance \n Without superspreaders')
plt.legend()
plt.show()

