import signal
import sys
import pickle
from threading import Thread
from time import sleep

from AbstractVirtualCapability import AbstractVirtualCapability, VirtualCapabilityServer, formatPrint
class OpenSmart_Electromagnet(AbstractVirtualCapability):
    
    def __init__(self, server):
        super().__init__(server)
        # Property initialization here
        self.Weight= #SetProperty
        self.MagnetStatus= #SetProperty

    def turnMagnetOn(self, params: dict) -> dict:
        # Method implementation here
        pass

    def turnMagnetOff(self, params: dict) -> dict:
        # Method implementation here
        pass

    def GetWeight(self, params: dict) -> dict:
        # Method implementation here
        pass

    def SetWeight(self, params: dict) -> dict:
        # Method implementation here
        pass

    def setMagnetStatus(self, params: dict) -> dict:
        # Method implementation here
        pass

    def getMagnetStatus(self, params: dict) -> dict:
        # Method implementation here
        pass

if __name__ == "__main__":
    try:
        port = None
        if len(sys.argv[1:]) > 0:
            port = int(sys.argv[1])
        server = VirtualCapabilityServer(port)
    except KeyboardInterrupt:
        print("[Main] Received KeyboardInterrupt")

