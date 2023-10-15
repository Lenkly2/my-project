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
Button11.setStyleSheet('background: rgb(0,130,255);')
Button21.setStyleSheet('background: rgb(0,130,255);')
Button31.setStyleSheet('background: rgb(0,130,255);')
Button12 = QPushButton("Додати до замітки")
Button22 = QPushButton("Видалити від заміток")
Button32 = QPushButton("Шукати замітку по тегу")
Button12.setStyleSheet('background: rgb(0,130,255);')
Button22.setStyleSheet('background: rgb(0,130,255);')
Button32.setStyleSheet('background: rgb(0,130,255);')


viewl1 = QListWidget()
viewl2 = QListWidget()
serch = QLineEdit("")
serch.setPlaceholderText("Введіть тег")


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
    viewl2.clear()
    viewl2.addItems(notes[key]['tegs'])
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

def addtags():
    if viewl1.selectedItems():
        key = viewl1.selectedItems()[0].text()
        tag = serch.text()
        if not tag in notes[key]['tegs']:
            notes[key]['tegs'].append(tag)
            viewl2.addItem(tag)
            serch.clear()
            with open("saves.json", "w") as file:
                json.dump(notes,file)
    else:
        print('замітка не обрана')
def deltags():
    if viewl1.selectedItems():
        key = viewl1.selectedItems()[0].text()
        tag = viewl2.selectedItems()[0].text()
        notes[key]['tegs'].remove(tag)
        viewl2.clear()
        viewl2.addItems(notes[key]['tegs'])
        with open("saves.json", "w") as file:
                json.dump(notes,file)

def search_tags():
    tag = text.text()
    if Button32.text() == 'Шукати замітку по тегу':
        notes_f = {}
        for n in notes[n]['tegs']:
            if tag in notes[n]['tegs']:
                notes_f[n] = notes[n]
        Button32.setText('Скинути пошук')
        viewl1.clear()
        viewl2.clear()
        viewl1.addItems(notes_f)
    elif Button32.text() == 'Скинути пошук':
        viewl1.clear()
        viewl2.clear()
        serch.clear()
        viewl1.addItems(notes)
        Button32.setText('Шукати замітку по тегу')
    else:
        pass


Button31.clicked.connect(savetext)
Button21.clicked.connect(del_notes)
viewl1.itemClicked.connect(shownotes)
Button11.clicked.connect(addnote)
Button12.clicked.connect(addtags)
Button22.clicked.connect(deltags)
Button32.clicked.connect(search_tags)


window.show()

with open("saves.json",'r') as file:
    notes = json.load(file)

viewl1.addItems(notes)
app.exec_()