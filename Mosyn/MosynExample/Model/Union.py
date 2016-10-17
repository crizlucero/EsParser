class Union:
    def __init__(self):
        self.izq = None
        self.der = None
        self.generan = None

    @property
    def _izq(self):
        return self.izq

    @_izq.setter
    def _izq(self, izq):
        self.izq = izq

    @property
    def _der(self):
        return self.der

    @_der.setter
    def _der(self, der):
        self.der = der

    @property
    def _generan(self):
        return self.generan

    @_generan.setter
    def _generan(self, generan):
        self.generan = generan
