from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QFrame, QPushButton, QScrollArea, QSizePolicy
)

from common.LosC_Style import NEWS_LIST_PAGE_QSS
from common.LosC_LosNewsListPage import (
    NEWS_LIST_PAGE_OBJECT_NAME,
    NEWS_PAGE_TITLE_OBJECT_NAME,
    NEWS_PAGE_SUBTITLE_OBJECT_NAME,
    NEWS_LIST_BOX_OBJECT_NAME,
    NEWS_DETAIL_BOX_OBJECT_NAME,
    NEWS_SECTION_TITLE_OBJECT_NAME,
    NEWS_EMPTY_TEXT_OBJECT_NAME,
    NEWS_DETAIL_TITLE_OBJECT_NAME,
    NEWS_DETAIL_META_OBJECT_NAME,
NEWS_DETAIL_SUMMARY_OBJECT_NAME,
    NEWS_DETAIL_LINK_OBJECT_NAME,
    NEWS_ITEM_BUTTON_OBJECT_NAME,
    NEWS_ROOT_MARGINS,
    NEWS_ROOT_SPACING,
    NEWS_BODY_SPACING,
    NEWS_BOX_MARGINS,
    NEWS_BOX_SPACING,
    NEWS_LIST_WIDGET_MARGINS,
    NEWS_LIST_WIDGET_SPACING,
    NEWS_LIST_BOX_MIN_WIDTH,
    NEWS_DETAIL_BOX_MIN_WIDTH,
    NEWS_ITEM_BUTTON_HEIGHT,
    NEWS_ITEM_TITLE_MAX_LEN,
    NEWS_ITEM_TITLE_ELLIPSIS,
    NEWS_LIST_BOX_STRETCH,
    NEWS_DETAIL_BOX_STRETCH,
    NEWS_SCROLL_STRETCH,
    NEWS_BOTTOM_STRETCH,
    NEWS_LIST_SECTION_TITLE,
    NEWS_DETAIL_SECTION_TITLE,
    NEWS_LIST_EMPTY_TEXT,
    NEWS_NO_DATA_TEXT,
    NEWS_LOADING_TEXT,
    NEWS_DETAIL_DEFAULT_TITLE,
    NEWS_DETAIL_DEFAULT_META,
    NEWS_DETAIL_DEFAULT_SUMMARY,
    NEWS_SUMMARY_EMPTY_TEXT,
    NEWS_DETAIL_LINK_PREFIX,
    NEWS_DETAIL_CONTENT_EMPTY_TEXT,
    NEWS_ITEM_TEXT_TEMPLATE,
    NEWS_DETAIL_META_TEMPLATE,
)

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
        self.setObjectName(NEWS_LIST_PAGE_OBJECT_NAME)

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
        root_layout.setContentsMargins(*NEWS_ROOT_MARGINS)
        root_layout.setSpacing(NEWS_ROOT_SPACING)

        # 这个就是最上面那个大写
        title = QLabel(self.L_title.upper())
        title.setObjectName(NEWS_PAGE_TITLE_OBJECT_NAME)

        # 这个是大标题下面的小标题
        subtitle = QLabel(self.L_route)
        subtitle.setObjectName(NEWS_PAGE_SUBTITLE_OBJECT_NAME)

        root_layout.addWidget(title)
        root_layout.addWidget(subtitle)

        body_layout = QHBoxLayout()
        body_layout.setSpacing(NEWS_BODY_SPACING)

        self.L_list_box = QFrame()
        self.L_list_box.setObjectName(NEWS_LIST_BOX_OBJECT_NAME)
        self.L_list_box.setMinimumWidth(NEWS_LIST_BOX_MIN_WIDTH)
        self.L_list_box.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding
        )

        list_box_layout = QVBoxLayout(self.L_list_box)
        list_box_layout.setContentsMargins(*NEWS_BOX_MARGINS)
        list_box_layout.setSpacing(NEWS_BOX_SPACING)

        list_title = QLabel(NEWS_LIST_SECTION_TITLE)
        list_title.setObjectName(NEWS_SECTION_TITLE_OBJECT_NAME)
        list_box_layout.addWidget(list_title)

        self.L_news_scroll = QScrollArea()
        self.L_news_scroll.setWidgetResizable(True)
        self.L_news_scroll.setFrameShape(QFrame.Shape.NoFrame)

        self.L_news_list_widget = QWidget()
        self.L_news_list_layout = QVBoxLayout(self.L_news_list_widget)
        self.L_news_list_layout.setContentsMargins(*NEWS_LIST_WIDGET_MARGINS)
        self.L_news_list_layout.setSpacing(NEWS_LIST_WIDGET_SPACING)

        list_empty = QLabel(NEWS_LIST_EMPTY_TEXT)
        list_empty.setObjectName(NEWS_EMPTY_TEXT_OBJECT_NAME)
        list_empty.setWordWrap(True)

        self.L_news_list_layout.addWidget(list_empty)
        self.L_news_list_layout.addStretch(NEWS_BOTTOM_STRETCH)

        self.L_news_scroll.setWidget(self.L_news_list_widget)
        list_box_layout.addWidget(self.L_news_scroll, stretch=NEWS_SCROLL_STRETCH)

        # 右侧详情区域
        self.L_detail_box = QFrame()
        self.L_detail_box.setObjectName(NEWS_DETAIL_BOX_OBJECT_NAME)
        self.L_detail_box.setMinimumWidth(NEWS_DETAIL_BOX_MIN_WIDTH)
        self.L_detail_box.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding
        )

        detail_layout = QVBoxLayout(self.L_detail_box)
        detail_layout.setContentsMargins(*NEWS_BOX_MARGINS)
        detail_layout.setSpacing(NEWS_BOX_SPACING)

        detail_title = QLabel(NEWS_DETAIL_SECTION_TITLE)
        detail_title.setObjectName(NEWS_SECTION_TITLE_OBJECT_NAME)

        self.L_detail_title = QLabel(NEWS_DETAIL_DEFAULT_TITLE)
        self.L_detail_title.setObjectName(NEWS_DETAIL_TITLE_OBJECT_NAME)
        self.L_detail_title.setWordWrap(True)

        self.L_detail_meta = QLabel(NEWS_DETAIL_DEFAULT_META)
        self.L_detail_meta.setObjectName(NEWS_DETAIL_META_OBJECT_NAME)

        self.L_detail_summary = QLabel(NEWS_DETAIL_DEFAULT_SUMMARY)
        self.L_detail_summary.setObjectName(NEWS_DETAIL_SUMMARY_OBJECT_NAME)
        self.L_detail_summary.setWordWrap(True)

        self.L_detail_content = QLabel(NEWS_DETAIL_CONTENT_EMPTY_TEXT)
        self.L_detail_content.setObjectName(NEWS_DETAIL_SUMMARY_OBJECT_NAME)
        self.L_detail_content.setWordWrap(True)
        
        self.L_detail_link = QLabel("")
        self.L_detail_link.setObjectName(NEWS_DETAIL_LINK_OBJECT_NAME)
        self.L_detail_link.setWordWrap(True)

        detail_layout.addWidget(detail_title)
        detail_layout.addWidget(self.L_detail_title)
        detail_layout.addWidget(self.L_detail_meta)
        detail_layout.addWidget(self.L_detail_summary)
        detail_layout.addWidget(self.L_detail_content)
        detail_layout.addWidget(self.L_detail_link)
        detail_layout.addStretch(NEWS_BOTTOM_STRETCH)
        
        body_layout.addWidget(self.L_list_box, stretch=NEWS_LIST_BOX_STRETCH)
        body_layout.addWidget(self.L_detail_box, stretch=NEWS_DETAIL_BOX_STRETCH)
        root_layout.addLayout(body_layout, stretch=NEWS_BOTTOM_STRETCH)
        
    
    
    """
    public tool
    
    设置新闻信息
    """
    def Lf_set_news_items(self,items):
        
        self._Lf_clear_news_in_list()
        if not items:
            empty_label = QLabel(NEWS_NO_DATA_TEXT)
            empty_label.setObjectName(NEWS_EMPTY_TEXT_OBJECT_NAME)
            
            # 自动换行
            empty_label.setWordWrap(True)
            
            self.L_news_list_layout.addWidget(empty_label)
            self.L_news_list_layout.addStretch(NEWS_BOTTOM_STRETCH)
            # 剩余 空间 会被 stretch 吃掉
            return
        for index, news in enumerate(items, start=1):
            # 这里的 start 就是决定了 index的开始数字 开始 从 最开始开始的不用担心
            title = self._Lf_make_short_text(news.get("title", ""))
            news_name = news.get("news_name", "")
            column_name = news.get("column_name", "")
            published = news.get("published", "")
            btn = QPushButton(
                NEWS_ITEM_TEXT_TEMPLATE.format(
                    index=index,
                    title=title,
                    news_name=news_name,
                    column_name=column_name,
                    published=published,
                )
            )
            btn.setObjectName(NEWS_ITEM_BUTTON_OBJECT_NAME)
            btn.setFlat(True)
            btn.setFixedHeight(NEWS_ITEM_BUTTON_HEIGHT)
            btn.setSizePolicy(
                QSizePolicy.Policy.Expanding,
                QSizePolicy.Policy.Fixed
            )
            btn.clicked.connect(
                lambda checked=False, n=news: self._Lf_show_news_detail(n)
            )
            self.L_news_list_layout.addWidget(btn)
        self.L_news_list_layout.addStretch(NEWS_BOTTOM_STRETCH)
    

            
    """
    public tool

    显示加载中状态
    """
    def Lf_set_loading(self) -> None:
        self._Lf_clear_news_in_list()
        loading_label = QLabel(NEWS_LOADING_TEXT)
        loading_label.setObjectName(NEWS_EMPTY_TEXT_OBJECT_NAME)
        loading_label.setWordWrap(True)
        self.L_news_list_layout.addWidget(loading_label)
        self.L_news_list_layout.addStretch(NEWS_BOTTOM_STRETCH)

    
    
    """
    public tool

    显示加载失败状态
    """
    def Lf_set_error(self, message: str) -> None:
        self._Lf_clear_news_in_list()

        error_label = QLabel(message)
        error_label.setObjectName(NEWS_EMPTY_TEXT_OBJECT_NAME)
        error_label.setWordWrap(True)

        self.L_news_list_layout.addWidget(error_label)
        self.L_news_list_layout.addStretch(NEWS_BOTTOM_STRETCH)
    
    
    
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
        content     = news.get("content","")
        self.L_detail_title.setText(title if title else NEWS_DETAIL_DEFAULT_TITLE)
        self.L_detail_meta.setText(
            NEWS_DETAIL_META_TEMPLATE.format(
                news_name=news_name,
                column_name=column_name,
                published=published,
            )
        )
        self.L_detail_content.setText(
            content if content else NEWS_DETAIL_CONTENT_EMPTY_TEXT
        )
        self.L_detail_summary.setText(summary if summary else NEWS_SUMMARY_EMPTY_TEXT)
        self.L_detail_link.setText(f"{NEWS_DETAIL_LINK_PREFIX}{link}" if link else "")



    """
    把过长的内容 缩短
    """
    def _Lf_make_short_text(self,text:str):
        if len(text) <= NEWS_ITEM_TITLE_MAX_LEN:
            return text
        return text[:NEWS_ITEM_TITLE_MAX_LEN] + NEWS_ITEM_TITLE_ELLIPSIS



    """
    清理 信息列表
    
    private tool
    """
    def _Lf_clear_news_in_list(self) -> None    :
        while self.L_news_list_layout.count() > 0:
            item = self.L_news_list_layout.takeAt(0)
            if item is None:
                continue
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
                            
                            
            
