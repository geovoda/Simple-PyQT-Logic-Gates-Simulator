from Widgets.LogicGates.Gates.LogicGate import LogicGate
from Widgets.LogicGates.Gates.Terminal import Terminal
from Widgets.LogicGates.GatesDesign.AND import GATE as AND

class AndLogicGate(LogicGate):
    def __init__(self, x, y, parent, scale):
        WIDTH = 250
        HEIGHT = 200
        super(AndLogicGate, self).__init__(x, y, WIDTH, HEIGHT, scale, parent)
        self.type = "AND"
        self.terminals = [
            Terminal("INPUT", 0, 40 - 5, self),
            Terminal("INPUT", 0, 160 - 5, self),
            Terminal("OUTPUT", 230, 100 - 5, self),
        ]

        self.show()

    def paintGate(self):
        for e in AND["elements"]:
            if e["type"] == "arc":
                self.painter.drawArc(e["x"], e["y"], e["height"], e["width"], e["start"], e["size"])
            elif e["type"] == "line":
                self.painter.drawLine(e["x1"], e["y1"], e["x2"], e["y2"])
