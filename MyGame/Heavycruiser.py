from CapitalShip import CapitalShip


class Heavycruiser(CapitalShip):
    def __init__(self):
        CapitalShip.__init__(self,
                             name='Heavycruiser',
                             maximum_speed=4,
                             length=60,
                             capacity=6,
                             health_point=45,
                             power=22,
                             )
