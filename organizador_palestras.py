from organizador_palestras import Palestra, agendar_sessao

def testar_agendamento_basico():
    palestras = [
        Palestra("Palestra A", 60),
        Palestra("Palestra B", 60),
        Palestra("Palestra C", 60),
        Palestra("Palestra D", 45),
        Palestra("Palestra E", 30),
    ]
    sessao, restantes = agendar_sessao(palestras, 180)
    tempo_total = sum(p.duracao for p in sessao)
    assert tempo_total <= 180
    assert all(isinstance(p, Palestra) for p in sessao)
    assert len(sessao) > 0
