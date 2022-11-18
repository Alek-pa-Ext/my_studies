from CapitalShip import CapitalShip


class Frigate(CapitalShip):
    def __init__(self):
        CapitalShip.__init__(self,
                             name='Frigate',
                             maximum_speed=6,
                             length=30,
                             capacity=2,
                             health_point=25,
                             power=12,
                             )
