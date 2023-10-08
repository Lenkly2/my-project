from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox, QListView, QTextEdit, QInputDialog)

import json

app = QApplication([])


window = QWidget()
width = 600
height = 500
window.resize(width, height)
window.move(300, 300)
window.setWindowTitle('НЕ Розумні замітки')


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
Button11.setStyleSheet('background: rgb(255,0,0);')
Button21.setStyleSheet('background: rgb(255,0,0);')
Button31.setStyleSheet('background: rgb(255,0,0);')
Button12 = QPushButton("Додати до замітки")
Button22 = QPushButton("Видалити від заміток")
Button32 = QPushButton("Шукати замітку по тегу")
Button12.setStyleSheet('background: rgb(255,0,0);')
Button22.setStyleSheet('background: rgb(255,0,0);')
Button32.setStyleSheet('background: rgb(255,0,0);')


viewl1 = QListWidget()
viewl2 = QListWidget()
viewl1.setStyleSheet('background: rgb(255,0,0);')
viewl2.setStyleSheet('background: rgb(255,0,0);')
serch = QLineEdit("")
serch.setPlaceholderText("Введіть тег")
serch.setStyleSheet('background: rgb(255,0,0);')

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


def shownotes():
    key = viewl1.selectedItems()[0].text()
    text.setText(notes[key]["text"])

def addnote():
    note_name, ok = QInputDialog.getText(window,'додати замітку', "Назва замітки")
    if note_name and ok != "":
        notes[note_name] = {"text":"",'tegs':[]}
        viewl1.addItem(note_name)


def savetext():
    if viewl1.selectedItems():
        key = viewl1.selectedItems()[0].text()
        notes[key]["text"] = text.toPlainText()
        with open("saves.json","w") as file:
            json.dump(notes,file)

def del_notes():
    if viewl1.selectedItems():
        key = viewl1.selectedItems()[0].text()
        del notes[key]
        text.clear()
        viewl1.clear()
        viewl1.addItems(notes)
        with open ('saves.json','w') as file:
            json.dump(notes,file)


Button31.clicked.connect(savetext)
Button21.clicked.connect(del_notes)

viewl1.itemClicked.connect(shownotes)
Button11.clicked.connect(addnote)
window.show()
with open("saves.json",'r') as file:
    notes = json.load(file)
viewl1.addItems(notes)
app.exec_()