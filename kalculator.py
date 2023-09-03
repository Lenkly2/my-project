from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QGridLayout,QLineEdit
from random import randint


app = QApplication([])
result = QLineEdit()
window = QWidget()
window.setWindowTitle('Калькулятор')
window.resize(500,500)
lay = QGridLayout()

def click():
    button = window.sender()
    label = button.text()
    if label == '=':
        try:
            r = str(eval(result.text()))
            result.setText(r)
        except:
            result.setText("error")
    else:
        result.setText(result.text() + label)
    if label == 'c':
        result.setText('')     

buttons = ['1','2','3','4','5','6','7','8','9','0','/','*','-','+','=','.','c']
col = 0
rov = 1
for n in buttons:
    button = QPushButton(n)
    button.clicked.connect(click)
    lay.addWidget(button,rov,col)
    col += 1
    if col > 3:
        col = 0
        rov +=1




lay.addWidget(result,0,0,1,4)
window.setLayout(lay)


window.show()
app.exec_()
