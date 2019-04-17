# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Manuel Castanares, manuelc@al.insper.edu.br
# - aluno B: Thomas Bekhor, thomasb2@al.insper.edu.br

def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "andar professor": "Tomar o elevador para o andar do professor",
                "biblioteca": "Ir para a biblioteca"
            }
        },
        "andar professor": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                "professor": "Falar com o professor"
            }
        },
        "professor": {
            "titulo": "O monstro do Python",
            "descricao": "Voce foi pedir para o professor adiar o EP. "
                         "O professor revelou que é um monstro disfarçado "
                         "e devorou sua alma.",
            "opcoes": {}
        },
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada"
            }
        }
    }
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual


def main():
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()

    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]

        print(cenario_atual["titulo"])
        
        barras = "-"*len(cenario_atual["titulo"])
        
        print(barras)
        
        print(cenario_atual["descricao"])

        opcoes = cenario_atual['opcoes']
        
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:
#<<<<<<< HEAD
           
            print ()
            
            print('Escolha sua opção:')
            
            print()
            
            for local in opcoes:
                
                print("{0}: {1}".format(local, opcoes[local]))
            
            
#=======

#>>>>>>> 8052eadd886d4bc9a73c4a5f0b79bc6ed6e2bb25
            escolha = input('O que você quer fazer?: ')

            if escolha in opcoes:
                nome_cenario_atual = escolha
                
                print('Escolha sua opção:')
                print(cenario_atual['opcoes'])
                          
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True
            
    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()
    
    
