# -*- coding: iso-8859-15 -*-
import mosyn
import copy
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


def main():
    dictionary = mosyn.MorphologicalDictionary("/home/christian/Documentos/mosynapi-master/mosyn/dict/spanish_dict.csv")
    dictionary.load()
    manager = mosyn.AnalysisManager(dictionary)

    processed_data = manager.parse_string_to_eagles(u"el niño que me saludó de allá")

    oracion = []
    aux = []
    palabras =[]
    for labels in processed_data:
        for label in labels:
            palabras.append(DescripcionPalabra(labels[0].get_lema(), label.get_category(), label.get_number(),
                                               label.get_type(), label.get_gender()))

    l = 0
    palabras1 = []
    while l < len(palabras):
        if l != (len(palabras)-1) and palabras[l].lema == palabras[l+1].lema:
            palabras1.append(palabras[l+1])
            l += 1
        palabras1.append(palabras[l])
        p = copy.deepcopy(palabras1)
        oracion.append(p)
        palabras1 = []
        l += 1
    i = 0
    aux1 = ''
    while i <= len(oracion)-1:
        for j in xrange(0, len(oracion[i])):
            aux1 = ''
            if oracion[i][j].getCategoria() == 'nombre' \
                    or oracion[i][j].getCategoria() == 'pronombre':
                for k in xrange(0, len(oracion[i+1])):
                    if oracion[i+1][k].getCategoria() == 'nombre':
                        i += 1
                        break
                aux1 = 'SN'
            elif oracion[i][j].getCategoria() == 'determinante' \
                    or oracion[i][j].getCategoria() == 'conjuncion':
                for k in xrange(0, len(oracion[i+1])):
                    if oracion[i+1][k].getCategoria() == 'nombre' \
                            or oracion[i+1][k].getCategoria() == 'pronombre' \
                            or oracion[i+1][k].getCategoria() == 'adjetivo':
                        aux1 = 'SD'
                        i += 1
                        break
            elif oracion[i][j].getCategoria() == 'verbo':
                aux1 = 'V'
            elif oracion[i][j].getCategoria() == 'adjetivo':
                aux1 = 'P'
            elif oracion[i][j].getCategoria() == 'adverbio':
                for k in xrange(0, len(oracion[i+1])):
                    if oracion[i+1][k].getCategoria() == 'adjetivo':
                        aux1 = 'P'
                        i += 1
            elif oracion[i][j].getCategoria() == 'preposicion':
                for k in xrange(0, len(oracion[i+1])):
                    if oracion[i+1][k].getCategoria() == 'nombre' \
                            or oracion[i+1][k].getCategoria() == 'pronombre' \
                            or oracion[i+1][k].getCategoria() == 'adjetivo' \
                            or oracion[i+1][k].getCategoria() == 'adverbio':
                        aux1 = 'P'
                        i += 1
                        break
            else:
                aux1 = ''
            i += 1
            if aux1 != '':
                break
        if aux1 != '':
            aux.append(aux1)
        else:
            return False

    return aux



if __name__ == '__main__':
    x = main()
    print x
