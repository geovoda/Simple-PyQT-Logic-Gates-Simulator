from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5 import QtGui
from PyQt5 import QtCore
import math

from Widgets.Buttons.GateIcon import GateIcon
from Widgets.LogicGates.Factories.PaintFactory import PaintFactory


class GateButton(QWidget):
    def __init__(self, type, parent):
        super().__init__()
        self.type = type
        self.setFixedHeight(60)
        self.setFixedWidth(60)

        # name = QLabel()
        # name.setText(type)
        # name.setParent(self)
        # name.setFixedHeight(20)

        self.paintFactory = PaintFactory()

        icon = GateIcon(type, self.paintFactory)
        icon.setAlignment(Qt.AlignHCenter)
        icon.setFixedHeight(40)

        vbox = QVBoxLayout()
        vbox.setAlignment(Qt.AlignHCenter)
        #vbox.addWidget(name)
        vbox.addWidget(icon)
        vbox.setSpacing(0)

        self.setLayout(vbox)
        self.setParent(parent)

        self.brush = QColor(41, 98, 255)
        self.installEventFilter(self)

        self.callback = None

    def mouseReleaseEvent(self, e: QtGui.QMouseEvent) -> None:
        if e.button() == QtCore.Qt.LeftButton and self.callback is not None:
            self.callback()

    def connect(self, callback):
        self.callback = callback
    def eventFilter(self, object, event):
        if event.type() == QEvent.Enter:
            self.brush = QColor(35, 73, 177)
            self.repaint()
            return True
        elif event.type() == QEvent.Leave:
            self.brush = QColor(41, 98, 255)
            self.repaint()
        return False

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        self.painter = QPainter(self)

        self.painter.begin(self)
        self.painter.setRenderHint(QPainter.Antialiasing)

        col = QColor(255, 255, 255)
        self.painter.setPen(col)

        self.painter.setBrush(self.brush)
        self.painter.drawEllipse(0, 0, 60, 60)

        self.painter.end()

    # def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
    #     super().mouseMoveEvent(event)
    #     if event.buttons() == QtCore.Qt.LeftButton and self.__mousePressPosition is not None:
    #         self.move(self.mapToParent(event.pos() - self.__mousePressPosition))
    #         self.parent().repaint()

