from Widgets.LogicGates.Gates import OrLogicGate, AndLogicGate


class LogicGateFactory:
    def __init__(self):
        pass

    def create(self, gateType):
        types = {
            "AND": AndLogicGate,
            "OR": OrLogicGate
        }
        return types[gateType]
