from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox, QListView)

app = QApplication([])

window = QWidget()
width = 600
height = 500
window.resize(width, height)
window.move(300, 300)
window.setWindowTitle('Memory Card')

button1 = QPushButton("нове питання")
button2 = QPushButton("видалити питання")
button3 = QPushButton("почати тренування")

text = QListView()

line1 = QLineEdit()
line2 = QLineEdit()
line3 = QLineEdit()
line4 = QLineEdit()
line5 = QLineEdit()

form = QFormLayout()
form.addRow('питання',line1)
form.addRow('Правильна відповідь',line2)
form.addRow('Неправильна відповідь',line3)
form.addRow('Неправильна відповідь',line4)
form.addRow('Неправильна відповідь',line5)

layautV = QVBoxLayout()
layautH = QHBoxLayout()
layautH2 = QHBoxLayout()
layautH3 = QHBoxLayout()

layautH.addWidget(text)
layautH.addLayout(form)
layautH2.addWidget(button1)
layautH2.addWidget(button2)
layautH3.addWidget(button3)

layautV.addLayout(layautH)
layautV.addLayout(layautH2)
layautV.addLayout(layautH3)

window.setLayout(layautV)

window.show()
app.exec_()