from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox, QListView, QTextEdit)

app = QApplication([])

window = QWidget()
width = 600
height = 500
window.resize(width, height)
window.move(300, 300)
window.setWindowTitle('НЕ Розумні замітки')

def savestonot():
    nerobotaet = "nexyi"

Vline = QVBoxLayout()
Vline1 = QVBoxLayout()
Hline = QHBoxLayout()
Hline2 = QHBoxLayout()
Hline3 = QHBoxLayout()

text = QTextEdit()
label1 = QLabel("Список заміток")
label2 = QLabel("Список тегів")
Button11 = QPushButton("Створити замітку")
Button21 = QPushButton("Видалити замітку")
Button31 = QPushButton("Зберегти замітку")

Button12 = QPushButton("Додати до замітки")
Button22 = QPushButton("Видалити від заміток")
Button32 = QPushButton("Шукати замітку по тегу")

viewl1 = QListWidget()
viewl2 = QListWidget()

serch = QLineEdit("Введіть тег")

Vline.addWidget(text)
Hline.addWidget(Button11)
Hline.addWidget(Button21)

Hline2.addWidget(Button12)
Hline2.addWidget(Button22)

Vline1.addWidget(label1)
Vline1.addWidget(viewl1)
Vline1.addLayout(Hline)
Vline1.addWidget(Button31)
Vline1.addWidget(label2)
Vline1.addWidget(viewl2)
Vline1.addWidget(serch)
Vline1.addLayout(Hline2)
Vline1.addWidget(Button32)

Hline3.addLayout(Vline)
Hline3.addLayout(Vline1)

window.setLayout(Hline3)








window.show()
app.exec_()