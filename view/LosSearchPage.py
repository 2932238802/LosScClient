from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QFrame
)
from common.LosC_Style import SEARCH_PAGE_QSS

class LosSearchPage(QWidget):
    """
    搜索页

    """

    def __init__(self) -> None:
        super().__init__()
        self.setObjectName("LosSearchPage")
        self._Lf_init_layout()
        self.setStyleSheet(SEARCH_PAGE_QSS)



    """
    private tool

    初始化布局
    """
    def _Lf_init_layout(self) -> None:
        root_layout = QVBoxLayout(self)
        root_layout.setContentsMargins(56, 52, 56, 40)
        root_layout.setSpacing(28)

        # 标题
        title = QLabel("SEARCH CENTER")
        title.setObjectName("SearchTitle")

        subtitle = QLabel("/ search / news")
        subtitle.setObjectName("SearchSubtitle")

        root_layout.addWidget(title)
        root_layout.addWidget(subtitle)

        # 搜索栏
        search_bar = QFrame()
        search_bar.setObjectName("SearchBar")

        search_layout = QHBoxLayout(search_bar)
        search_layout.setContentsMargins(20, 16, 20, 16)
        search_layout.setSpacing(12)

        self.L_keyword_edit = QLineEdit()
        self.L_keyword_edit.setObjectName("SearchInput")
        self.L_keyword_edit.setPlaceholderText("输入关键词，例如 BBC / China / economy")

        self.L_search_btn = QPushButton("SEARCH")
        self.L_search_btn.setObjectName("SearchButton")
        self.L_search_btn.setFixedWidth(120)

        search_layout.addWidget(self.L_keyword_edit)
        search_layout.addWidget(self.L_search_btn)

        root_layout.addWidget(search_bar)

        # 结果标题
        result_title = QLabel("RESULTS")
        result_title.setObjectName("SectionTitle")
        root_layout.addWidget(result_title)

        # 结果区域
        result_box = QFrame()
        result_box.setObjectName("SearchResultBox")

        result_layout = QVBoxLayout(result_box)
        result_layout.setContentsMargins(24, 22, 24, 22)
        result_layout.setSpacing(12)

        empty_label = QLabel(
            "Search results will be rendered here after API integration.\n"
            "当前阶段：搜索页面 UI 已完成，下一步接入后端搜索接口。"
        )
        empty_label.setObjectName("SearchResultEmpty")
        empty_label.setWordWrap(True)

        result_layout.addWidget(empty_label)
        result_layout.addStretch(1)

        root_layout.addWidget(result_box, stretch=1)