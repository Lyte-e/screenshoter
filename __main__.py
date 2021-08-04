import sys
from PyQt5.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)

    from src.handler import Handler
    Handler.start()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
