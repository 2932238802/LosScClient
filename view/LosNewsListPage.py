from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QFrame,QPushButton
)

from common.LosC_Style import NEWS_LIST_PAGE_QSS

class LosNewsListPage(QWidget):
    """
    新闻列表页

    """

    def __init__(
        self,
        title: str,
        route: str,
        news_name: str,
        column_name: str | None = None
    ) -> None:
        super().__init__()
        self.setObjectName("LosNewsListPage")

        self.L_title = title
        self.L_route = route
        self.L_news_name = news_name
        self.L_column_name = column_name

        self._Lf_init_layout()
        self.setStyleSheet(NEWS_LIST_PAGE_QSS)



    """
    private tool

    初始化布局
    """
    def _Lf_init_layout(self) -> None:
        root_layout = QVBoxLayout(self)
        root_layout.setContentsMargins(56, 52, 56, 40)
        root_layout.setSpacing(28)

        # 这个就是最上面那个大写
        title = QLabel(self.L_title.upper())
        title.setObjectName("NewsPageTitle")

        # 这个是大标题下面的小标题
        subtitle = QLabel(self.L_route)
        subtitle.setObjectName("NewsPageSubtitle")

        root_layout.addWidget(title)
        root_layout.addWidget(subtitle)

        body_layout = QHBoxLayout()
        body_layout.setSpacing(18)

        self.L_list_box = QFrame()
        self.L_list_box.setObjectName("NewsListBox")

        self.L_news_list_layout = QVBoxLayout(self.L_list_box)
        self.L_news_list_layout.setContentsMargins(24, 22, 24, 22)
        self.L_news_list_layout.setSpacing(12)

        # 左侧的内容
        list_title = QLabel("NEWS LIST")
        list_title.setObjectName("NewsSectionTitle")

        list_empty = QLabel("新闻列表将在这里显示。\n当前阶段先做 UI 骨架。")
        list_empty.setObjectName("NewsEmptyText")
        list_empty.setWordWrap(True)

        self.L_news_list_layout.addWidget(list_title)
        self.L_news_list_layout.addWidget(list_empty)
        self.L_news_list_layout.addStretch(1)

        # 右侧详情区域
        self.L_detail_box = QFrame()
        self.L_detail_box.setObjectName("NewsDetailBox")

        detail_layout = QVBoxLayout(self.L_detail_box)
        detail_layout.setContentsMargins(24, 22, 24, 22)
        detail_layout.setSpacing(12)

        detail_title = QLabel("DETAIL")
        detail_title.setObjectName("NewsSectionTitle")

        self.L_detail_title = QLabel("选择一条新闻查看详情")
        self.L_detail_title.setObjectName("NewsDetailTitle")
        self.L_detail_title.setWordWrap(True)

        self.L_detail_meta = QLabel("/ waiting / selected")
        self.L_detail_meta.setObjectName("NewsDetailMeta")

        self.L_detail_summary = QLabel("点击左侧新闻列表中的任意条目，详情会显示在这里。")
        self.L_detail_summary.setObjectName("NewsDetailSummary")
        self.L_detail_summary.setWordWrap(True)

        self.L_detail_link = QLabel("")
        self.L_detail_link.setObjectName("NewsDetailLink")
        self.L_detail_link.setWordWrap(True)

        detail_layout.addWidget(detail_title)
        detail_layout.addWidget(self.L_detail_title)
        detail_layout.addWidget(self.L_detail_meta)
        detail_layout.addWidget(self.L_detail_summary)
        detail_layout.addWidget(self.L_detail_link)
        detail_layout.addStretch(1)
        
        body_layout.addWidget(self.L_list_box, stretch=2)
        body_layout.addWidget(self.L_detail_box, stretch=3)
        root_layout.addLayout(body_layout, stretch=1)
        
    
    
    """
    public tool
    
    设置新闻信息
    """
    def Lf_set_news_items(self,items):
        
        self._Lf_clear_news_in_list()
        if not items:
            empty_label = QLabel("暂无新闻数据")
            empty_label.setObjectName("NewsEmptyText")
            
            # 自动换行
            empty_label.setWordWrap(True)
            
            self.L_news_list_layout.addWidget(empty_label)
            self.L_news_list_layout.addStretch(1)
            # 剩余 空间 会被 stretch 吃掉
            return
        for index, news in enumerate(items, start=1):
            # 这里的 start 就是决定了 index的开始数字 开始 从 最开始开始的不用担心
            title = news.get("title", "")
            news_name = news.get("news_name", "")
            column_name = news.get("column_name", "")
            published = news.get("published", "")
            btn = QPushButton(
                f"{index:02d}  {title}\n"
                f"     {news_name} / {column_name} · {published}"
            )
            btn.setObjectName("NewsItemButton")
            btn.setFlat(True)
            btn.clicked.connect(
                lambda checked=False, n=news: self._Lf_show_news_detail(n)
            )
            self.L_news_list_layout.addWidget(btn)
        self.L_news_list_layout.addStretch(1)
    
           
            
    """
    public tool

    显示加载中状态
    """
    def Lf_set_loading(self) -> None:
        self._Lf_clear_news_in_list()
        loading_label = QLabel("正在加载新闻数据...")
        loading_label.setObjectName("NewsEmptyText")
        loading_label.setWordWrap(True)
        self.L_news_list_layout.addWidget(loading_label)
        self.L_news_list_layout.addStretch(1)

    
    
    """
    public tool

    显示加载失败状态
    """
    def Lf_set_error(self, message: str) -> None:
        self._Lf_clear_news_in_list()

        error_label = QLabel(message)
        error_label.setObjectName("NewsEmptyText")
        error_label.setWordWrap(True)

        self.L_news_list_layout.addWidget(error_label)
        self.L_news_list_layout.addStretch(1)
    
    
    
    """
    显示当个 新闻n
    
    private tool
    """
    def _Lf_show_news_detail(self,news: dict):
        title       = news.get("title", "")
        summary     = news.get("summary", "")
        news_name   = news.get("news_name", "")
        column_name = news.get("column_name", "")
        published   = news.get("published", "")
        link        = news.get("link", "")
        self.L_detail_title.setText(title if title else "选择一条新闻查看详情")
        self.L_detail_meta.setText(f"/ {news_name} / {column_name} / {published}")
        self.L_detail_summary.setText(summary if summary else "无摘要")
        self.L_detail_link.setText(link)



    """
    清理 信息列表
    
    private tool
    """
    def _Lf_clear_news_in_list(self) -> None    :
        while self.L_news_list_layout.count() > 1:
            # 这里不写 0 是因为 标题是 0
            item = self.L_news_list_layout.takeAt(1)
            if item is None:
                continue
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
                            
                            
            
