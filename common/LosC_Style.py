# ==========================================
# LosScClient 全局样式表 (QSS)
#
# 设计原则：
#   - 黑白大气、极客风、端正、宽敞
#   - 主色：#0a0a0a (纯黑)
#   - 次级黑：#121212 / #1f1f1f / #2a2a2a
#   - 边框：#262626
#   - 文字主：#e5e5e5
#   - 文字次：#888888
#   - 文字弱：#555555
#   - 强调：#ffffff
# ==========================================


# ----- 颜色常量（Python 端可引用） -----
COLOR_BG_MAIN       = "#0a0a0a"
COLOR_BG_NAV        = "#121212"
COLOR_BG_CONTENT    = "#0a0a0a"
COLOR_BG_HOVER      = "#1f1f1f"
COLOR_BG_SELECTED   = "#2a2a2a"

COLOR_BORDER        = "#262626"
COLOR_BORDER_STRONG = "#ffffff"

COLOR_TEXT_MAIN     = "#e5e5e5"
COLOR_TEXT_SECOND   = "#888888"
COLOR_TEXT_DIM      = "#555555"
COLOR_TEXT_ACCENT   = "#ffffff"


# ----- 字体 -----
FONT_FAMILY_DEFAULT = "'Segoe UI', 'Microsoft YaHei', sans-serif"
FONT_FAMILY_MONO    = "'JetBrains Mono', 'Consolas', 'Courier New', monospace"


# ==========================================
# 主窗口样式
# ==========================================
MAIN_WINDOW_QSS = f"""
QMainWindow {{
    background-color: {COLOR_BG_MAIN};
}}

QWidget {{
    color: {COLOR_TEXT_MAIN};
    font-family: {FONT_FAMILY_DEFAULT};
    font-size: 14px;
}}

QSplitter::handle {{
    background-color: {COLOR_BORDER};
    width: 1px;
}}

QSplitter::handle:hover {{
    background-color: {COLOR_BORDER_STRONG};
}}

QStatusBar {{
    background-color: {COLOR_BG_NAV};
    color: {COLOR_TEXT_SECOND};
    border-top: 1px solid {COLOR_BORDER};
    padding: 4px 16px;
    font-family: {FONT_FAMILY_MONO};
    font-size: 12px;
}}

QStatusBar QLabel {{
    color: {COLOR_TEXT_SECOND};
    font-family: {FONT_FAMILY_MONO};
    font-size: 12px;
}}
"""


# ==========================================
# 左侧导航面板
# ==========================================
NAV_PANEL_QSS = f"""
#LosNavPanel {{
    background-color: {COLOR_BG_NAV};
    border-right: 1px solid {COLOR_BORDER};
}}

#NavBrand {{
    color: {COLOR_TEXT_ACCENT};
    font-family: {FONT_FAMILY_MONO};
    font-size: 22px;
    font-weight: bold;
    padding: 32px 24px 4px 24px;
    letter-spacing: 3px;
}}

#NavSubBrand {{
    color: {COLOR_TEXT_DIM};
    font-family: {FONT_FAMILY_MONO};
    font-size: 11px;
    padding: 0 24px 24px 24px;
    letter-spacing: 2px;
}}

#NavGroupLabel {{
    color: {COLOR_TEXT_DIM};
    font-family: {FONT_FAMILY_MONO};
    font-size: 11px;
    padding: 20px 24px 6px 24px;
    letter-spacing: 2px;
}}

QTreeWidget {{
    background-color: {COLOR_BG_NAV};
    border: none;
    outline: 0;
    padding: 4px 12px;
}}

QTreeWidget::item {{
    color: {COLOR_TEXT_MAIN};
    padding: 10px 8px;
    border: none;
    margin: 1px 0;
}}

QTreeWidget::item:hover {{
    background-color: {COLOR_BG_HOVER};
}}

QTreeWidget::item:selected {{
    background-color: {COLOR_BG_SELECTED};
    color: {COLOR_TEXT_ACCENT};
    border-left: 2px solid {COLOR_BORDER_STRONG};
}}

QTreeWidget::branch {{
    background-color: transparent;
}}

QTreeWidget::branch:has-siblings:!adjoins-item,
QTreeWidget::branch:has-siblings:adjoins-item,
QTreeWidget::branch:!has-children:!has-siblings:adjoins-item {{
    border-image: none;
    image: none;
}}
"""


# ==========================================
# 右侧内容区
# ==========================================
CONTENT_AREA_QSS = f"""
#LosContentArea {{
    background-color: {COLOR_BG_CONTENT};
}}
"""


# ==========================================
# 占位页（空页面）
# ==========================================
PAGE_PLACEHOLDER_QSS = f"""
#PagePlaceholder {{
    background-color: {COLOR_BG_CONTENT};
}}

#PageTitle {{
    color: {COLOR_TEXT_ACCENT};
    font-size: 34px;
    font-weight: 300;
    padding: 56px 56px 4px 56px;
    letter-spacing: 1px;
}}

#PageSubtitle {{
    color: {COLOR_TEXT_SECOND};
    font-family: {FONT_FAMILY_MONO};
    font-size: 13px;
    padding: 0 56px 32px 56px;
    letter-spacing: 1px;
}}

#PageDivider {{
    background-color: {COLOR_BORDER};
    min-height: 1px;
    max-height: 1px;
    margin: 0 56px;
    border: none;
}}

#PageBody {{
    color: {COLOR_TEXT_SECOND};
    font-size: 14px;
    padding: 48px 56px;
    line-height: 1.8;
}}
"""





