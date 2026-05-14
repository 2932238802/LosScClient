from abc import ABC,abstractmethod

class LosRepo(ABC):
    @abstractmethod
    def Lf_set(self,key:str,data:object):
        pass
    
    @abstractmethod
    def Lf_get(self,key:str) ->object|None:
        pass
    
    @abstractmethod
    def Lf_clear(self):
        pass
    
    @abstractmethod
    def Lf_has(self,key:str) -> bool:
        pass