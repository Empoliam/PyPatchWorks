from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .pNode import pNode

class pGate:
    
    def __init__(self):
        self.tgt: 'pGate'
        self.host: 'pNode'
        self.port: int