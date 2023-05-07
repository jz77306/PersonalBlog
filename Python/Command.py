# python 调用bat文件夹
import subprocess
import  os

class Command:
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
