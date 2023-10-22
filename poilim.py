from PIL import Image, ImageFilter
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton,QLabel,QListWidget,QHBoxLayout,QVBoxLayout)

app = QApplication([])
window = QWidget()
window.resize(900,600)

popka = QPushButton("папка")
vlivo = QPushButton("вліво")
vpravo = QPushButton("вправо")
dzerkalo = QPushButton("відзеркалити")
rizkist = QPushButton("різкість")
zib = QPushButton("N\d")
imag = QLabel("картинка")
lest = QListWidget()

H1 = QHBoxLayout()
v1 = QVBoxLayout()
H2 = QHBoxLayout()
v2 = QVBoxLayout()

v1.addWidget(popka)
v1.addWidget(lest)
H1.addWidget(vlivo)
H1.addWidget(vpravo)
H1.addWidget(dzerkalo)
H1.addWidget(rizkist)
H1.addWidget(zib)
v2.addLayout(H1)
H2.addLayout(v1)
H2.addWidget(imag)
H2.addLayout(v2)
window.setLayout(H2)

window.show()
app.exec_()