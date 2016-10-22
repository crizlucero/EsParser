from Union import Union


class Arbol:
    def __init__(self):
        self.nivel = 0
        self.union = []

    @property
    def _nivel(self):
        return self.nivel

    @_nivel.setter
    def _nivel(self, nivel):
        self.nivel = nivel

    @property
    def _union(self):
        return self.union

    @_union.setter
    def _union(self, union):
        self.union = union