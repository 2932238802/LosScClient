from model.LosRepo import LosRepo

class LosNewsRepo(LosRepo):
    def __init__(self) -> None:
        self.L_news_dict:dict[str,list] = {}
    
    
    
    """
    public tool has
    判断 key 存不存在
    """
    def Lf_has(self, key: str) -> bool:
        return key in self.L_news_dict
    
    
    """
    public tool
    set
    
    """
    def Lf_set(self, key: str, data: object):
        if isinstance(data,list):
            self.L_news_dict[key] = data
            
            

    """
    public tool
    clear
    """
    def Lf_clear(self):
        self.L_news_dict.clear()
        
        
    
    """
    public tool get
    """
    def Lf_get(self, key: str):
        return self.L_news_dict.get(key,[])