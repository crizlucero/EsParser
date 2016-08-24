from mosyn.util import AbstractMorphology

class DescripcionPalabra:

    categoria = 0
    numero = 0
    tipo = 0
    genero = 0

    def __init__(self, categoria, numero, tipo, genero):
        self.categoria = categoria
        self.numero = numero
        self.tipo = tipo
        self.genero = genero

    def getCategoria(self):
        if self.categoria == AbstractMorphology.CAT_ARTICLE:
            return "article"
        elif self.categoria == AbstractMorphology.CAT_DETERMINANT:
            return "determinant"
        elif self.categoria == AbstractMorphology.CAT_ABBREVIATION:
            return "abbreviation"
        elif self.categoria == AbstractMorphology.CAT_ADJECTIVE:
            return "adjective"
        elif self.categoria == AbstractMorphology.CAT_ADVERB:
            return "adverb"
        elif self.categoria == AbstractMorphology.CAT_CONJUNCTION:
            return "conjunction"
        elif self.categoria == AbstractMorphology.CAT_INTERJECTION:
            return "interjection"
        elif self.categoria == AbstractMorphology.CAT_NAME:
            return "name"
        elif self.categoria == AbstractMorphology.CAT_NUMERAL:
            return "numeral"
        elif self.categoria == AbstractMorphology.CAT_ADPOSITION: # Preposition
            return "adposition/preposition"
        elif self.categoria == AbstractMorphology.CAT_PRONOUN:
            return "pronoun"
        elif self.categoria == AbstractMorphology.CAT_PUNCTUATION:
            return "punctuation"
        elif self.categoria == AbstractMorphology.CAT_VERB:
            return "verb"
        else:
            return "unknown"

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