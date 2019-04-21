# QDialog对话框使用
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QApplication, QHBoxLayout, QDialog, QPushButton, QMainWindow, \
    QGridLayout, QLabel

from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import Qt

import sys


class WindowClass(QWidget):

    def __init__(self, parent=None):
        super(WindowClass, self).__init__(parent)
        layout = QVBoxLayout()
        self.btn = QPushButton()
        self.btn.setText("显示对话框")
        self.btn.clicked.connect(self.showDialog)
        self.resize(500, 500)
        layout.addWidget(self.btn)

        self.setLayout(layout)

    def showDialog(self):
        vbox = QVBoxLayout()  # 纵向布局
        hbox = QHBoxLayout()  # 横向布局
        panel = QLabel()
        panel.setText("确定保存信息？")
        self.dialog = QDialog()
        self.dialog.resize(100, 100)
        self.okBtn = QPushButton("确定")
        self.cancelBtn = QPushButton("取消")

        # 绑定事件
        self.okBtn.clicked.connect(self.ok)
        self.cancelBtn.clicked.connect(self.cancel)

        self.dialog.setWindowTitle("提示信息！")
        # okBtn.move(50,50)#使用layout布局设置，因此move效果失效
        # 确定与取消按钮横向布局
        hbox.addWidget(self.okBtn)
        hbox.addWidget(self.cancelBtn)

        # 消息label与按钮组合纵向布局
        vbox.addWidget(panel)
        vbox.addLayout(hbox)
        self.dialog.setLayout(vbox)

        self.dialog.setWindowModality(Qt.ApplicationModal)  # 该模式下，只有该dialog关闭，才可以关闭父界面
        self.dialog.exec_()

    # 槽函数如下：
    def ok(self):
        print("确定保存！")
        self.dialog.close()

    def cancel(self):
        print("取消保存！")
        self.dialog.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WindowClass()
    win.show()
    sys.exit(app.exec_())
