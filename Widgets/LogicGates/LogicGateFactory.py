from Widgets.LogicGates.LogicGate import LogicGate
from Widgets.LogicGates.UI.AND import GATE


class LogicGateFactory:
    def __init__(self):
        pass

    def paint(self, painter):
        for e in GATE["elements"]:
            if e["type"] == "arc":
                painter.drawArc(e["x"], e["y"], e["height"], e["width"], e["start"], e["size"])
            elif e["type"] == "line":
                painter.drawLine(e["x1"], e["y1"], e["x2"], e["y2"])

        # painter.drawArc(0, 2, 196, 196, -90 * 16, 180 * 16)
        # painter.drawLine(100, 2, 50, 2)
        # painter.drawLine(50, 198, 100, 198)
        # painter.drawLine(50, 0, 50, 200)
        # painter.drawLine(0, 40, 50, 40)
        # painter.drawLine(0, 160, 50, 160)
        # painter.drawLine(200, 100, 240, 100)