from CapitalShip import CapitalShip


class Corvette(CapitalShip):
    def __init__(self):
        CapitalShip.__init__(self,
                             name='Corvette',
                             maximum_speed=7,
                             length=20,
                             capacity=0,
                             health_point=15,
                             power=8,
                             )
