from Widgets.LogicGates import AndLogicGate, OrLogicGate
from Widgets.LogicGates.LogicGate import LogicGate
from Widgets.LogicGates.UI.AND import GATE as AND
from Widgets.LogicGates.UI.OR import GATE as OR


class LogicGateFactory:
    def __init__(self):
        pass

    def create(self, gateType):
        types = {
            "AND": AndLogicGate,
            "OR": OrLogicGate
        }
        return types[gateType]
