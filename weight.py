'''Contains the Weight class for storing weights'''


class Weight:
    '''
    Used to store weights
    can convert from lbs to kg
    '''
    LB_TO_KG = 0.45359237

    def __init__(
            self,
            *,
            lbs: float | None = None,
            kgs: float | None = None,
        ):
        '''
        Initializes the class instance
        All arguments are keyword-only
        if no arguments are passed weight is assumed to be 0
        '''
        if lbs is not None and kgs is not None:
            raise ValueError('Given both pounds and kilos to Weight constructor, ambiguous')
        elif lbs is None and kgs is None:
            self.lbs = 0
        elif kgs is None:
            self.lbs = lbs
        else:
            self.kgs = kgs

    @property
    def kgs(self) -> float:
        '''
        Weight in kilograms
        converted from stored lbs
        '''
        return self.lbs * self.LB_TO_KG

    @kgs.setter
    def kgs(self, kgs: float):
        self.lbs = kgs / self.LB_TO_KG

