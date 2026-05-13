import sys
from PySide6.QtWidgets import QApplication

from view.LosMainWindow import LosMainWindow

def main() -> None:
    app = QApplication(sys.argv)
    window = LosMainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()