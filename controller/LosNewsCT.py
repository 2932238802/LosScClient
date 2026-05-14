from controller.LosRouter import get_router
from view.LosNewsListPage import LosNewsListPage
from controller.task.LosNewsTask import LosNewsTask
from PySide6.QtCore import QThreadPool
from model.LosNewsRepo import LosNewsRepo

"""
news controller
"""
class LosNewsCT:
    def __init__(self,pages: dict) -> None:
        self.L_pages = pages                            # str -> widght
        self.L_pool = QThreadPool.globalInstance()
        self.L_cur_key:str | None = None
        self.L_news_repo = LosNewsRepo()
        self._Lf_init_connect()
        
        
        
    """
    private init
    
    初始化 连接
    """
    def _Lf_init_connect(self):
        get_router().Ls_nav_selected.connect(
            self._Lf_on_nav_selected
        )
        get_router().Ls_news_load_suc.connect(
            self._Lf_on_news_load_suc
        )
        get_router().Ls_news_load_err.connect(
            self._Lf_on_news_load_err
        )
        
        
    
    """
    private slot
    
    槽函数
    有缓存的话 
    优先选择缓存回去
    没有缓存的话
    去请求
    """
    def _Lf_on_nav_selected(self,select_name:str):
        page = self.L_pages.get(select_name)
        if page is None:
            return
        if not isinstance(page,LosNewsListPage):
            return 
        self.L_cur_key = select_name
        if self.L_news_repo.Lf_has(select_name):
            print("[LosNewsCT] cache hit")
            items = self.L_news_repo.Lf_get(select_name)
            page.Lf_set_news_items(items)
            return
        print("[LosNewsCT] cache miss")
        self._Lf_load_page(select_name,page)            
        
    
    
    """
    private slot
    
    当信息加载成功的时候
    """
    def _Lf_on_news_load_suc(self,key:str, res: object):
        if(key != self.L_cur_key):
            return
        page = self.L_pages.get(key)
        if page is None:
            return
        
        if not isinstance(page,LosNewsListPage):
            return
        if not isinstance(res,dict):
            return
        
        data = res.get("data",{})
        items = data.get("items",[])
        self.L_news_repo.Lf_set(key, items)
        page.Lf_set_news_items(items)
        
    
    
    """
    private slot
    
    当信息加载失败的时候
    """
    def _Lf_on_news_load_err(self,key:str,msg:str):
        if(key != self.L_cur_key):
            return
        
        page = self.L_pages.get(key)
        if page is None:
            return
        
        if not isinstance(page, LosNewsListPage):
            return
        
        page.Lf_set_error(
            "新闻加载失败\n"
            f"错误信息：{msg}"
        )
    
    

    """
    private tool
    
    加载文章
    也就是去请求信息
    """
    def _Lf_load_page(self, key: str, page: LosNewsListPage) -> None:
        page.Lf_set_loading()

        task = LosNewsTask(
            key=key,
            news_name=page.L_news_name,
            column_name=page.L_column_name
        )

        self.L_pool.start(task)