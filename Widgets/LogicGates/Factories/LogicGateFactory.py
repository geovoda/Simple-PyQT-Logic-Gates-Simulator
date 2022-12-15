from Widgets.LogicGates.Factories.PaintFactory import PaintFactory
from Widgets.LogicGates.Gates.AndLogicGate import AndLogicGate
from Widgets.LogicGates.Gates.InputStream import InputStream
from Widgets.LogicGates.Gates.NandLogicGate import NandLogicGate
from Widgets.LogicGates.Gates.NorLogicGate import NorLogicGate
from Widgets.LogicGates.Gates.OrLogicGate import OrLogicGate
from Widgets.LogicGates.Gates.XnorLogicGate import XnorLogicGate
from Widgets.LogicGates.Gates.XorLogicGate import XorLogicGate
from Widgets.LogicGates.Gates.OutputStream import OutputStream

class LogicGateFactory:
    def __init__(self):
        self.types = {
            "AND": AndLogicGate,
            "OR": OrLogicGate,
            "XOR": XorLogicGate,
            "NAND": NandLogicGate,
            "NOR": NorLogicGate,
            "XNOR": XnorLogicGate,
            "INPUT_STREAM": InputStream,
            "OUTPUT_STREAM": OutputStream

        }

        self.paintFactory = PaintFactory()

    def create(self, type, x, y, scale, parent):
        return self.types[type](x, y, parent, scale, self.paintFactory)
