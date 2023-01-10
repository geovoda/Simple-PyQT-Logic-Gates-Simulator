from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from Widgets.Buttons.GateButton import GateButton


class TopBar(QWidget):
    def __init__(self, parentWindow):
        super(TopBar, self).__init__()
        self.parentWindow = parentWindow
        horizontalLayout = QHBoxLayout()
        horizontalLayout.setAlignment(Qt.AlignLeft)

        undoButton = QPushButton(self)
        undoButton.setText("Undo")  # text
        undoButton.setShortcut('Ctrl+Z')  # shortcut key
        undoButton.clicked.connect(self.parentWindow.logicGateContainer.undo)
        undoButton.setToolTip("Anuleaza ultima actiune ")  # Tool tip
        undoButton.move(10, 1)
        horizontalLayout.addWidget(undoButton)

        redoButton = QPushButton(self)
        redoButton.setText("Redo")  # text
        redoButton.setShortcut('Ctrl+Z')  # shortcut key
        redoButton.clicked.connect(self.parentWindow.logicGateContainer.redo)
        redoButton.setToolTip("Reface ultima actiune")  # Tool tip
        redoButton.move(110, 1)
        horizontalLayout.addWidget(redoButton)

        self.setLayout(horizontalLayout)

