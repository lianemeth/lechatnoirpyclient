from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

MAIN_WINDOW_SIZE = (400, 400, 400, 600)

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Le Chat Noir')
        self.setGeometry(*MAIN_WINDOW_SIZE)
        menu = self.menuBar()
        connect = menu.addMenu('&Connect')
        

class ClientAppUI(object):

    def __init__(self, argv, client):
        self.client = client
        self.app = QApplication(argv)
        self.window = MainWindow()

    def show_ui(self):
        self.window.show()

    def execute(self):
        return self.app.exec_()
