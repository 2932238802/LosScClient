from PySide6.QtCore import QRunnable,Slot
from model.LosClient import LosClient
from controller.LosRouter import get_router

class LosNewsTask(QRunnable):
    
    """
    init
    """
    def __init__(
        self,
        key:str,
        news_name : str,
        column_name: str|None = None
        )  -> None:
        
        super().__init__()
        self.L_key = key
        self.L_news_name = news_name
        self.L_column_name = column_name
        self.L_client = LosClient()
    
    
    
    """
    public slot tool
    
    run 是必须要 坚持的函数签名
    
    @Slot
    槽函数声明器
    虽然有自动推导 但是可以减少运行时的开销
    """
    @Slot()
    def run(self):
        self.Lf_run()
    def Lf_run(self) -> None:
        try:
            if self.L_column_name is None:
                res = self.L_client.Lf_get_news_by_news_name(
                    news_name=self.L_news_name,
                    page=1,
                    page_size=20
                )
            else:
                res = self.L_client.Lf_get_news_by_news_name_and_column(
                    news_name=self.L_news_name,
                    column_name=self.L_column_name,
                    page=1,
                    page_size=20
                )
            get_router().Ls_news_load_suc.emit(self.L_key, res)
        except Exception as e:
            get_router().Ls_news_load_err.emit(self.L_key, str(e))    
            
