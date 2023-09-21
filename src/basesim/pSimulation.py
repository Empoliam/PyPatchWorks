from queue import PriorityQueue

from .pEvent import pEvent

class pSimulation:



    def __init__(self, endTime):
        self.eventQueue = PriorityQueue()
        self.time = 0
        self.endTime = 0
        self.eventsTotal = 0
        self.endTime = endTime

    def scheduleEventAtTime(self, t, E: pEvent):
        E.eventTime = t
        self.eventQueue.put((t,E))

    def scheduleEventIn(self, t, E: pEvent):
        self.scheduleEventAtTime(self.time+t,E)

    def doNextEvent(self):
        if(self.eventQueue.empty()): return 0        
        
        e: pEvent = self.eventQueue.get()[1]
        
        if(e.eventTime > self.endTime): return 0
        
        self.time = e.eventTime
        self.eventsTotal += 1
        
        e.tgt.handleMessage(e.msg)
        
        return 1
        