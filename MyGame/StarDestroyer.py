from CapitalShip import CapitalShip


class StarDestroyer(CapitalShip):
    def __init__(self):
        CapitalShip.__init__(self,
                             name='StarDestroyer',
                             maximum_speed=3,
                             length=70,
                             capacity=8,
                             health_point=55,
                             power=30,
                             )