# ==========================================
# 首页 Dashboard
# ==========================================
HOME_PAGE_QSS = f"""
#LosHomePage {{
    background-color: {COLOR_BG_CONTENT};
}}

#HomeTitle {{
    color: {COLOR_TEXT_ACCENT};
    font-family: {FONT_FAMILY_MONO};
    font-size: 34px;
    font-weight: bold;
    letter-spacing: 3px;
}}

#HomeSubtitle {{
    color: {COLOR_TEXT_SECOND};
    font-family: {FONT_FAMILY_MONO};
    font-size: 13px;
    letter-spacing: 1px;
}}

#HomeStatCard {{
    background-color: #111111;
    border: 1px solid {COLOR_BORDER};
    min-height: 130px;
}}

#HomeStatCard:hover {{
    border: 1px solid #555555;
    background-color: #151515;
}}

#HomeStatTitle {{
    color: {COLOR_TEXT_DIM};
    font-family: {FONT_FAMILY_MONO};
    font-size: 12px;
    letter-spacing: 2px;
}}

#HomeStatValue {{
    color: {COLOR_TEXT_ACCENT};
    font-family: {FONT_FAMILY_MONO};
    font-size: 28px;
    font-weight: bold;
}}

#HomeStatDesc {{
    color: {COLOR_TEXT_SECOND};
    font-family: {FONT_FAMILY_MONO};
    font-size: 12px;
}}

#SectionTitle {{
    color: {COLOR_TEXT_MAIN};
    font-family: {FONT_FAMILY_MONO};
    font-size: 14px;
    font-weight: bold;
    letter-spacing: 2px;
    padding-top: 8px;
}}

#HomeStreamBox {{
    background-color: #101010;
    border: 1px solid {COLOR_BORDER};
}}

#HomeStreamEmpty {{
    color: {COLOR_TEXT_SECOND};
    font-size: 14px;
    line-height: 1.8;
}}
"""




# ==========================================
# 搜索页
# ==========================================
SEARCH_PAGE_QSS = f"""
#LosSearchPage {{
    background-color: {COLOR_BG_CONTENT};
}}

#SearchTitle {{
    color: {COLOR_TEXT_ACCENT};
    font-family: {FONT_FAMILY_MONO};
    font-size: 34px;
    font-weight: bold;
    letter-spacing: 3px;
}}

#SearchSubtitle {{
    color: {COLOR_TEXT_SECOND};
    font-family: {FONT_FAMILY_MONO};
    font-size: 13px;
    letter-spacing: 1px;
}}

#SearchBar {{
    background-color: #101010;
    border: 1px solid {COLOR_BORDER};
}}

#SearchInput {{
    background-color: #0a0a0a;
    color: {COLOR_TEXT_MAIN};
    border: 1px solid {COLOR_BORDER};
    padding: 12px 14px;
    font-family: {FONT_FAMILY_MONO};
    font-size: 14px;
}}

#SearchInput:focus {{
    border: 1px solid #ffffff;
}}

#SearchButton {{
    background-color: #ffffff;
    color: #000000;
    border: 1px solid #ffffff;
    padding: 12px 18px;
    font-family: {FONT_FAMILY_MONO};
    font-size: 12px;
    font-weight: bold;
    letter-spacing: 1px;
}}

#SearchButton:hover {{
    background-color: #dcdcdc;
    border: 1px solid #dcdcdc;
}}

#SearchButton:pressed {{
    background-color: #999999;
    border: 1px solid #999999;
}}

#SearchResultBox {{
    background-color: #101010;
    border: 1px solid {COLOR_BORDER};
}}

#SearchResultEmpty {{
    color: {COLOR_TEXT_SECOND};
    font-size: 14px;
    line-height: 1.8;
}}
"""


# ==========================================
# 新闻列表页
# ==========================================
NEWS_LIST_PAGE_QSS = f"""
#LosNewsListPage {{
    background-color: {COLOR_BG_CONTENT};
}}

#NewsPageTitle {{
    color: {COLOR_TEXT_ACCENT};
    font-family: {FONT_FAMILY_MONO};
    font-size: 34px;
    font-weight: bold;
    letter-spacing: 3px;
}}

#NewsPageSubtitle {{
    color: {COLOR_TEXT_SECOND};
    font-family: {FONT_FAMILY_MONO};
    font-size: 13px;
    letter-spacing: 1px;
}}

#NewsListBox,
#NewsDetailBox {{
    background-color: #101010;
    border: 1px solid {COLOR_BORDER};
}}

#NewsSectionTitle {{
    color: {COLOR_TEXT_MAIN};
    font-family: {FONT_FAMILY_MONO};
    font-size: 13px;
    font-weight: bold;
    letter-spacing: 2px;
}}

#NewsEmptyText {{
    color: {COLOR_TEXT_SECOND};
    font-size: 14px;
    line-height: 1.8;
}}

#NewsItemLabel {{
    background-color: #0a0a0a;
    color: #dddddd;
    border: 1px solid #222222;
    padding: 14px 16px;
    font-family: {FONT_FAMILY_MONO};
    font-size: 12px;
    line-height: 1.6;
}}

#NewsItemButton {{
    background-color: #0a0a0a;
    color: #dddddd;
    border: 1px solid #222222;
    padding: 14px 16px;
    text-align: left;
    font-family: {FONT_FAMILY_MONO};
    font-size: 12px;
    line-height: 1.6;
}}

#NewsItemButton:hover {{
    background-color: #161616;
    border: 1px solid #555555;
}}

#NewsItemButton:pressed {{
    background-color: #222222;
    border: 1px solid #ffffff;
}}
"""