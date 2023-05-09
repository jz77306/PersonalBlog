
import sys, math, sip
import numpy as np      # 导入 numpy 并简写成 np
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from Widget import Ui_Dialog
import datetime
import  os


class MainWidget(QMainWindow, Ui_Dialog):  # 继承 QMainWindow 类和 Ui_MainWindow 界面类
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)  # 初始化父类
        self.setupUi(self)  # 继承 Ui_MainWindow 界面类

        self.pushButton.clicked.connect(self.RunTestPage)  # type: ignore
        self.pushButton_2.clicked.connect(self.StartTest)  # type: ignore
        self.pushButton_3.clicked.connect(self.MakePost)  # type: ignore
        return

    def StartTest(self):
        # cmd = 'cmd.exe c:\\sam.bat'
        p = subprocess.Popen("cmd.exe /c" + "StartTest.bat", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        curline = p.stdout.readline()
        while (curline != b''):
            print(curline)
            curline = p.stdout.readline()
        print(p.returncode)
        return

    def RunTestPage(self):
        p = subprocess.Popen("cmd.exe /c" + "RunTestPage.bat", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        curline = p.stdout.readline()
        while (curline != b''):
            print(curline)
            curline = p.stdout.readline()
        print(p.returncode)
        return

    def getInit(self):      #获取用户输入的作者与文章信息
        author = self.AuthorEdit.text()
        title = self.TitleEdit.text()
        return author, title


    def txt2Md(self, filename):      #文本转Markdown文件
        os.rename(filename, f"{filename}.md")
        return

    def initMD(self, filename):      #Markdown文件初始化
        content = []
        # 打开文件并写入内容
        with open(filename, "w") as f:
            for line in content:
                f.write(line + "\n")
        return

    def makeFile(self, author, Title):  #创建文章
        # 设置文件名和后缀
        newfile = f"{author}_{Title}.txt"
        filename = f"{author}_{Title}"
        suffix = 0
        # 如果文件已经存在，则增加一个数字后缀
        while os.path.isfile(newfile):
            suffix += 1
            newfile = f"{author}_{Title}({suffix}).txt"
            filename = f"{author}_{Title}({suffix})"
        f = open(newfile, "w")
        f.close()
        print(f"文件 {newfile} 创建成功！")
        return filename

    def MakePost(self):
        print(type(Ui_Dialog))
        author, title = self.getInit()
        filename = self.makeFile(author, title)
        initMD(filename)

        return

if __name__ == '__main__':
    app = QApplication(sys.argv)  # 在 QApplication 方法中使用，创建应用程序对象
    myWin = MainWidget()  # 实例化 MyMainWindow 类，创建主窗口
    myWin.show()  # 在桌面显示控件 myWin
    sys.exit(app.exec_())  # 结束进程，退出程序