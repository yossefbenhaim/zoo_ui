
from zooo import zoo


class Mammals(zoo):
    def __init__(self,family,name_of_zoo):
        self.family= family
        super().__init__(name_of_zoo)
