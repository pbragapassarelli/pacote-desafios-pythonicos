"""
14. mimic

Neste desafio você vai fazer um gerador de lero-lero.

É um programa que lê um arquivo, armazena a relação entre as palavras e
então gera um novo texto respeitando essas relações para imitar um
escritor de verdade.

Para isso você precisa:

A. Abrir o arquivo especificado via linha de comando.

B. Ler o conteúdo e separar as palavras obtendo uma lista de palavras.

C. Criar um dicionário de "imitação".

Nesse dicionário a chave será uma palavra e o valor será uma lista
contendo as palavras que aparecem no texto após a palavra usada na chave.

Por exemplo, suponha um arquivo com o conteúdo: A B C B A

O dicionário de imitação deve considerar que:
* a chave A contém uma lista com a palavra B
* a chave B contém uma lista com as palavras C e A
* a chave C contém uma lista com a palavra B

Além disso precisamos considerar que:
* a chave '' contém uma lista com a primeira palavra do arquivo
* a última palavra do arquivo contém uma lista com a palavra ''.

Com o dicionario imitador é bastante simples emitir aleatoriamente texto
que imita o original. Imprima uma palavra, depois veja quais palavras podem
vir a seguir e pegue uma aleatoriamente como a proxima palavra do texto.

Use a string vazia como a primeira palavra do texto para preparar as coisas.

Nota: o módulo padrão do python 'random' conta com o random.choice(list),
método que escolhe um elemento aleatório de uma lista não vazia.
"""

import random
import sys

def read_text_from_file(filename):
    with open(filename) as f:
        text = f.read()
    return text

def words_from_text(text):
    return text.lower().split()

def mimic_dict(filename):
    """Retorna o dicionario imitador mapeando cada palavra para a lista de
    palavras subsequentes."""
    # +++ SUA SOLUÇÃO +++

    text = read_text_from_file(filename)
    wordlist = words_from_text(text)
        
    mimic_dict = {
      '': [wordlist[0]] 
    }

    def add_next_word_to_mimic_dict(current_word, next_word, mimic_dict):
        if current_word in mimic_dict.keys():
            mimic_dict[current_word].append(next_word)
        else:
            mimic_dict[current_word] = [next_word]
        
    for i, word in enumerate(wordlist):
        
        if i == len(wordlist) - 1:
            add_next_word_to_mimic_dict(word, '', mimic_dict)
        else:
            add_next_word_to_mimic_dict(word, wordlist[i+1], mimic_dict)

    print(mimic_dict)
    
    return mimic_dict


def print_mimic(mimic_dict, word):
    """Dado o dicionario imitador e a palavra inicial, imprime texto de 200 palavras."""
    # +++ SUA SOLUÇÃO +++
    text = word
    wordcount = 1 if word else 0

    while wordcount < 200:
        next_word = random.choice(mimic_dict[word])
        if next_word:
            text = ' '.join([text, next_word])
            wordcount += 1
        word = next_word

    print(text)


# Chama mimic_dict() e print_mimic()
def main():
  if len(sys.argv) != 2:
    print('Utilização: ./14_mimic.py file-to-read')
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, '')


if __name__ == '__main__':
  main()
