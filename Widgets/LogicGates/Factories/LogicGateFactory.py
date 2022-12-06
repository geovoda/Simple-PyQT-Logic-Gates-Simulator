from Widgets.LogicGates.Gates.AndLogicGate import AndLogicGate
from Widgets.LogicGates.Gates.OrLogicGate import OrLogicGate
from Widgets.LogicGates.Factories.PaintFactory import PaintFactory
class LogicGateFactory:
    def __init__(self):
        self.types = {
            "AND": AndLogicGate,
            "OR": OrLogicGate
        }

        self.paintFactory = PaintFactory()

    def create(self, type, x, y, scale, parent):
        return self.types[type](x, y, parent, scale, self.paintFactory)
