from controller.LosRouter import get_router
from model.LosClient import LosClient
from view.LosNewsListPage import LosNewsListPage


"""
news controller
"""
class LosNewsCT:
    def __init__(self,pages: dict) -> None:
        self.L_client = LosClient()
        self.L_pages = pages # str -> widght
        self._Lf_init_connect()
        
        
        
    """
    private init
    
    初始化 连接
    """
    def _Lf_init_connect(self):
        get_router().Ls_nav_selected.connect(
            self._Lf_on_nav_selected
        )
        
        
    
    """
    private slot
    
    槽函数
    """
    def _Lf_on_nav_selected(self,select_name:str):
        
        page = self.L_pages.get(select_name)
        if page is None:
            return
        if not isinstance(page,LosNewsListPage):
            return 
        self._Lf_load_page(page)
        
        

    """
    private tool
    
    加载文章
    """
    def _Lf_load_page(self,page:LosNewsListPage):
        page.Lf_set_loading()                                   # 设置为 加载的环节
        try:
            news_name = page.L_news_name
            column_name = page.L_column_name
            if column_name is None:
                res = self.L_client.Lf_get_news_by_news_name(
                    news_name= news_name,
                    page= 1,
                    page_size=20
                )
            else:
                res = self.L_client.Lf_get_news_by_news_name_and_column(
                    news_name=news_name,
                    column_name=column_name,
                    page=1,
                    page_size=20
                )
                
            data = res.get("data",{})
            items = data.get("items",[])
            page.Lf_set_news_items(items)
        except Exception as e:
            page.Lf_set_error(
                "新闻加载失败\n"
                f"错误信息：{e}"
            )