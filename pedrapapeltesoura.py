from random import choice

jogador_vitorias = 0 
maq_vitorias = 0 

def Opcao_jogador():
    esc_jogador = input("Escolha: Pedra, Papel ou Tesoura: ")
    esc_jogador.lower()
    if esc_jogador == "pedra":
        return esc_jogador
    elif esc_jogador == "papel":
        return esc_jogador
    elif esc_jogador == "tesoura":
        return esc_jogador
    else: 
        print("Opção invalida, tente novamente")
        Opcao_jogador()
        
        
def Opcao_Maquina():
   esc_maquina = choice(["pedra", "papel", "tesoura"])
   return esc_maquina
   
   
while True:
    
    print("-"*30)
    esc_jogador = Opcao_jogador()
    esc_maquina = Opcao_Maquina()
    print("-"*30)
    
    if (esc_jogador == "pedra") and (esc_maquina == "tesoura") \
        or (esc_jogador == "papel") and (esc_maquina == "pedra") \
            or (esc_jogador =="tesoura") and (esc_maquina == "papel"):
            #JOGADOR GANHA
            print(f"Jogador escolheu {esc_jogador} e a maquina escolheu {esc_maquina}."
            " Resultado: Você Ganhou!")
            jogador_vitorias += 1 
            
    elif esc_jogador == esc_maquina:
        #empate
        print(f"Jogador escolheu {esc_jogador} e a maquina escolheu {esc_maquina}."
            " Resultado: Empate!")
            
    else: 
        print(f"Jogador escolheu {esc_jogador} e a maquina escolheu {esc_maquina}."
            " Resultado: Você Perdeu!")
        maq_vitorias += 1
    
    print("-"*30)
    print(f"Vitorias do jogador: {jogador_vitorias}")
    print(f"Vitorias da maquina: {maq_vitorias}")
    print("-"*30)
    
    esc_jogador = input("Voce quer jogar novamente?  ")
    if esc_jogador in ["SIM", "sim", "s", "S", "Sim"]:
        pass
    elif esc_jogador in ["NAO", "Nao", "n", "N", "nao"]:
        break
    else:
        break