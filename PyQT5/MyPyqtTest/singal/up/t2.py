from PyQt5.QtCore import QObject, pyqtSignal


# 信号对象
class QTypeSignal(QObject):
    # 定义一个信号
    # sendmsg = pyqtSignal(object)
    # todo 优化 多个参数传递
    sendmsg = pyqtSignal(str, str)

    def __init__(self):
        super(QTypeSignal, self).__init__()

    def run(self):
        # 发射信号
        # self.sendmsg.emit('hell')

        # todo 优化 发射多个参数
        self.sendmsg.emit('第一参数', '第二个参数')


# 槽对象
class QTypeSlot(QObject):
    def __init__(self):
        super(QTypeSlot, self).__init__()

    # 槽对象中的槽函数
    # def get( self,msg ):
    #     print("QSlot get msg => " + msg)

    # todo 优化 多个参数
    def get(self, msg1, msg2):
        print("QSlot get msg => " + msg1 + ' ' + msg2)


if __name__ == '__main__':
    # 实例化信号对象
    send = QTypeSignal()
    # 实例化槽对象
    slot = QTypeSlot()

    # 1
    print('_____-把信号绑定到槽函数上_)___')
    send.sendmsg.connect(slot.get)

    send.run()

    print('_____-把信号与槽函数解绑_)___')
    send.sendmsg.disconnect(slot.get)

    send.run()
