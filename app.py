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
    
    def isValidDNI(self, dni):
        return len(dni) == 8 and dni.isdigit()

    def calcularganador(self, data):
        votosxcandidato = {}
        total_votos_validos = 0
        for fila in data:
            region, provincia, distrito, dni, candidato, es_valido = fila
            if self.isValidDNI(dni) and es_valido == '1':
                total_votos_validos += 1
                if candidato not in votosxcandidato:
                    votosxcandidato[candidato] = 0
                votosxcandidato[candidato] += 1

        porcentaje_ganador = 0.5 * total_votos_validos
        ganador = None
        segunda_vuelta = []
        no_ganador = []
        for candidato, votos in votosxcandidato.items():
            if votos > porcentaje_ganador:
                ganador = candidato
            elif votos == porcentaje_ganador:
                segunda_vuelta.append(candidato)
            elif votos < porcentaje_ganador:
                no_ganador.append(candidato)

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
print(c.calcularganador(datatest))