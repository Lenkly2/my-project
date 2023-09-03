from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from random import randint


app = QApplication([])

window = QWidget()
window.setWindowTitle('вгадайте кнопку')
window.resize(500,500)

button = QPushButton("рандом")
label = QLabel("Угадай що")
lay = QVBoxLayout()
lay.addWidget(label)
lay.addWidget(button)

window.setLayout(lay)
def kol():
    a = randint(1,1000000)
    label.setText(str(a))

button.clicked.connect(kol)


window.show()
app.exec_()
