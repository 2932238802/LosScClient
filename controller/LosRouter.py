
from PySide6.QtCore import QObject, Signal
class LosRouter(QObject):
    # 导航栏 被选中
    Ls_nav_selected = Signal(str)
        
    def __init__(self) -> None:
        super().__init__()
        
    
_router: LosRouter|None = None
def get_router():
    global _router
    if _router is None:
        _router = LosRouter()
        return _router
    else:
        return _router
    
    
