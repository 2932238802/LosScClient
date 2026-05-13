from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame
)
from PySide6.QtCore import Qt
from common.LosC_Style import HOME_PAGE_QSS

class LosHomePage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setObjectName("LosHomePage")
        self._Lf_init_layout()
        self.setStyleSheet(HOME_PAGE_QSS)

    """
    private tool
    初始化布局
    """
    def _Lf_init_layout(self) -> None:
        root_layout = QVBoxLayout(self)
        root_layout.setContentsMargins(56, 52, 56, 40)
        root_layout.setSpacing(28)
        title = QLabel("LOS SC NEWS CENTER")
        title.setObjectName("HomeTitle")
        subtitle = QLabel("/ home / overview")
        subtitle.setObjectName("HomeSubtitle")
        root_layout.addWidget(title)
        root_layout.addWidget(subtitle)
        card_layout = QHBoxLayout()
        card_layout.setSpacing(18)
        self.L_total_card = self._Lf_make_stat_card(
            title="NEWS TOTAL",
            value="0000",
            desc="stored articles"
        )
        self.L_source_card = self._Lf_make_stat_card(
            title="SOURCES",
            value="BBC / RMW",
            desc="active feeds"
        )
        self.L_status_card = self._Lf_make_stat_card(
            title="STATUS",
            value="ONLINE",
            desc="api connection"
        )
        card_layout.addWidget(self.L_total_card)
        card_layout.addWidget(self.L_source_card)
        card_layout.addWidget(self.L_status_card)
        root_layout.addLayout(card_layout)
        stream_title = QLabel("RECENT STREAM")
        stream_title.setObjectName("SectionTitle")
        root_layout.addWidget(stream_title)
        stream_box = QFrame()
        stream_box.setObjectName("HomeStreamBox")
        stream_layout = QVBoxLayout(stream_box)
        stream_layout.setContentsMargins(24, 22, 24, 22)
        stream_layout.setSpacing(12)
        empty_label = QLabel(
            "Latest news stream will be rendered here after API integration.\\n"
            "当前阶段：UI 骨架已完成，下一步接入后端 /api/news/latest。"
        )
        empty_label.setObjectName("HomeStreamEmpty")
        empty_label.setWordWrap(True)
        stream_layout.addWidget(empty_label)
        stream_layout.addStretch(1)
        root_layout.addWidget(stream_box, stretch=1)



    """
    private tool

    创建统计卡片
    """
    def _Lf_make_stat_card(self, title: str, value: str, desc: str) -> QFrame:
        card = QFrame()
        card.setObjectName("HomeStatCard")
        layout = QVBoxLayout(card)
        layout.setContentsMargins(22, 18, 22, 18)
        layout.setSpacing(10)
        title_label = QLabel(title)
        title_label.setObjectName("HomeStatTitle")
        value_label = QLabel(value)
        value_label.setObjectName("HomeStatValue")
        desc_label = QLabel(desc)
        desc_label.setObjectName("HomeStatDesc")
        layout.addWidget(title_label)
        layout.addWidget(value_label)
        layout.addWidget(desc_label)
        return card