import re
from datetime import timedelta, datetime

INICIO_MANHA = datetime.strptime("09:00", "%H:%M")
DURACAO_MANHA = 180  # minutos
INICIO_TARDE = datetime.strptime("13:00", "%H:%M")
MIN_TARDE = 180  # até 16h
MAX_TARDE = 240  # até 17h

class Palestra:
    def __init__(self, titulo, duracao):
        self.titulo = titulo
        self.duracao = 5 if duracao == "lightning" else int(duracao)

    def __repr__(self):
        return f"{self.titulo} ({self.duracao}min)"

def ler_palestras(arquivo):
    palestras = []
    with open(arquivo, encoding="utf-8") as f:
        for linha in f:
            match = re.match(r"(.+?)\s(\d+min|lightning)", linha.strip())
            if match:
                titulo, duracao_str = match.groups()
                duracao = duracao_str.replace("min", "")
                palestras.append(Palestra(titulo, duracao))
    return palestras

def agendar_sessao(palestras, duracao_max):
    usadas = [False] * len(palestras)
    sessao = []
    total = 0

    for i, palestra in enumerate(palestras):
        if not usadas[i] and total + palestra.duracao <= duracao_max:
            sessao.append(palestra)
            usadas[i] = True
            total += palestra.duracao
    restantes = [p for i, p in enumerate(palestras) if not usadas[i]]
    return sessao, restantes

def formatar_sessao(inicio, palestras):
    horario = inicio
    resultado = ""
    for palestra in palestras:
        resultado += f"{horario.strftime('%H:%M')} {palestra.titulo} {palestra.duracao}min\n"
        horario += timedelta(minutes=palestra.duracao)
    return resultado, horario

def criar_trilhas(palestras):
    trilhas = []
    restantes = palestras[:]

    while restantes:
        trilha = {}
        manha, restantes = agendar_sessao(restantes, DURACAO_MANHA)
        tarde, restantes = agendar_sessao(restantes, MAX_TARDE)
        trilha["manha"] = manha
        trilha["tarde"] = tarde
        trilhas.append(trilha)

    return trilhas

def imprimir_programacao(trilhas):
    for i, trilha in enumerate(trilhas, 1):
        print(f"Track {chr(64+i)}:")
        sessao_manha, _ = formatar_sessao(INICIO_MANHA, trilha["manha"])
        print(sessao_manha.strip())
        print("12:00 Almoço")
        sessao_tarde, fim = formatar_sessao(INICIO_TARDE, trilha["tarde"])
        print(sessao_tarde.strip())
        networking = max(fim, datetime.strptime("16:00", "%H:%M"))
        print(f"{networking.strftime('%H:%M')} Evento de Networking\n")

if __name__ == "__main__":
    palestras = ler_palestras("proposals.txt")
    trilhas = criar_trilhas(palestras)
    imprimir_programacao(trilhas)
