from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QSplitter, QStatusBar, QLabel
from controller.LosRouter import get_router
from common.LosC_MainWindow import (
    MAIN_WINDOW_TITLE,
    MAIN_WINDOW_WIDTH,
    MAIN_WINDOW_HEIGHT,
)
from common.LosC_Style import MAIN_WINDOW_QSS
from controller.LosNewsCT import LosNewsCT
from view.LosNavPanel import LosNavPanel
from view.LosContentArea import LosContentArea


class LosMainWindow(QMainWindow):
    """
    主窗口
    
    左侧导航 + 右侧内容区 QStackedWidget 多页
    """


    def __init__(self) -> None:
        super().__init__()
        self._Lf_init_style()
        self._Lf_init_layout()
        self._Lf_init_connect()


    """
    private tool
    
    初始化窗口样式
    """
    def _Lf_init_style(self) -> None:
        self.setWindowTitle(MAIN_WINDOW_TITLE)
        self.resize(MAIN_WINDOW_WIDTH, MAIN_WINDOW_HEIGHT)
        self.setStyleSheet(MAIN_WINDOW_QSS)


    """
    private tool
    
    初始化布局
    """
    def _Lf_init_layout(self) -> None:
        self.L_nav_panel = LosNavPanel()
        self.L_content_area = LosContentArea()
        self.L_status_label = QLabel("● READY")
        self.L_version_label = QLabel("LosSc v0.1.0 · by LosAngelous")
        splitter = QSplitter(Qt.Orientation.Horizontal)                 # 水平分割
        splitter.addWidget(self.L_nav_panel)
        splitter.addWidget(self.L_content_area)
        splitter.setSizes([260, MAIN_WINDOW_WIDTH - 260])
        splitter.setStretchFactor(0, 0)                                 # 0 表示控制索引
        splitter.setStretchFactor(1, 1)                                 # 左侧的1 也是 右侧的1表示多吃掉剩下的空间
        splitter.setHandleWidth(2)
        splitter.setChildrenCollapsible(False)                          # 这个就是可以保证 不会被拖没
        self.setCentralWidget(splitter)
        status_bar = QStatusBar()
        status_bar.addWidget(self.L_status_label)
        status_bar.addPermanentWidget(self.L_version_label)
        self.setStatusBar(status_bar)
        self.L_content_area.Lf_switch_to("home")


    """
    private tool
    
    初始化信号与槽
    是 信号 连接 槽
    """
    def _Lf_init_connect(self) -> None:
        self.L_news_ct = LosNewsCT(self.L_content_area.L_pages)
        get_router().Ls_nav_selected.connect(self.L_content_area.Lf_switch_to)
        get_router().Ls_nav_selected.connect(self._Lf_on_nav_selected)



    """
    private slot
        
    """
    def _Lf_on_nav_selected(self, key: str) -> None:
        self.L_status_label.setText(f"● SELECTED  /  {key}")