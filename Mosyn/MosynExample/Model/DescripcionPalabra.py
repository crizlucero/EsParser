from mosyn.util import AbstractMorphology

class DescripcionPalabra:

    lema = ""
    categoria = 0
    numero = 0
    tipo = 0
    genero = 0

    def __init__(self, lema, categoria, numero, tipo, genero):
        self.lema = lema
        self.categoria = categoria
        self.numero = numero
        self.tipo = tipo
        self.genero = genero

    def getCategoria(self):
        if self.categoria == AbstractMorphology.CAT_ARTICLE:
            return "articulo"
        elif self.categoria == AbstractMorphology.CAT_DETERMINANT:
            return "determinante"
        elif self.categoria == AbstractMorphology.CAT_ABBREVIATION:
            return "abreviacion"
        elif self.categoria == AbstractMorphology.CAT_ADJECTIVE:
            return "adjetivo"
        elif self.categoria == AbstractMorphology.CAT_ADVERB:
            return "adverbio"
        elif self.categoria == AbstractMorphology.CAT_CONJUNCTION:
            return "conjuncion"
        elif self.categoria == AbstractMorphology.CAT_INTERJECTION:
            return "interjeccion"
        elif self.categoria == AbstractMorphology.CAT_NAME:
            return "nombre"
        elif self.categoria == AbstractMorphology.CAT_NUMERAL:
            return "numeral"
        elif self.categoria == AbstractMorphology.CAT_ADPOSITION: # Preposition
            return "preposicion"
        elif self.categoria == AbstractMorphology.CAT_PRONOUN:
            return "pronombre"
        elif self.categoria == AbstractMorphology.CAT_PUNCTUATION:
            return "puntuacion"
        elif self.categoria == AbstractMorphology.CAT_VERB:
            return "verbo"
        else:
            return "desconocido"

    def getNumero(self):
        if self.numero == AbstractMorphology.NUMBER_SINGULAR:
            print "singular",
        elif self.numero == AbstractMorphology.NUMBER_PLURAL:
            print "plural",
        elif self.numero == AbstractMorphology.NUMBER_INVARIABLE:
            print "invariable",
        elif self.numero == AbstractMorphology.NUMBER_UNKNOWN:
            print "undefined number",
        else:
            print str(self.numero),

    def getTipo(self):
        if self.tipo == AbstractMorphology.TYPE_GENERAL:
            print ", it is of general type",
        elif self.tipo == AbstractMorphology.TYPE_CALIFICATIVE:
            print ", it is of calificative type",

    def getGenero(self):
        if self.genero == AbstractMorphology.GENDER_MALE:
            print "male", self.categoria,
        elif self.genero == AbstractMorphology.GENDER_FEMALE:
            print "female", self.categoria,
        else:
            print self.categoria, "without gender",