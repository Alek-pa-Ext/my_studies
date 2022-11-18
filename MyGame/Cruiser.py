from CapitalShip import CapitalShip


class Cruiser(CapitalShip):
    def __init__(self):
        CapitalShip.__init__(self,
                             name='Cruiser',
                             maximum_speed=5,
                             length=50,
                             capacity=4,
                             health_point=35,
                             power=18,
                             )
