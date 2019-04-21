from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys


class WinForm(QWidget):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        self.resize(400, 90)
        self.setWindowTitle('对话框关闭时返回值给主窗口的例子')

        self.lineEdit = QLineEdit(self)
        self.button1 = QPushButton('弹出对话框1')
        self.button1.clicked.connect(self.onButton1Clicked)

        self.button2 = QPushButton('弹出对话框2')
        self.button2.clicked.connect(self.onButton2Clicked)

        gridLayout = QGridLayout(self)
        gridLayout.addWidget(self.lineEdit)
        gridLayout.addWidget(self.button1)
        gridLayout.addWidget(self.button2)

    def onButton1Clicked(self):
        dialog = DateDialog(self)
        result = dialog.exec_()
        date = dialog.dateTime()
        self.lineEdit.setText(date.date().toString())
        print('\n日期对话框的返回值')
        print('date=%s' % str(date.date))
        print('time=%s' % str(date.time()))
        print('result=%s' % result)

    def onButton2Clicked(self):
        date, time, result = DateDialog.getDateTime()
        self.lineEdit.setText(date.toString())
        print('\n 日期对话框的返回值')
        print('date=%s' % str(date))
        print('time=%s' % str(time))
        print('result=%s' % result)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = WinForm()
    form.show()
    sys.exit(app.exec_())

class DateDialog(QDialog):
    def __init__(self, parent=None):
        super(DateDialog, self).__init__(parent)
        self.setWindowTitle('DateDialog')

        # 在布局中添加控件
        layout = QVBoxLayout(self)
        self.datetime = QDateTimeEdit(self)
        self.datetime.setCalendarPopup(True)
        self.datetime.setDateTime(QDateTime.currentDateTime())
        layout.addWidget(self.datetime)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def dateTime(self):
        return self.datetime.dateTime()

    @staticmethod
    def getDateTime(parent=None):
        dialog = DateDialog(parent)
        result = dialog.exec_()
        date = dialog.dateTime()
        return (date.date(), date.time(), result == QDialog.Accepted)

class WinForm(QWidget):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        self.resize(400, 90)
        self.setWindowTitle('对话框关闭时返回值给主窗口的例子')

        self.lineEdit = QLineEdit(self)
        self.button1 = QPushButton('弹出对话框1')
        self.button1.clicked.connect(self.onButton1Clicked)

        self.button2 = QPushButton('弹出对话框2')
        self.button2.clicked.connect(self.onButton2Clicked)

        gridLayout = QGridLayout(self)
        gridLayout.addWidget(self.lineEdit)
        gridLayout.addWidget(self.button1)
        gridLayout.addWidget(self.button2)

    def onButton1Clicked(self):
        dialog = DateDialog(self)
        result = dialog.exec_()
        date = dialog.dateTime()
        self.lineEdit.setText(date.date().toString())
        print('\n日期对话框的返回值')
        print('date=%s' % str(date.date))
        print('time=%s' % str(date.time()))
        print('result=%s' % result)

    def onButton2Clicked(self):
        date, time, result = DateDialog.getDateTime()
        self.lineEdit.setText(date.toString())
        print('\n 日期对话框的返回值')
        print('date=%s' % str(date))
        print('time=%s' % str(time))
        print('result=%s' % result)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = WinForm()
    form.show()
    sys.exit(app.exec_())
# ---------------------
# 作者：jia666666
# 来源：CSDN
# 原文：https://blog.csdn.net/jia666666/article/details/81781697
# 版权声明：本文为博主原创文章，转载请附上博文链接！
