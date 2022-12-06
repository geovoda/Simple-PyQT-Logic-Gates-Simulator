
class PaintFactory:
    def __init__(self):
        self.gatesDesign = {}

    def paintGate(self, type, painter):
        if type in self.gatesDesign:
            self.paint(type, painter)
            return

        if type == "AND":
            from Widgets.LogicGates.GatesDesign.AND import GATE as AND
            self.gatesDesign[type] = AND

        elif type == "OR":
            from Widgets.LogicGates.GatesDesign.AND import GATE as OR
            self.gatesDesign[type] = OR

        else:
            return

        self.paint(type, painter)

    def paint(self, type, painter):
        for e in self.gatesDesign[type]["elements"]:
            if e["type"] == "arc":
                painter.drawArc(e["x"], e["y"], e["height"], e["width"], e["start"], e["size"])
            elif e["type"] == "arcR":
                painter.drawArc(e["rectangle"], e["start"], e["angle"])
            elif e["type"] == "line":
                painter.drawLine(e["x1"], e["y1"], e["x2"], e["y2"])
            elif e["type"] == "circle":
                painter.drawEllipse(e["x"], e["y"], e["height"], e["width"])