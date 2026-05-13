from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame
from PySide6.QtCore import Qt

from common.LosC_Style import PAGE_PLACEHOLDER_QSS


class LosPagePlaceholder(QWidget):
    """
    占位页
    用于各导航项暂时没实现的页面占位
    """


    def __init__(self, title: str, subtitle: str = "", body: str = "") -> None:
        super().__init__()
        self.setObjectName("PagePlaceholder")
        self.setStyleSheet(PAGE_PLACEHOLDER_QSS)

        self.L_title    = title
        self.L_subtitle = subtitle
        self.L_body     = body

        self._Lf_init_layout()


    """
    private tool
    
    初始化布局
    """
    def _Lf_init_layout(self) -> None:
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # 标题
        title_label = QLabel(self.L_title)
        title_label.setObjectName("PageTitle")

        # 副标题（路径标识，用等宽字体）
        subtitle_label = QLabel(self.L_subtitle)
        subtitle_label.setObjectName("PageSubtitle")

        # 分隔线
        divider = QFrame()
        divider.setObjectName("PageDivider")

        # 正文
        body_label = QLabel(self.L_body if self.L_body else "此页面尚未实现 · COMING SOON")
        body_label.setObjectName("PageBody")
        body_label.setWordWrap(True)
        body_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        layout.addWidget(title_label)
        layout.addWidget(subtitle_label)
        layout.addWidget(divider)
        layout.addWidget(body_label)
        layout.addStretch(1)
