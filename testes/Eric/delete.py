import numpy as np


inteiro: np.int32 = np.int32(42)


caminho: str = "/dados/inteiro"


def salvar_inteiro_no_caminho(valor: np.int32, path: str):
    with open(path, 'wb') as f:
        np.save(f, valor)

def carregar_inteiro_do_caminho(path: str) -> np.int32:
    with open(path, 'rb') as f:
        return np.load(f)


salvar_inteiro_no_caminho(inteiro, caminho)
inteiro_carregado = carregar_inteiro_do_caminho(caminho)
print(f"Inteiro carregado: {inteiro_carregado}")
