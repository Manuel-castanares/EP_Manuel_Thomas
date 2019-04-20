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
                "sala professor": "Tomar o elevador para o andar do professor",
                "banheiro": "Dar um cagão"
            }
        },
        "sala professor": {
            "titulo": "sala do desespero",
            "descricao": "Voce esta na frente da sala do professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                "Porta da sala": "Bater na porta"
            }
        },
        "Porta da sala": {
            "titulo": "O monstro do Python: El Tochi",
            "descricao": "Voce foi pedir para o professor adiar o EP. "
                         "O professor revelou que é um domador de cobras "
                         "e assim, soltou na sala uma grande anaconda, "
                         "uma mamba negra e sua favorita, a python blackboardiana.",
            "opcoes": {
                "sala coordenação: fugir para a sala mestre",
                "insistir: continuar tentando com El Tochi: domador"}
        },
        "banheiro": {
            "titulo": "Caverna escura",
            "descricao": "Voce esta no banheiro fedorento",
            "opcoes": {
                "inicio": "Voltar para o saguão de entrada"
            }
        },
        "sala coordenação": {
             "titulo": " Carol da Costa cafofo's",
             "descricao": "Após nao suceder na sala do El Tochi," 
                          "voce encontrou a sala de controle total do insper",
             "opcoes": {
                 "Entrar computador": "alterar entrega EP"}
        }}
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

    player1 = 100
    
    emocional = 100
    
    verdade = True
    
    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]

        print(cenario_atual["titulo"])
        
        barras = "-"*len(cenario_atual["titulo"])
        
        print(barras)
        
        print(cenario_atual["descricao"])
        
        print()
        
        print("Seu total de hitpoints é: {0}".format(player1))
        
        print()
        
        print("Seu emocional está em : {0}" .format(emocional))

        opcoes = cenario_atual['opcoes']
        
        if len(opcoes) == 0:
            
            print()
            
            print("Você foi devorado! Miou pra voce parça... Aiaiaiuiuiui")
            game_over = True
            
        else:
           
            print ()
            
            print('Escolha sua opção:')
            
            print()
            
            for local in opcoes:
                
                print("{0}: {1}".format(local, opcoes[local]))
            
            escolha = input('O que você quer fazer?: ')

            if escolha in opcoes:
                
                nome_cenario_atual = escolha

                if escolha=='banheiro':

                    print("Voce encontrou a loira do banheiro e se assutou brutalmente:") 
                
                    print("-25 hit points")
                    
                    player1 -= 25
                    emocional -=10
                    print()
             
                
                if escolha == "sala professor" and verdade:
                    
                    print()
                    
                    print("Você encontrou uma espada: +50 hit points")
                    
                    player1 += 50
                    
                    print()
                    
                    verdade = False
                        
                    print('O elevador esta lotado, você terá que ir de escada')
                    
                    print()
                    
                    print('O funcionario da casa do pao de queijo apareceu:')
                    
                    print('Ele quer te desafiar pra uma luta pois acabou de ser demitido.')
                    
                    print() 
                    
                    print('Player 1: {0} hitpoints, {1} de emocional' .format(player1, emocional))
                    
                    print('Funcionario demitido: 80 hitpoints, 20 emocional')
                    
                    print()
                    
                    decisao=input('Voce deseja correr ou lutar?: ')
                    
                    if decisao =='lutar':
                        
                        print('Player 1 atacou e causou uma morte emocional ao ex-funcionario, coitado!')
                        
                    else:
                        print('Voce é um frangolone')
                        
                        print()
                    
                        emocional -=15
                    
                          
            else:
                
                print('O adiamento do EP nã foi um sucesso')
                
                print()
                
                print("Sua indecisão foi sua ruína!")
                game_over = True
            
    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()
    
    
