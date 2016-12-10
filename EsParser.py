# -*- coding: iso-8859-15 -*-
from copy import deepcopy

#Local imports
import mosyn
from Model.DescripcionPalabra import DescripcionPalabra
from Model.Oracion import Oracion
from Model.Arbol import Arbol
from Model.Union import Union
from Model.Tags import Tags
from Model.Db import DB

#Global Vars
frase = Oracion()


def main():
    dictionary = mosyn.MorphologicalDictionary("C:\Users\ChristianJavier\Documents\mosynapi-master\mosyn\dict\spanish_dict.csv")
    dictionary.load()
    manager = mosyn.AnalysisManager(dictionary)

    processed_data = manager.parse_string_to_eagles(u"el niño que me saludó de allá")

    oracion = []
    aux = []
    palabras = []

    for labels in processed_data:
        for label in labels:
            palabras.append(DescripcionPalabra(label.get_lema(), label.get_category(), label.get_number(),
                                               label.get_type(), label.get_gender()))
            tag = Tags()
            tag.DescripcionPalabra = DescripcionPalabra(label.get_lema(), label.get_category(), label.get_number(),
                                               label.get_type(), label.get_gender())
            tag.Eagle = label.get_eagles_label()
            frase.tokens.tags.append(tag)

    l = 0
    while l < len(palabras):
        palabras1 = []
        if l != (len(palabras) - 1) and palabras[l].lema == palabras[l + 1].lema:
            palabras1.append(palabras[l + 1])
            l += 1
        palabras1.append(palabras[l])
        oracion.append(deepcopy(palabras1))
        l += 1
    i = 0
    aux1 = ''

    while i <= len(oracion) - 1:
        arbol = Arbol()
        arbol.nivel = i
        for j in xrange(0, len(oracion[i])):
            aux1 = ''
            union = Union()
            if oracion[i][j].getCategoria() == 'nombre' \
                    or oracion[i][j].getCategoria() == 'pronombre':

                for k in xrange(0, len(oracion[i + 1])):
                    if oracion[i + 1][k].getCategoria() == 'nombre':
                        union.der = oracion[i + 1][k].getCategoria()
                        i += 1
                        break
                union.izq = oracion[i][j].getCategoria()
                union.generan = 'SN'
                arbol.union.append(union)
                aux1 = 'SN'
            elif oracion[i][j].getCategoria() == 'determinante' \
                    or oracion[i][j].getCategoria() == 'conjuncion':
                for k in xrange(0, len(oracion[i + 1])):
                    if oracion[i + 1][k].getCategoria() == 'nombre' \
                            or oracion[i + 1][k].getCategoria() == 'pronombre' \
                            or oracion[i + 1][k].getCategoria() == 'adjetivo':
                        union.der = oracion[i + 1][k].getCategoria()
                        union.izq = oracion[i][j].getCategoria()
                        union.generan = 'SD'
                        arbol.union.append(union)
                        aux1 = 'SD'
                        i += 1
                        break
            elif oracion[i][j].getCategoria() == 'verbo':
                union.izq = oracion[i][j].getCategoria()
                union.generan = 'V'
                arbol.union.append(union)
                aux1 = 'V'
            elif oracion[i][j].getCategoria() == 'adjetivo':
                union.izq = oracion[i][j].getCategoria()
                union.generan = 'SD'
                arbol.union.append(union)
                aux1 = 'SD'
            elif oracion[i][j].getCategoria() == 'adverbio':
                for k in xrange(0, len(oracion[i + 1])):
                    if oracion[i + 1][k].getCategoria() == 'adjetivo':
                        union.der = oracion[i + 1][k].getCategoria()
                        union.izq = oracion[i][j].getCategoria()
                        union.generan = 'SD'
                        frase.arbol.union.append(union)
                        aux1 = 'SD'
                        i += 1
            elif oracion[i][j].getCategoria() == 'preposicion':
                for k in xrange(0, len(oracion[i + 1])):
                    if oracion[i + 1][k].getCategoria() == 'nombre' \
                            or oracion[i + 1][k].getCategoria() == 'pronombre' \
                            or oracion[i + 1][k].getCategoria() == 'adjetivo' \
                            or oracion[i + 1][k].getCategoria() == 'adverbio':
                        union.der = oracion[i + 1][k].getCategoria()
                        union.izq = oracion[i][j].getCategoria()
                        union.generan = 'SD'
                        arbol.union.append(union)
                        aux1 = 'P'
                        i += 1
                        break
            else:
                aux1 = ''
            i += 1
            if aux1 != '':
                break
        frase.arbol.append(arbol)

        if aux1 != '':
            aux.append(aux1)
        else:
            return False

    return VerificarOracion(aux)


def VerificarOracion(oracion):
    while len(oracion) != 1:
        i = 0
        aux1 = []
        if len(oracion) % 2 != 0:
            oracion.append("")
        while i < len(oracion) - 1:
            aux = ""
            if (oracion[i] == "SN" and oracion[i + 1] == "SD") \
                    or (oracion[i] == "SD" and oracion[i + 1] == "SN"):
                aux = "SD"
                i += 1
            elif (oracion[i] == "SN" and oracion[i + 1] == "SN") \
                    or oracion[i] == "SN":
                aux = "SN"
            elif (oracion[i] == "SD" and oracion[i + 1] == "V") \
                    or (oracion[i] == "V") \
                    or (oracion[i] == "ST"):
                aux = "ST"
                i += 1
            elif oracion[i] == 'C' and oracion[i + 1] == 'ST':
                aux = "SC"
            elif oracion[i] == "SD" and oracion[i + 1] == "SC":
                aux = "SD"
            elif oracion[i] == "SD" and oracion[i + 1] == "ST":
                aux = "O"
            if aux != "":
                aux1.append(aux)
            i += 1
        oracion = deepcopy(aux1)
    return oracion


def VerificaTiempo(oracion):
    return False

if __name__ == '__main__':
    x = main()
    db = DB()
    db.saveData(frase.toJSON())
    print frase.toJSON()