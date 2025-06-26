''' Jogo da Forca utilizando Orientação a Objeto.'''
import random

class Forca:
    def __init__(self, palavras):
        self.palavras = palavras
        self.palavra = self.escolher_palavra()
        self.letras_descobertas = []
        self.letras_erradas = []
        self.vidas = 5
        
    
    def escolher_palavra(self):
        ''' Seleciona uma palavra aleatória da lista de palavras.'''
        return random.choice(self.palavras)
    
    
    @property
    def progresso(self):
        ''' Define o progresso atual do jogador, mostrando letras já
            adivinhadas e espaços das palavras a descobrir.'''
        progresso = []
        for letra in self.palavra:
            if letra in self.letras_descobertas:
                progresso.append(letra.upper())
            else:
                progresso.append("_")
        return " ".join(progresso)
    
    
    def tentativa(self):
        """ Permite que o jogador arrisque uma tentativa.
            Valida a tentativa do jogador, avançando o progresso
            da descoberta da palavra caso ele acerte, ou
            diminuindo sua vida restante caso esteja errado."""
        print(f"{self.progresso.upper()}")
        tentativa = input("Arrisque uma letra: ")
        if len(tentativa) != 1 or not tentativa.isalpha():
            print("Digite apenas **uma única letra** válida.")
        elif tentativa in self.letras_descobertas:
            print(f"A letra {tentativa.upper()} já foi descoberta.")
        elif tentativa in self.letras_erradas:
            print(f"Você já tentou a letra '{tentativa.upper()}'.")
        elif tentativa in self.palavra:
            print(f"✅ A letra '{tentativa.upper()}' está correta.")
            self.letras_descobertas.append(tentativa)
        else:
            print(f"❌ A letra '{tentativa.upper()}' não está na palavra.")
            self.letras_erradas.append(tentativa)
            self.vidas -= 1
        return
    
    
    def concluir(self):
        ''' Apresenta a pontuação final do jogo em caso de vitória,
            ou uma mensagem de Game Over caso as vidas estejam
            esgotadas. '''
        if self.vidas == 0:
            print("\n💀 Fim de jogo! Suas vidas acabaram.")
            print(f"A palavra correta era: {self.palavra.upper()}")
            return False
        if "_" not in self.progresso:
            print("\n\n🎉 Parabéns! Você acertou a palavra!")
            print(f"Pontuação final: {self.vidas * len(self.palavra)}")
            return True
            
    
    def jogar(self):
        ''' Inicia o looping principal do jogo. '''
        print("====== JOGO DA FORA ======")
        print(f"Adivinhe uma palavra de {len(self.palavra)} letras.\n")

        while self.vidas > 0 and len(self.letras_descobertas) < len(self.palavras):
            print(f"Vidas restantes: {'❤' * self.vidas}")
            self.tentativa()
        self.concluir()
        
        
if __name__ == "__main__":
    # Lista de palavras possíveis
    PALAVRAS = [
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
    ]
    f = Forca(PALAVRAS)
    f.jogar()

    