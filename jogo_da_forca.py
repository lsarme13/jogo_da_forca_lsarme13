"""
Jogo da Forca - Versão Terminal

Descrição:
Este script implementa uma versão simples do tradicional jogo da forca,
onde o jogador deve adivinhar uma palavra secreta letra por letra antes
de esgotar o número de tentativas disponíveis.

Características:
- Palavra aleatória de uma lista predefinida
- 5 vidas para errar
- Feedback visual sobre acertos e erros
- Pontuação baseada nas vidas restantes e no comprimento da palavra

Autor: Luan Sarmento Orsi da Silva
Data: 12 de Novembro de 2024
"""

import random

# Lista de palavras possíveis
PALAVRAS = list(set([
    'beijo', 'cacto', 'feito', 'moeda', 'sarjeta', 'amor', 'paixao', 'doce',
    'treta', 'prazer', 'encanto', 'carinho', 'estrume', 'folgado', 'quente',
    'brega', 'banheiro', 'sutileza', 'chamego', 'cafune', 'delicia', 'trapaca',
    'namoro', 'paquera', 'ciumes', 'doidice', 'farsa', 'balela', 'piada',
    'pirralho', 'bobagem', 'charme', 'vaidade', 'seducao', 'covarde', 'amizade',
    'maldade', 'poder', 'luxuria', 'bumbum', 'bagunca', 'bolado', 'trevosa',
    'vergonha', 'biruta', 'escandalo', 'babado', 'putaria', 'broto', 'amasso',
    'macaco', 'golpe', 'enrosco', 'zoeira', 'paranoia', 'medroso', 'moleque',
    'gracinha', 'nobreza', 'cheiro', 'feioso', 'comedia', 'alegria', 'rebeldia',
    'coragem', 'mandinga', 'doente', 'cremoso', 'doidinho', 'ladrao', 'bebado',
    'sonhador', 'bondade', 'sarcasmo', 'gentileza', 'intenso', 'gaiato',
    'loucuras', 'aposta', 'esquema', 'inocente', 'romance', 'adorado',
    'florido', 'briguento', 'brinquedo', 'carencia', 'desleixo', 'porrete',
    'cabelo', 'banguela', 'malandro', 'falsidade', 'fanfarra', 'melodia',
    'amargura', 'chocante', 'dureza', 'valente'
]))


def selecionar_palavra():
    """
    Seleciona uma palavra aleatória da lista de palavras.

    Returns:
        str: Palavra escolhida.
    """
    return random.choice(PALAVRAS)


def mostrar_progresso(palavra, letras_descobertas):
    """
    Exibe o progresso atual do jogador, mostrando letras já adivinhadas e espaços vazios.

    Args:
        palavra (str): Palavra secreta.
        letras_descobertas (list[str]): Letras que o jogador já acertou.

    Returns:
        list[str]: Lista com as letras corretamente adivinhadas até o momento.
    """
    progresso = []

    print("\nPalavra: ", end="")
    for letra in palavra:
        if letra in letras_descobertas:
            print(letra.upper(), end=" ")
            progresso.append(letra)
        else:
            print("_", end=" ")

    return progresso


def validar_tentativa(tentativa, letras_descobertas, letras_erradas):
    """
    Valida a tentativa do jogador.

    Args:
        tentativa (str): Letra inserida pelo jogador.
        letras_descobertas (list[str]): Letras já descobertas.
        letras_erradas (list[str]): Letras já tentadas e incorretas.

    Returns:
        str: Mensagem de erro, se houver. Caso contrário, retorna None.
    """
    if len(tentativa) != 1 or not tentativa.isalpha():
        return "Digite apenas **uma única letra** válida."
    if tentativa in letras_descobertas:
        return f"A letra '{tentativa.upper()}' já foi descoberta."
    if tentativa in letras_erradas:
        return f"Você já tentou a letra '{tentativa.upper()}'."
    return None


def jogar():
    """
    Função principal que executa o loop do jogo.
    """
    print("====== JOGO DA FORCA ======\n")

    palavra = selecionar_palavra()
    letras_descobertas = []
    letras_erradas = []
    vidas = 5

    print(f"Adivinhe uma palavra de {len(palavra)} letras.")

    while vidas > 0:
        print(f"\nVidas restantes: {vidas}")
        progresso = mostrar_progresso(palavra, letras_descobertas)

        if len(progresso) == len(palavra):
            print("\n\n🎉 Parabéns! Você acertou a palavra!")
            print(f"✔ Pontuação final: {vidas * len(palavra)} pontos.")
            return

        tentativa = input("\n\nDigite uma letra: ").lower().strip()
        erro = validar_tentativa(tentativa, letras_descobertas, letras_erradas)

        if erro:
            print(f"⚠ {erro}")
            continue

        if tentativa in palavra:
            print(f"✅ A letra '{tentativa.upper()}' está correta!")
            letras_descobertas.append(tentativa)
        else:
            print(f"❌ A letra '{tentativa.upper()}' não está na palavra.")
            letras_erradas.append(tentativa)
            vidas -= 1

    print("\n💀 Fim de jogo! Suas vidas acabaram.")
    print(f"A palavra correta era: {palavra.upper()}")


if __name__ == "__main__":
    jogar()