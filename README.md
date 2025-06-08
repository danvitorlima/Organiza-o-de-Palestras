# Organizador de Palestras de Conferência

Organiza palestras automaticamente, separa em horários da manhã, tarde e evento de networking. Feito em Python.

---

##  Arquivos

- `main.py` → Código principal
- `proposals.txt` → Lista de palestras
- `organizador_palestras.py`

---

## Como usar 

### 1. Verificar se o Python está instalado

 Abrir **VS Code**

 Abrir a pasta do projeto  
 Abrir o terminal no VS Code: `Terminal > Novo Terminal`

Digite no terminal:

```bash
python --version
```

Se aparecer algo como `Python 3.x.x` → OK

❌ Se aparecer erro:
- Ir no site: https://www.python.org/downloads
- Baixar e instalar
- **Marcar a opção** `Add Python to PATH`
- Depois de instalar, **fechar e abrir de novo o VS Code**

---

### 2. Rodar o programa

No terminal (com `main.py` e `proposals.txt` na mesma pasta):

```bash
python main.py
```

O terminal vai mostrar as trilhas da conferência (Track A, Track B...)

---

## Teste (opcional)

1. Instalar pytest:

```bash
pip install pytest
```

2. Rodar teste:

```bash
pytest organizador_palestras.py
```
