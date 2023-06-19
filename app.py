import csv

class CalculaGanador:

    def leerdatos(self, archivo):
        data = []
        with open(archivo, 'r') as csvfile:
            next(csvfile)
            data_votos = csv.reader(csvfile)
            for fila in data_votos:
                data.append(fila)
        return data

    def isValidDNI(self, dni):# 1) Extraccion de métodos
        return len(dni) == 8 and dni.isdigit()

    def calcular_ganador(self, data):
        votosxcandidato = {}
        total_votos_validos = 0

        for fila in data:
            region, provincia, distrito, dni, candidato, es_valido = fila # 2) Renombrar variables
            if self.isValidDNI(dni) and es_valido == '1':  # 3) Simplificación de condicionales
                total_votos_validos += 1

                votosxcandidato[candidato] = votosxcandidato.get(candidato, 0) + 1 #Simplificación de condicionales, uso de dict.get() # 4) Eliminacion de codigo duplicado

        return self.obtener_resultado(total_votos_validos, votosxcandidato)
    # 5)División de metodos
    def obtener_resultado(self, total_votos_validos, votosxcandidato):
        porcentaje_ganador = 0.5 * total_votos_validos
        ganador = None
        segunda_vuelta = []
        no_ganador = []


        for candidato, votos in votosxcandidato.items():
            if votos > porcentaje_ganador:
                ganador = candidato
            elif votos == porcentaje_ganador:
                segunda_vuelta.append(candidato)
            else:                   #Simplificación de condicionales: uso de else en vez de elif que cubría casos contrarios.
                no_ganador.append(candidato)

        return self.obtener_resultado_final(ganador, segunda_vuelta, no_ganador, votosxcandidato)

    def obtener_resultado_final(self, ganador, segunda_vuelta, no_ganador, votosxcandidato):
        if ganador:
            return [ganador]
        elif len(segunda_vuelta) >= 2:
            return segunda_vuelta[:1]
        elif len(segunda_vuelta) == 1:
            return segunda_vuelta + [list(votosxcandidato.keys())[0]]
        else:
            no_ganador_ordenado = sorted(no_ganador, key=lambda candidato: votosxcandidato[candidato], reverse=True)
            return no_ganador_ordenado[:2]


c = CalculaGanador()
datatest = [
    ['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '0'],
    ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
    ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '0'],
    ['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '0'],
    ['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1'],
    ['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '0'],
]
print(c.calcular_ganador(datatest))

c = CalculaGanador()
datos = c.leerdatos("0204.csv")
print(c.calcularganador(datos))