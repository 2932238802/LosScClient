from common.LosC import API_BASE_URL, API_TIMEOUT
import requests

class LosClient:
    def __init__(self) -> None:
        self.L_baseUrl = API_BASE_URL
        self.L_timeout = API_TIMEOUT


        """
        后端:
        获取最新新闻（混合流，不分来源）
        @LosNewsRouter.get("/latest")
        def LF_get_latest_news(limit: int = Query(10, ge=1, le=100)):
        
        """
    def Lf_get_latest_news(self, limit: int = 10) -> dict:
        url = f"{self.L_baseUrl}/api/news/latest"
        res = requests.get(
            url=url,
            params={
                "limit": limit
            },
            timeout=self.L_timeout
        )
        res.raise_for_status()
        return res.json()
    
    

    """
    按新闻网站分页获取新闻
    例如 /api/news/by_news_name/bypage?news_name=BBC
    @LosNewsRouter.get("/by_news_name/bypage")
    def LF_get_news_by_news_name_and_page(
        news_name: str = Query(...),
        page: int = Query(1, ge=1),
        page_size: int = Query(20, ge=1, le=50)
    ):
    """
    def Lf_get_news_by_news_name(
        self,
        news_name:str,
        page:int = 1,
        page_size:int = 20
        ):
        
        url = f"{self.L_baseUrl}/api/news/by_news_name/bypage"
        res = requests.get(
            url = url,
            params={
                "news_name":news_name,
                "page":page,
                "page_size":page_size
            },
            timeout=self.L_timeout
        )
        res.raise_for_status()
        return res.json()
    
    
    
    """
    按 新闻网站 + 栏目 分页获取新闻
    /api/news/by_news_name_and_column/bypage?news_name=BBC&column_name=top
    @LosNewsRouter.get("/by_news_name_and_column/bypage")
    def LF_get_news_by_news_name_and_column_name_and_page(
        news_name: str = Query(...),
        column_name: str = Query(...),
        page: int = Query(1, ge=1),
        page_size: int = Query(20, ge=1, le=50)
    ):
    """
    def Lf_get_news_by_news_name_and_column(
    self,
        news_name: str,
        column_name: str,
        page: int = 1,
        page_size: int = 20
    ) -> dict:
        url = f"{self.L_baseUrl}/api/news/by_news_name_and_column/bypage"
        res = requests.get(
            url=url,
            params={
                "news_name": news_name,
                "column_name": column_name,
                "page": page,
                "page_size": page_size
            },
            timeout=self.L_timeout
        )
        res.raise_for_status()
        return res.json()
                
        

        
        