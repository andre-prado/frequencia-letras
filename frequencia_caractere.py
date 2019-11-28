from collections import Counter


def frequencia_caractere(texto, num_letras):
    """
    Retorna a frequência de caracteres dentro de um texto.
    primeiro parâmetro: texto.txt
    segundo parâmetro: número de caracteres que deseja ver.
    """
    abre_texto = open(texto, 'r')
    aparicoes = Counter(abre_texto.read().lower())
    total_caracteres = sum(aparicoes.values())
    proporcoes = [(letra, frequencia / total_caracteres) for letra,
                  frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(num_letras)
    print(mais_comuns)
    for caractere, proporcao in mais_comuns:
        print('{} > {:.2f} %'.format(caractere, proporcao * 100))
