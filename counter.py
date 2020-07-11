#!/usr/bin/env python3
import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
import PyQt5.QtGui as qtg


# Clickable label
class QClickLabel(qtw.QLabel):
    clicked = qtc.pyqtSignal()

    def __init__(self, parent=None):
        qtw.QLabel.__init__(self, parent)

    def mouseDoubleClickEvent(self, ev):
        self.clicked.emit()


# LineEdit that returns focus info
class QFocusLineEdit(qtw.QLineEdit):
    focusOut = qtc.pyqtSignal()

    def __init__(self, parent=None):
        qtw.QLineEdit.__init__(self, parent)

    def focusOutEvent(self, ev):
        self.focusOut.emit()


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        # Setup the window
        self.setWindowTitle("Counter")
        self.setFixedSize(240, 120)
        self.setLayout(qtw.QVBoxLayout())

        # Initialize variables
        self.x = 0
        self.label = QClickLabel(str(self.x))
        self.edit = QFocusLineEdit(str(self.x))
        add = qtw.QPushButton("+", clicked=self.add)
        sub = qtw.QPushButton("-", clicked=self.sub)
        reset = qtw.QPushButton("0", clicked=self.reset)
        grid = qtw.QWidget()

        # Configure elements
        self.label.setAlignment(qtc.Qt.AlignCenter)
        self.label.setFont(qtg.QFont('sans-serif', 24))
        self.label.clicked.connect(self.editLabel)

        self.edit.setAlignment(qtc.Qt.AlignCenter)
        self.edit.setFont(qtg.QFont('sans-serif', 24))
        self.edit.returnPressed.connect(self.editLabelDone)
        self.edit.focusOut.connect(self.editLabelDone)
        self.edit.setValidator(qtg.QIntValidator())
        self.edit.hide()

        grid.setLayout(qtw.QGridLayout())

        # Keyboard shortcuts
        add.setToolTip("Add (A)")
        add.setShortcut(qtc.Qt.Key_A)
        sub.setToolTip("Substract (S)")
        sub.setShortcut(qtc.Qt.Key_S)
        reset.setToolTip("Reset (D)")
        reset.setShortcut(qtc.Qt.Key_D)

        # Pack elements
        grid.layout().addWidget(add, 0, 0, 1, 2)
        grid.layout().addWidget(sub, 0, 2, 1, 2)
        grid.layout().addWidget(reset, 0, 4)

        self.layout().addWidget(self.label, alignment=qtc.Qt.AlignCenter)
        self.layout().addWidget(self.edit, alignment=qtc.Qt.AlignCenter)
        self.layout().addWidget(grid, alignment=qtc.Qt.AlignBottom)

        # Show window
        self.show()

    def update(self):
        self.label.setText(str(self.x))
        self.edit.setText(str(self.x))

    def add(self):
        self.x += 1
        self.update()

    def sub(self):
        self.x -= 1
        self.update()

    def reset(self):
        self.x = 0
        self.update()

    def editLabel(self):
        self.label.hide()
        self.edit.show()
        self.edit.setFocus()

    def editLabelDone(self):
        self.x = int(self.edit.text())
        self.update()
        self.label.show()
        self.edit.hide()


app = qtw.QApplication([])
mw = MainWindow()
app.exec_()
