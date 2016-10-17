from DescripcionPalabra import DescripcionPalabra


class Tags:
    def __init__(self):
        self.Eagle = None
        self.DescripcionPalabra = DescripcionPalabra()

    @property
    def _eagle(self):
        return self.Eagle

    @_eagle.setter
    def _eagle(self, eagle):
        self.Eagle = eagle

    @property
    def _descripcionPalabra(self):
        return self.DescripcionPalabra

    @_descripcionPalabra.setter
    def _descripcionPalabra(self, dp):
        self.DescripcionPalabra = dp
