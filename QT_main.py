import sys, socket
from PyQt5.QtWidgets import QApplication, QWidget, \
     QMainWindow,QPushButton, QMessageBox, QLineEdit, QLabel
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon

class AppMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Asterisk DialPlan'
        self.left = 100
        self.top = 60
        self.width = 1200
        self.height = 600
        self.setFixedSize(1200, 600)
        self.initUI()

    def initUI(self):
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.statusBar().showMessage(ip)
        self.show()

    @pyqtSlot()
    def on_click_submit(self):
        if self.textbox_user.text() == 'admin' and self.textbox_pass.text() == 'password' and self.textbox_host.text() != "":
            textboxOK = self.textbox_user.text()
            QMessageBox.question(self, 'Asterisk Dialplan',' Login Success '
                                 , QMessageBox.Ok,QMessageBox.Cancel)
            self.textbox_user.setText("")
            self.hide()

        else:
            QMessageBox.warning(self, 'Login Error ', ' Invalid Value !!!!! '
                                 ,QMessageBox.Ok)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AppMain()
    sys.exit(app.exec_())