import os
from PyQt5.QtWidgets import (
   QApplication, QWidget,
   QFileDialog,
   QLabel, QPushButton, QListWidget,
   QHBoxLayout, QVBoxLayout
)
from PyQt5.QtCore import Qt # потрібна константа Qt.KeepAspectRatio для зміни розмірів із збереженням пропорцій
from PyQt5.QtGui import QPixmap # оптимізована для показу на екрані картинка
 
from PIL import Image


from PIL import ImageFilter
from PIL.ImageFilter import (
   BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN,
   GaussianBlur, UnsharpMask )


###############################
app = QApplication([])
main = QWidget()
main.setWindowTitle('Порожнє вікно')
main.show()


image = QLabel("!")
btn_left = QPushButton('Вліво')
btn_right = QPushButton('Вправо')
btn_mirror = QPushButton('Дзеркало')
btn_sharp = QPushButton('Різкість')
btn_bw = QPushButton('чб')
btn_folder = QPushButton('Папка')
btn_countor = QPushButton('Контур')

list1 = QListWidget()


v1 = QVBoxLayout()
v1.addWidget(btn_folder)
v1.addWidget(list1)
h1 = QHBoxLayout()
h1.addWidget(btn_left)
h1.addWidget(btn_right)
h1.addWidget(btn_mirror)
h1.addWidget(btn_sharp)
h1.addWidget(btn_bw)
h1.addWidget(btn_countor)
v2 = QVBoxLayout()
v2.addWidget(image)
v2.addLayout(h1)
h2 = QHBoxLayout()
h2.addLayout(v1)
h2.addLayout(v2)
main.setLayout(h2)


def choise_workdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory() #получаємо шлях з обраної папки
   
def filter(files,extensions):
    result = []
    for f in files:
        for e in extensions:
            if f.endswith(e):
                result.append(f)
    return result


def showfiles():
    extensions = ['jpeg','png','svg','jpg']
    choise_workdir()
    filenames = filter(os.listdir(workdir),extensions) # витягуємо файли з вказаного шляху
    list1.clear()
    for f in filenames:
        list1.addItem(f)
btn_folder.clicked.connect(showfiles)




class ImageProcessor():
   def __init__(self):
       self.image = None
       self.dir = None
       self.filename = None
       self.save_dir = "Modified/"
 
   def loadImage(self, filename):

       self.filename = filename
       fullname = os.path.join(workdir, filename)
       self.image = Image.open(fullname)
 
   def saveImage(self):

       path = os.path.join(workdir, self.save_dir)
       if not(os.path.exists(path) or os.path.isdir(path)):
           os.mkdir(path)
       fullname = os.path.join(path, self.filename)
 
       self.image.save(fullname)
    ###############
   def do_bw(self):
       self.image = self.image.convert("L")
       self.saveImage()
       image_path = os.path.join(workdir, self.save_dir, self.filename)
       self.showImage(image_path)
 


    ##################################
   def showImage(self, path):
       image.hide()
       pixmapimage = QPixmap(path)
       w, h = image.width(), image.height()
       pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
       image.setPixmap(pixmapimage)
       image.show()

   def do_right(self):
       self.image = self.image.transpose(Image.ROTATE_270)
       self.saveImage()
       image_path = os.path.join(workdir, self.save_dir, self.filename)
       self.showImage(image_path)

   def do_left(self):
       self.image = self.image.transpose(Image.ROTATE_90)
       self.saveImage()
       image_path = os.path.join(workdir, self.save_dir, self.filename)
       self.showImage(image_path)

   def do_dzerkalo(self):
       self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
       self.saveImage()
       image_path = os.path.join(workdir, self.save_dir, self.filename)
       self.showImage(image_path)
    
   def do_rozmita(self):
       self.image = self.image.filter(ImageFilter.BLUR)
       self.saveImage()
       image_path = os.path.join(workdir, self.save_dir, self.filename)
       self.showImage(image_path)
       
   def do_CONTOUR(self):
       self.image = self.image.filter(ImageFilter.CONTOUR)
       self.saveImage()
       image_path = os.path.join(workdir, self.save_dir, self.filename)
       self.showImage(image_path)

def showChosenImage():
   if list1.currentRow() >= 0:
       filename = list1.currentItem().text()
       workimage.loadImage(filename)
       workimage.showImage(os.path.join(workdir, workimage.filename))
 
workimage = ImageProcessor() #поточне робоче зображення для роботи
list1.currentRowChanged.connect(showChosenImage)
 
btn_bw.clicked.connect(workimage.do_bw)
btn_right.clicked.connect(workimage.do_right)
btn_left.clicked.connect(workimage.do_left)
btn_mirror.clicked.connect(workimage.do_dzerkalo)
btn_sharp.clicked.connect(workimage.do_rozmita)
btn_countor.clicked.connect(workimage.do_CONTOUR)
app.exec()

