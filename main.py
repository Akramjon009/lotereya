from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QApplication, QListWidget, QWidget
from sys import argv,exit
from steel import *
from PyQt5.Qt import Qt
class Latareya(Window):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1000, 800)
        self.btn_1 = Button("1")
        self.btn_2 = Button("2")
        self.btn_3 = Button("3")
        self.btn_4 = Button("4")
        self.btn_5 = Button("5")
        self.btn_6 = Button("6")
        self.btn_7 = Button("7")
        self.btn_8 = Button("8")
        self.btn_9 = Button("9")
        self.btn_10 = Button("10")
        self.btn_11 = Button("11")
        self.btn_12 = Button("12")
        self.btn_13 = Button("13")
        self.btn_14 = Button("14")
        self.btn_15 = Button("15")
        self.btn_16 = Button("16")
        self.btn_17 = Button("17")
        self.btn_18 = Button("18")
        self.btn_19 = Button("19")
        self.btn_20 = Button("20")
        self.btn_21 = Button("21")
        self.btn_22 = Button("22")
        self.btn_23 = Button("23")
        self.btn_24 = Button("24")
        self.btn_25 = Button("25")
        self.btn_26 = Button("26")
        self.btn_27 = Button("27")
        self.btn_28 = Button("28")
        self.btn_29 = Button("29")
        self.btn_30 = Button("30")
        self.btn_31 = Button("31")
        self.btn_32 = Button("32")
        self.btn_33 = Button("33")
        self.btn_34 = Button("34")
        self.btn_35 = Button("35")
        self.btn_36 = Button("36")

        self.label = Label(" ")
        self.label1 = Label(" ")
        self.label_circl1 = Label_to_circle(" ")
        self.label_circl2 = Label_to_circle(" ")
        self.label_circl3 = Label_to_circle(" ")
        self.label_circl4 = Label_to_circle(" ")
        self.label_circl5 = Label_to_circle(" ")
        self.label_circl6 = Label_to_circle(" ")

        self.btn_start = Button("Start")
        self.btn_restart = Button("Restart")
        self.btn_0 = Button("+")

        self.box_2_1 = QHBoxLayout()


        self.box_0 = QHBoxLayout()
        self.box_1 = QHBoxLayout()
        self.box_2 = QHBoxLayout()
        self.box_3 = QHBoxLayout()
        self.box_4 = QHBoxLayout()
        self.box_5 = QHBoxLayout()
        self.box_6 = QHBoxLayout()

        self.box_H = QHBoxLayout()
        self.box_v1 = QVBoxLayout()
        self.box_v2 = QVBoxLayout()

        self.box_0.addWidget(self.label)
        self.box_0.addWidget(self.btn_0)

        self.box_1.addWidget(self.btn_1)
        self.box_1.addWidget(self.btn_2)
        self.box_1.addWidget(self.btn_3)
        self.box_1.addWidget(self.btn_4)
        self.box_1.addWidget(self.btn_5)
        self.box_1.addWidget(self.btn_6)

        self.box_2.addWidget(self.btn_7)
        self.box_2.addWidget(self.btn_8)
        self.box_2.addWidget(self.btn_9)
        self.box_2.addWidget(self.btn_10)
        self.box_2.addWidget(self.btn_11)
        self.box_2.addWidget(self.btn_12)

        self.box_3.addWidget(self.btn_13)
        self.box_3.addWidget(self.btn_14)
        self.box_3.addWidget(self.btn_15)
        self.box_3.addWidget(self.btn_16)
        self.box_3.addWidget(self.btn_17)
        self.box_3.addWidget(self.btn_18)

        self.box_4.addWidget(self.btn_19)
        self.box_4.addWidget(self.btn_20)
        self.box_4.addWidget(self.btn_21)
        self.box_4.addWidget(self.btn_22)
        self.box_4.addWidget(self.btn_23)
        self.box_4.addWidget(self.btn_24)

        self.box_5.addWidget(self.btn_25)
        self.box_5.addWidget(self.btn_26)
        self.box_5.addWidget(self.btn_27)
        self.box_5.addWidget(self.btn_28)
        self.box_5.addWidget(self.btn_29)
        self.box_5.addWidget(self.btn_30)

        self.box_6.addWidget(self.btn_31)
        self.box_6.addWidget(self.btn_32)
        self.box_6.addWidget(self.btn_33)
        self.box_6.addWidget(self.btn_34)
        self.box_6.addWidget(self.btn_35)
        self.box_6.addWidget(self.btn_36)

        self.box_2_1.addWidget(self.btn_start)
        self.box_2_1.addWidget(self.label_circl1)
        self.box_2_1.addWidget(self.label_circl2)
        self.box_2_1.addWidget(self.label_circl3)
        self.box_2_1.addWidget(self.label_circl4)
        self.box_2_1.addWidget(self.label_circl5)
        self.box_2_1.addWidget(self.label_circl6)

        self.box_v2.addLayout(self.box_2_1)
        self.box_v2.addWidget(self.label1)
        self.box_v2.addWidget(self.btn_restart)


        self.box_v1.addLayout(self.box_0)
        self.box_v1.addLayout(self.box_1)
        self.box_v1.addLayout(self.box_2)
        self.box_v1.addLayout(self.box_3)
        self.box_v1.addLayout(self.box_4)
        self.box_v1.addLayout(self.box_5)
        self.box_v1.addLayout(self.box_6)

        self.box_v1.setAlignment(Qt.AlignLeft)

        self.box_H.addLayout(self.box_v1)
        self.box_H.addLayout(self.box_v2)

        self.setLayout(self.box_H)

app = QApplication(argv)
menu = Latareya()
menu.show()
exit(app.exec_())



