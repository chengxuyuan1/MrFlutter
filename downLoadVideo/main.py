import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow

import helloWord
import DownVideoSigle


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = helloWord.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.webEngineView.setUrl(QtCore.QUrl("https://www.youtube.com/watch?v=zxaI2v7ZqDk"))
    ui.pushButton.clicked.connect(lambda:DownVideoSigle.handle_camsave(ui))
    MainWindow.show()
    sys.exit(app.exec_())





