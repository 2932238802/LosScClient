from PySide6.QtWidgets import QStackedWidget

from common.LosC_Style import CONTENT_AREA_QSS
from common.LosC_Nav import NAV_TOP_ITEMS, NAV_NEWS_GROUPS, NAV_BOTTOM_ITEMS

from view.LosHomePage import LosHomePage
from view.LosSearchPage import LosSearchPage
from view.LosNewsListPage import LosNewsListPage
from view.LosPagePlaceholder import LosPagePlaceholder


class LosContentArea(QStackedWidget):

    def __init__(self) -> None:
        super().__init__()
        self.setObjectName("LosContentArea")
        self.setStyleSheet(CONTENT_AREA_QSS)
        self.L_pages: dict = {}
        self._Lf_build_pages()


    """
    private tool
    
    按导航项构建所有占位页，并注册到 stack 里
    """
    def _Lf_build_pages(self) -> None:
        for item in NAV_TOP_ITEMS:
            if item["key"] == "home":
                page = LosHomePage()
                self.L_pages["home"] = page
                self.addWidget(page)
            elif item["key"] == "search":
                page = LosSearchPage()
                self.L_pages["search"] = page
                self.addWidget(page)
            else:
                self._Lf_add_page(
                    key=item["key"],
                    title=item["title"],
                    subtitle=f"/ {item['key']}",
                )

        # 新闻源页
        for group in NAV_NEWS_GROUPS:
            group_page = LosNewsListPage(
                title=group["title"],
                route=f"/ news / {group['key']}",
                news_name=group["title"]
            )
            # child 就是栏目
            self.L_pages[group["key"]] = group_page
            self.addWidget(group_page)
            for child in group["children"]:
                child_page = LosNewsListPage(
                    title=f"{group['title']} / {child['title']}",
                    route=f"/ news / {child['key']}",
                    news_name=group["title"],
                    column_name=child["title"]
                )
                self.L_pages[child["key"]] = child_page
                self.addWidget(child_page)

        # 底部功能页
        for item in NAV_BOTTOM_ITEMS:
            self._Lf_add_page(
                key=item["key"],
                title=item["title"],
                subtitle=f"/ {item['key']}",
            )

    

    """
    private tool
    
    新增一个占位页
    """
    def _Lf_add_page(self, key: str, title: str, subtitle: str, body: str = "") -> None:
        page = LosPagePlaceholder(title=title, subtitle=subtitle, body=body)
        self.L_pages[key] = page
        self.addWidget(page)


    """
    public tool
    
    切换到 key 对应的页面
    """
    def Lf_switch_to(self, key: str) -> None:
        page = self.L_pages.get(key)
        if page is None:
            return
        self.setCurrentWidget(page)
