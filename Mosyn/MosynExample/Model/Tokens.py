class Tokens:
    def __init__(self):
        self.palabra = None
        self.tags = None

    @property
    def _palabra(self):
        return self.palabra

    @_palabra.setter
    def _palabra(self, palabra):
        self.palabra = palabra

    @property
    def _tags(self):
        return self.tags

    @_tags.setter
    def _tags(self, tags):
        self.tags = tags
