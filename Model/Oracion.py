from uuid import uuid4
from Tokens import Tokens
from Arbol import Arbol
from json import dumps


class Oracion:
    def __init__(self):
        self.oracionID = uuid4()
        self.oracion = None
        self.tokens = Tokens()
        self.arbol = []

    @property
    def _oracion(self):
        return self.oracion

    @_oracion.setter
    def _oracion(self, oracion):
        self.oracion = oracion

    @property
    def _tokens(self):
        return self.tokens

    @_tokens.setter
    def _tokens(self, tokens):
        self.tokens = tokens

    @property
    def _arbol(self):
        return self.arbol

    @_arbol.setter
    def _arbol(self, arbol):
        self.arbol = arbol

    def toJSON(self):
        return dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)