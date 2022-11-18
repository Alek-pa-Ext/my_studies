from CapitalShip import CapitalShip


class Battlecruiser(CapitalShip):
    def __init__(self):
        CapitalShip.__init__(self,
                             name='Battlecruiser',
                             maximum_speed=2,
                             length=80,
                             capacity=10,
                             health_point=65,
                             power=40,
                             )
