from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTreeWidget, QTreeWidgetItem,
)
from PySide6.QtCore import Qt, Signal

from common.LosC_Style import NAV_PANEL_QSS
from common.LosC_Nav import NAV_TOP_ITEMS, NAV_NEWS_GROUPS, NAV_BOTTOM_ITEMS

from controller.LosRouter import get_router

class LosNavPanel(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setObjectName("LosNavPanel")
        self.setStyleSheet(NAV_PANEL_QSS)

        self._Lf_init_layout()
        self._Lf_init_connect()


    """
    private tool
    
    初始化布局
    """
    def _Lf_init_layout(self) -> None:
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        brand = QLabel("LOSSC")
        brand.setObjectName("NavBrand")

        sub_brand = QLabel("NEWS · CLIENT")
        sub_brand.setObjectName("NavSubBrand")

        layout.addWidget(brand)
        layout.addWidget(sub_brand)

        top_group_label = QLabel("— NAVIGATION")
        top_group_label.setObjectName("NavGroupLabel")
        layout.addWidget(top_group_label)

        self.L_tree_top = self._Lf_make_tree_flat(NAV_TOP_ITEMS)
        layout.addWidget(self.L_tree_top)

        sources_label = QLabel("— SOURCES")
        sources_label.setObjectName("NavGroupLabel")
        layout.addWidget(sources_label)

        self.L_tree_news = self._Lf_make_tree_groups(NAV_NEWS_GROUPS)
        layout.addWidget(self.L_tree_news)

        layout.addStretch(1)

        system_label = QLabel("— SYSTEM")
        system_label.setObjectName("NavGroupLabel")
        layout.addWidget(system_label)

        self.L_tree_bottom = self._Lf_make_tree_flat(NAV_BOTTOM_ITEMS)
        layout.addWidget(self.L_tree_bottom)

        bottom_spacer = QLabel(" ")
        bottom_spacer.setFixedHeight(16)
        layout.addWidget(bottom_spacer)


    """
    private tool
    
    构造平铺结构的树（无子项）
    """
    def _Lf_make_tree_flat(self, items: list) -> QTreeWidget:
        tree = QTreeWidget()
        tree.setHeaderHidden(True)
        tree.setIndentation(0)
        tree.setRootIsDecorated(False)
        tree.setUniformRowHeights(True)
        tree.setFrameShape(QTreeWidget.Shape.NoFrame)

        for item in items:
            node = QTreeWidgetItem([f"  {item['title']}"])
            node.setData(0, Qt.ItemDataRole.UserRole, item["key"])
            tree.addTopLevelItem(node)

        # 高度自适应项数
        tree.setFixedHeight(42 * len(items) + 10)
        return tree


    """
    private tool
    
    构造带分组的树（有子项）
    """
    def _Lf_make_tree_groups(self, groups: list) -> QTreeWidget:
        tree = QTreeWidget()
        tree.setHeaderHidden(True)
        tree.setIndentation(18)
        tree.setRootIsDecorated(True)
        tree.setUniformRowHeights(True)
        tree.setAnimated(True)
        tree.setFrameShape(QTreeWidget.Shape.NoFrame)

        for group in groups:
            parent = QTreeWidgetItem([f"  {group['title']}"])
            parent.setData(0, Qt.ItemDataRole.UserRole, group["key"])
            for child in group["children"]:
                child_node = QTreeWidgetItem([f"  {child['title']}"])
                child_node.setData(0, Qt.ItemDataRole.UserRole, child["key"])
                parent.addChild(child_node)
            tree.addTopLevelItem(parent)
            parent.setExpanded(True)

        total_rows = sum(1 + len(g["children"]) for g in groups)
        tree.setFixedHeight(42 * total_rows + 10)
        return tree


    """
    private tool
    
    连接信号
    """
    def _Lf_init_connect(self) -> None:
        self.L_tree_top.itemClicked.connect(self._Lf_on_item_clicked)
        self.L_tree_news.itemClicked.connect(self._Lf_on_item_clicked)
        self.L_tree_bottom.itemClicked.connect(self._Lf_on_item_clicked)


    """
    private slot
    
    任意树项被点击时触发，统一转发一个 key 信号
    """
    def _Lf_on_item_clicked(self, item: QTreeWidgetItem, column: int) -> None:
        key = item.data(0, Qt.ItemDataRole.UserRole)
        if key:
            get_router().Ls_nav_selected.emit(key)
