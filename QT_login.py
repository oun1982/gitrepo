import sys, socket
from PyQt5.QtWidgets import QApplication, QWidget, \
     QMainWindow,QPushButton, QMessageBox, QLineEdit, QLabel, QComboBox
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from gitrepo.QT_main import *
from PyQt5.QtCore import QSize, QRect

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Asterisk DialPlan'
        self.left = 500
        self.top = 200
        self.setFixedSize(400, 300)
        self.width = 400
        self.height = 300
        self.initUI()
        self.setMinimumSize(QSize(640, 140))

    def initUI(self):
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.statusBar().showMessage(ip)

        self.textbox_user = QLineEdit(self)
        self.textbox_user.move(100, 60)
        self.textbox_user.resize(200, 25)
        self.textbox_pass = QLineEdit(self)
        self.textbox_pass.setEchoMode(QLineEdit.Password)
        self.textbox_pass.move(100, 90)
        self.textbox_pass.resize(200, 25)
        self.textbox_host = QLineEdit(self)
        self.textbox_host.move(100, 120)
        self.textbox_host.resize(200, 25)

        lb_user = QLabel('User: ',self)
        lb_user.move(60,60)
        lb_pass = QLabel('Password: ', self)
        lb_pass.move(37, 90)
        lb_host = QLabel('Host: ', self)
        lb_host.move(61, 120)
        lb_eg = QLabel('e.g. 192.168.1.1 ', self)
        lb_eg.move(100, 150)

        submit = QPushButton('Submit', self)
        submit.setToolTip('submit button')
        submit.move(100, 180)
        submit.clicked.connect(self.on_click_submit)
        reset = QPushButton('Reset', self)
        reset.setToolTip('Clear data in dialog')
        reset.move(200, 180)
        reset.clicked.connect(self.on_click_reset)
        self.show()

    @pyqtSlot()

    def on_click_reset(self):
        self.textbox_user.setText("")
        self.textbox_pass.setText("")
        self.textbox_host.setText("")

    def on_click_submit(self):
        if self.textbox_user.text() == 'admin' and self.textbox_pass.text() == 'admin' and self.textbox_host.text() != "":
            textboxOK = self.textbox_user.text()
            QMessageBox.question(self, 'Asterisk Dialplan',' Login Success '
                                 , QMessageBox.Ok,QMessageBox.Cancel)
            self.textbox_user.setText("")
            self.hide()
            main = AppMain()
            main.show()

        else:
            QMessageBox.warning(self, 'Login Error ', ' Invalid Value !!!!! '
                                 ,QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())