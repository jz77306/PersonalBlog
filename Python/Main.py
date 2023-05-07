
import sys, math, sip
import numpy as np      # 导入 numpy 并简写成 np

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from Widget import MainWindow
from Command import Command


class MainWidget(QMainWindow, MainWindow):  # 继承 QMainWindow 类和 Ui_MainWindow 界面类
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)  # 初始化父类
        self.setupUi(self)  # 继承 Ui_MainWindow 界面类

        self.pushButton.clicked.connect(Command.RunTestPage)  # type: ignore
        self.pushButton_2.clicked.connect(Command.StartTest)  # type: ignore
        return

if __name__ == '__main__':
    app = QApplication(sys.argv)  # 在 QApplication 方法中使用，创建应用程序对象
    myWin = MainWidget()  # 实例化 MyMainWindow 类，创建主窗口
    myWin.show()  # 在桌面显示控件 myWin
    sys.exit(app.exec_())  # 结束进程，退出程序