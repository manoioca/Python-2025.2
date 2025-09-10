import random

print ('   |   |   ')
print ('-----------')
print ('   |   |   ')
print ('-----------')
print ('   |   |   ')

class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = [" " for _ in range(9)]
        self.jogador_atual = "X"
        
        self.jogador_humano = "O"
    
    def exibir_tabuleiro(self):
        print(f" {self.tabuleiro[0]} | {self.tabuleiro[1]} | {self.tabuleiro[2]} ")
        print("-----------")
        print(f" {self.tabuleiro[3]} | {self.tabuleiro[4]} | {self.tabuleiro[5]} ")
        print("-----------")
        print(f" {self.tabuleiro[6]} | {self.tabuleiro[7]} | {self.tabuleiro[8]} ")

    def fazer_jogada(self, posicao):
        if self.tabuleiro[posicao] == " ":
            self.tabuleiro[posicao] = self.jogador_atual
            return True
        else:
            print("Posição já ocupada. Tente outro número.")
            return False

    def verificar_vencedor(self):
        combinacoes = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  
            (0, 4, 8), (2, 4, 6)              
        ]
        for x, y, z in combinacoes:
            if self.tabuleiro[x] == self.tabuleiro[y] == self.tabuleiro[z] != " ":
                return True
        return False

    def verificar_empate(self):
        return " " not in self.tabuleiro

    def alternar_jogador(self):
        self.jogador_atual = "O" if self.jogador_atual == "X" else "X"
    
    def jogada_ia(self):

        posicoes_vazias = [i for i, x in enumerate(self.tabuleiro) if x == " "]
        posicao_escolhida = random.randint(0,8)
        print(f"Jogador O (IA) escolheu a posição {posicao_escolhida + 1}")
        return posicao_escolhida

    def jogar(self):
        print("W E L C O M E     T O      T I C - T A C - T O E  !")
        while True:
            self.exibir_tabuleiro()
            if self.jogador_atual == self.jogador_humano:
                try:
                    pos = int(input(f"Jogador {self.jogador_atual}, escolha uma posição (1-9): ")) - 1
                    if pos < 0 or pos > 8:
                        print("Jogada inválida. Digite um número de 1 a 9.")
                        continue
                except ValueError:
                    print("Jogada inválida. Digite outro número.")
                    continue
            else:
                pos = self.jogada_ia()

            if self.fazer_jogada(pos):
                if self.verificar_vencedor():
                    self.exibir_tabuleiro()
                    print(f"Jogador {self.jogador_atual} venceu!")
                    break
                elif self.verificar_empate():
                    self.exibir_tabuleiro()
                    print("Empate!")
                    break
                else:
                    self.alternar_jogador()


if __name__ == "__main__":
    jogo = JogoDaVelha()
    jogo.jogar()
