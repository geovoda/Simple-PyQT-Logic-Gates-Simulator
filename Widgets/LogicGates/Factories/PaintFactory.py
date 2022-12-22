
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
            from Widgets.LogicGates.GatesDesign.OR import GATE as OR
            self.gatesDesign[type] = OR

        elif type == "XOR":
            from Widgets.LogicGates.GatesDesign.XOR import GATE as XOR
            self.gatesDesign[type] = XOR

        elif type == "NAND":
            from Widgets.LogicGates.GatesDesign.NAND import GATE as NAND
            self.gatesDesign[type] = NAND

        elif type == "NOR":
            from Widgets.LogicGates.GatesDesign.NOR import GATE as NOR
            self.gatesDesign[type] = NOR

        elif type == "XNOR":
            from Widgets.LogicGates.GatesDesign.XNOR import GATE as XNOR
            self.gatesDesign[type] = XNOR

        elif type == "INPUT_ICON":
            from Widgets.LogicGates.GatesDesign.INPUT_ICON import GATE as INPUT_ICON
            self.gatesDesign[type] = INPUT_ICON

        elif type == "OUTPUT_ICON":
            from Widgets.LogicGates.GatesDesign.OUTPUT_ICON import GATE as OUTPUT_ICON
            self.gatesDesign[type] = OUTPUT_ICON

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