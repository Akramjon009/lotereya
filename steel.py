from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QListWidget, QLabel
from PyQt5.QtGui import QIcon


class QLW(QListWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""background: #fff; 
                           border: 1px solid; 
                           border-radius: 15px;
                           font-size: 20px;
                           padding: 5px 
                           """)


class Label(QLabel):
    def __init__(self, text):
        super().__init__(text)
        self.setStyleSheet("""
                           font-size: 20px;
                           border: 2px solid;
                           border-radius: 5px;
                           color: white;
                           background-color:white;
                           padding: 5px 
                           """)

class Label_to_circle(QLabel):
    def __init__(self, text):
        super().__init__(text)
        self.setFixedSize(50,30)
        self.setStyleSheet("""
                           font-size: 5px;
                           border: 2px solid;
                           border-radius: 10px;
                           background-color:white;
                           border-color: orange;
                           padding: 1px 
                           """)


class Button(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.setFixedSize(80, 70)
        self.setStyleSheet("""background: #79AC78; 
                           border: 2px solid; 
                           border-radius: 25px;
                           font-size: 18px; 
                           margin: 5 0""")


class Edit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""background: #B0D9B1; 
                           border: 1px solid; 
                           border-radius: 5px;
                           font-size: 25px;
                            padding-left: 5px
                           """)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1000, 900)
        self.setStyleSheet("background: #D0E7D2")
        self.setWindowIcon(QIcon('icon.png'))