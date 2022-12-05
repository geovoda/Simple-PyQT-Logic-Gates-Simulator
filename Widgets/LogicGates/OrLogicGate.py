from Widgets.LogicGates.LogicGate import LogicGate
from Widgets.LogicGates.LogicGateFactoryOld import LogicGateFactoryOld
from Widgets.LogicGates.Terminal import Terminal
from Widgets.LogicGates.UI.OR import GATE as OR


class OrLogicGate(LogicGate):
    def __init__(self, x, y, parent, scale):
        WIDTH = 250
        HEIGHT = 200
        super(OrLogicGate, self).__init__(x, y, WIDTH, HEIGHT, scale, parent)
        self.type = "OR"
        self.terminals = [
            Terminal("INPUT", 0, 40 - 5, self),
            Terminal("INPUT", 0, 160 - 5, self),
            Terminal("OUTPUT", 230, 100 - 5, self),
        ]

        self.show()

    def paintGate(self):
        for e in OR["elements"]:
            if e["type"] == "arc":
                self.painter.drawArc(e["x"], e["y"], e["height"], e["width"], e["start"], e["size"])
            elif e["type"] == "line":
                self.painter.drawLine(e["x1"], e["y1"], e["x2"], e["y2"])
            elif e["type"] == "arcR":
                self.painter.drawArc(e["rectangle"], e["start"], e["angle"])
