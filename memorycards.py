
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

app = QApplication([])


#vidjet
main = QWidget()
main.resize(500,500)
layH = QHBoxLayout()
layV = QVBoxLayout()
button1 = QPushButton("меню")
button2 = QPushButton("відповісти")
button3 = QPushButton("відпочити")
Box = QSpinBox()
label = QLabel("?")
Box.setValue(30)

layH.addWidget(button1)
layH.addStretch(1)
layH.addWidget(button3)
layH.addWidget(Box)

layV.addLayout(layH)
layV.addWidget(label,alignment=Qt.AlignCenter)
layV.addWidget(button2,alignment=Qt.AlignCenter,stretch=2)

main.setLayout(layV)


main.setWindowTitle("memory card")
main.show()
app.exec_()
