from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction,
                             QLineEdit, QLabel, QPushButton)


MAIN_WINDOW_SIZE = (400, 400, 400, 600)
NEW_CONN_WINDOW_SIZE = (200, 200, 200, 250)


class ConnectWindow(QMainWindow):

    def create_field(self, text):
        label = QLabel(self)
        label.move(5, self.position)
        self.position += 20
        label.setText(text)
        label.adjustSize()
        field = QLineEdit(self)
        field.move(5, self.position)
        self.position += 30
        return field

    def __init__(self):
        super().__init__()
        self.setWindowTitle('New Connection')
        self.setGeometry(*NEW_CONN_WINDOW_SIZE)
        self.position = 0
        self.create_field('Host')
        self.create_field('Post')
        self.create_field('User')
        button = QPushButton('ok', self)
        button.move(50, self.position + 30)


class MainWindow(QMainWindow):

    def __init__(self, main_ui):
        super().__init__()
        self.main_ui = main_ui
        self.setWindowTitle('Le Chat Noir')
        self.setGeometry(*MAIN_WINDOW_SIZE)
        self.menu = self.menuBar()
        self.connect_menu = self.menu.addMenu('&Connections')
        self.connect_menu.addAction("&New Connection")
        self.connect_window = ConnectWindow()
        self.connect_menu.triggered[QAction].connect(self.open_connect_window)

    def open_connect_window(self, q):
        self.connect_window.show()


class ClientAppUI(object):

    def __init__(self, argv, client):
        self.client = client
        self.app = QApplication(argv)
        self.window = MainWindow(self)

    def show_ui(self):
        self.window.show()

    def execute(self):
        return self.app.exec_()
