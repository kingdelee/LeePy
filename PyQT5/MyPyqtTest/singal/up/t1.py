import sys
from PyQt5.QtWidgets import QMessageBox, QPushButton, QApplication, QWidget

app = QApplication(sys.argv)
widget = QWidget()


def showMsg():
    QMessageBox.information(widget, '信息提示框', 'Ok 弹出测试信息')


btn = QPushButton('测试点击按钮', widget)

btn.clicked.connect(showMsg)

widget.show()
sys.exit(app.exec_())
