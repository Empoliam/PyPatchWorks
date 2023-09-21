from basesim.pSimulation import pSimulation
from basesim.pEvent import pEvent
from basesim.pMessage import pMessage
from basesim.pNode import pNode
from basesim.pGate import pGate

sim = pSimulation(1000)

A = pNode("Node A")
A.addGate(1,pGate())
A.registerSim(sim)

B = pNode("Node B")
B.registerSim(sim)
B.addGate(1,pGate())

A.connectNodes(1,B,1)

sim.scheduleEventAtTime(50,pEvent(pMessage("Ping"),A))

while(sim.doNextEvent()):
    pass

print("t=" + str(sim.time) + ", events total " + str(sim.eventsTotal))