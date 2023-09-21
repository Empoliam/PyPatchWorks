from typing import Dict
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .pSimulation import pSimulation 
    from .pGate import pGate
    
from .pMessage import pMessage   
from .pEvent import pEvent

class pNode:
    
    def __init__(self, name: str):
        self.name = name
        self.gateList: Dict[int,'pGate'] = {}
        self.sim: 'pSimulation'

    def registerSim(self, sim: 'pSimulation'):
        self.sim = sim

    def addGate(self, n: int, gate:'pGate'):
        gate.host = self
        gate.port = n
        self.gateList.update({n: gate})

    def connectNodes(self,srcPort: int, tgtNode:'pNode', tgtPort: int):
        self.gateList[srcPort].tgt = tgtNode.gateList[tgtPort]
        tgtNode.gateList[tgtPort].tgt = self.gateList[srcPort]
        
    def sendMessage(self, msg: 'pMessage', port: int):
        self.sim.scheduleEventIn(0, pEvent(msg, self.gateList[port].tgt.host))

    def scheduleIn(self, msg: 'pMessage', t: int):
        self.sim.scheduleEventIn(t,pEvent(msg,self))

    def handleMessage(self, msg: 'pMessage'):
                
        if(msg.name=="Ping"):
            print(self.name + " recieved message " + msg.name)
            self.scheduleIn(pMessage("trigger"),50)
        elif(msg.name=="trigger"):
            self.sendMessage(pMessage("Ping"),1)
