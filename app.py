import csv

class Datos(): #División de clases
    def __init__(self, data):
        self.data = data
    
    def leerdatos(self, archivo):
        with open(archivo, 'r') as csvfile:
            next(csvfile)
            data_votos = csv.reader(csvfile)
            for fila in data_votos: 
                self.data.append(fila)
    

class CalculaGanador:

    def isValidDNI(self,dni): #División de métodos
        return (len(dni) == 8 and dni.isdigit())

    def calcularganador(self, data):
        votosxcandidato = {}
        total_votos_validos = 0
        for fila in data:
            region, provincia, distrito, dni, candidato, es_valido = fila #Renombrar variables
            if self.isValidDNI(dni) and es_valido == '1': #Simplificación de condicionales
                total_votos_validos += 1
                if candidato not in votosxcandidato:
                    votosxcandidato[candidato] = 0
                votosxcandidato[candidato] += 1

        porcentaje_ganador = 0.5 * total_votos_validos
        ganador = None
        segunda_vuelta = {}
        empate = []
        for candidato, votos in votosxcandidato.items():
            if votos > porcentaje_ganador:
                ganador = candidato
            if votos == porcentaje_ganador:
                empate.append(candidato)
            segunda_vuelta[candidato] = votos

        if ganador:
            return [ganador]
        elif len(empate) > 0:
            return [empate[0]]
        else:
            candidatos_ord_votos = dict(sorted(segunda_vuelta.items(), key=lambda x:x[1], reverse=True))
            return [candidato for candidato in list(candidatos_ord_votos)[:2]]