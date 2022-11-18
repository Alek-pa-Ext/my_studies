from CapitalShip import CapitalShip


class Dreadnaughts(CapitalShip):
    def __init__(self):
        CapitalShip.__init__(self,
                             name='Dreadnaughts',
                             maximum_speed=1,
                             length=90,
                             capacity=20,
                             health_point=75,
                             power=50,
                             )
