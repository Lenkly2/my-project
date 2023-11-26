from PIL import Image, ImageFilter
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton,
                             QLabel,QListWidget,QHBoxLayout,QVBoxLayout,QFileDialog)
import os
app = QApplication([])
window = QWidget()
window.setWindowTitle("Порожнє вікно")
app.setStyle('Fusion')

popka = QPushButton("папка")
vlivo = QPushButton("вліво")
vpravo = QPushButton("вправо")
dzerkalo = QPushButton("відзеркалити")
rizkist = QPushButton("різкість")
blw = QPushButton("B/W")
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
H1.addWidget(blw)
v2.addWidget(imag)
v2.addLayout(H1)
H2.addLayout(v1)
H2.addLayout(v2)
window.setLayout(H2)

def filter(files,extensions):
    result = []
    for f in files:
        for e in extensions:
            if f.endswith(e):
                result.append(f)
    return result
def choise_work():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def show_file():
    extensions = ['jpeg','png','jpg','svg','py','docx','pdf','exe','mp4','mp3']
    choise_work()
    filenames = filter(os.listdir(workdir),extensions)
    lest.clear()
    for f in filenames:
        lest.addItem(f)
popka.clicked.connect(show_file)

class Image():
    def __init__(self):
        self.dir = None
        self.image = None
        self.name = None
    def loadimage(self,dir,name):
        self.dir = dir
        self.name = name
        image_path = os.path.join(dir,name)
        self.image = Image.open(image_path)
    def showimage(self,path):
        image.hide()
        pixmapimage = QPixmap(path)
        w, h = image.width(), image.height()
        pixmapimage = pixmapimage.scaled(w,h, Qt.KeepAspectRadio)
        image.setPixmap(pixmapimage)
        image.show()

workimage = Image()
window.show()
app.exec_()