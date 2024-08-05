import os
import re

def analise_lexica(arquivo):
    with open(arquivo, 'r') as file:
        invalido = 0
        for linha in file:
            tokens = encontra_token_inválido(linha)
            for token, tipo in tokens:
                if tipo == 'invalido':
                    invalido = 1
                    print(f'o caractere "{token}" é inválido')
        if invalido == 0:
            file.seek(0)
            for linha in file:
                tokens = encontrar_tokens(linha)
                for token, tipo in tokens:
                    if tipo == None:
                        print(f'<{token}> ', end='')
                    else:
                        print(f'<{tipo},{token}> ', end='')

def encontrar_tokens(linha):
    tokens = []
    expressao_numero = r'\d+'
    expressao_palavra = r'[a-zA-ZÀ-ÖØ-öø-ÿ]+'
    expressao_simbolo = r'[()+\-*]'

    while linha:
        token = None
        if re.match(expressao_numero, linha):
            match = re.match(expressao_numero, linha)
            token = match.group(0)
            tipo = 'num'
        elif re.match(expressao_palavra, linha):
            match = re.match(expressao_palavra, linha)
            token = match.group(0)
            tipo = 'id'
        elif re.match(expressao_simbolo, linha):
            match = re.match(expressao_simbolo, linha)
            token = match.group(0)
            tipo = None
        if token:
            tokens.append((token, tipo))
            linha = linha[len(token):].lstrip()
        else:
            linha = linha[1:]

    return tokens

def encontra_token_inválido(linha):
    tokens = []
    expressao_invalido = r'[!@#$%^&\[\]{};:",.<>?\\]'

    while linha:
        tipo = None
        token = None
        if re.match(expressao_invalido, linha):
            match = re.match(expressao_invalido, linha)
            token = match.group(0)
            tipo = 'invalido'
        if token:
            tokens.append((token, tipo))
            linha = linha[len(token):].lstrip()
        else:
            linha = linha[1:]
    return tokens

# Obtenha o diretório do script atual
current_dir = os.path.dirname(os.path.abspath(__file__))
# Nome do arquivo de texto que você deseja analisar
nome_arquivo = os.path.join(current_dir, 'arquivo.txt')

# Chamada da função de análise léxica
analise_lexica(nome_arquivo)
