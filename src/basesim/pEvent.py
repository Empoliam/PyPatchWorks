from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .pNode import pNode

from .pMessage import pMessage

class pEvent:
    
    def __init__(self, msg: 'pMessage', tgt: 'pNode'):
        self.msg = msg
        self.tgt = tgt
        self.eventTime = 0

    def __lt__(self,other):
        return (self.eventTime < other.eventTime)
    
    def __eq__(self,other):
        return (self.eventTime == other.eventTime)