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
                "banheiro": "Dar um cagão",
                "biblioteca":"fingir que vai estudar pra prova de Dessoft"
            }
        },
        "biblioteca": {
            "titulo": " Lugar de estudos",
            "descricao": "Lugar silencioso com muitas pessoas bonitas",
            "opcoes": {
                  "inicio": "Tomar o elevador para o saguao de entrada",
                  "banheiro": "Dar um cagão"}},
          
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
                "sala coordenação": "fugir para a sala mestre",
                "insistir": "continuar tentando com El Tochi, o domador"}},
       
       "insistir": {
               "titulo": "ainda na sala de El Tochi",
               "descricao": "",
               "opcoes":{}
            },
        
       "banheiro": {
            "titulo": "Caverna escura",
            "descricao": "Voce esta no banheiro fedorento",
            "opcoes": {
                "inicio": "Voltar para o saguão de entrada"}
        },
        "sala coordenação": {
             "titulo": " Carol da Costa cafofo's",
             "descricao": "Após nao suceder na sala do El Tochi," 
                          "voce encontrou a sala de controle total do insper",
             "opcoes": {
                     "inicio": "Voltar para o saguão de entrada"}}
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
    
    import random
    
    player1 = 100
    
    emocional = 100
    
    ataque = 20
    
    inventário = []
    
    loira_banheiro = True
    
    verdade = True
    
    elevador = True
    
    game_over = False
    
    transporte = True
    
    menina = True
    
    vencer = False
    
    senha = True
    
    while not game_over and player1 > 0:
        
        cenario_atual = cenarios[nome_cenario_atual]

        print(cenario_atual["titulo"])
        
        barras = "-"*len(cenario_atual["titulo"])
        
        print(barras)
        
        print(cenario_atual["descricao"])
        
        print()
        
        print("Seu total de hitpoints é: {0}".format(player1))
        
        print()
        
        print("Seu emocional está em : {0}" .format(emocional))
        
        print()
        
        print("seu ataque está em : {0}".format(ataque))
        
        monstro = random.randint(1, 10)
        
        if monstro == 3:
            
            print("Um aluno da GV apareceu no Insper e quer lutar!")
            
            print()
            
            monstro_luta = input("Quer lutar ou correr? ")
            
            if monstro_luta == "lutar":
                    print()
                    print("Você acabou com ele!")
                    print()
                    print("hitpoints: +30, emocional: +20")
                    
                    player1 += 30
                    emocional += 20
                    
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

                if escolha == 'banheiro':
                    
                    if loira_banheiro:

                        print("Voce encontrou a loira do banheiro e se assutou brutalmente:") 
                
                        print("-25 hit points")
                    
                        print("-10 emocional")
                    
                        print()
                    
                        player1 -= 25
                    
                        emocional -=10
                        
                        loira_banheiro = False
                    
                    if transporte:
                        
                        print("Você encontrou uma porta secreta no banheiro de deficientes.")
                    
                        print("Nela esta escrito: Transporte-se para qualquer sala")
                    
                        print("se acertar um numero sorteado de 1 a 20.")
                    
                        numero_aleat = random.randint(1, 20)
                        
                        i = 0
                        
                        acertou_numero = True
                        
                        while i <= 4 and acertou_numero:
                            
                            numero = int(input("numero entre 1 e 20: "))
                            
                            if numero < numero_aleat:
                        
                                print("Voce errou! tente um numero maior")
                                print()
                                print("-10 hitpoints")
                                player1 -= 10
                                i += 1
                                
                            elif numero > numero_aleat:
                                
                                print()
                                print("Voce errou! tente um numero menor")
                                print()
                                print("-10 hitpoints")
                                player1 -= 10
                                i += 1
                                
                            else:
                            
                                print("Voce acertou, escolha uma sala entre as seguintes")
                         
                                print("para se teletransportar: biblioteca, sala professor, sala coordenação, Porta da sala")
                        
                                teletransporte = input("Sala escolhida: ")
                        
                                escolha = teletransporte
                            
                                nome_cenario_atual = teletransporte
                            
                                transporte = False
                                
                                acertou_numero = False
                                
                            
                            
                        if i == 4:
                            
                            print()
                            print("Volte mais tarde!")
                            print()
                            
                        
                    else:
                        
                        print()
                        
                        print("O teletransportador já está desbloqueado!")
                        
                        print()
                        
                        print("teletransportar para: biblioteca, sala professor, sala coordenação, Porta da sala")
                        
                        teletransporte = input("Sala escolhida: ")
                        
                        escolha = teletransporte
                        
                        nome_cenario_atual = teletransporte
                        
             
                if escolha == "biblioteca":

                    if menina:
                    
                        print("Tem uma menina que não entendeu algumas coisas sobre python...")
                    
                        print("ela pediu a sua ajuda" )
                    
                        ajuda = input("quer ajudar, sim ou não?: ")
                    
                        if ajuda == "sim":
                            print()
                            print("ela pergunta se abre dicionarios com chave ou parênteses.")
                        
                            dic_chaves = input("chave ou parênteses?: ")
                        
                            if dic_chaves == "chave":
                                
                                print()
                                
                                print("muito bem! +10 emocional")
                            
                                emocional += 10
                            
                                print("agora ela quer usar um numero decimal. O que ela usa?")
                            
                                numero = input("float ou int?: ")
                            
                                if numero == "float":
                                
                                    print()
                                    print("muito bem! +10 emocional")
                                
                                    emocional += 10
                                    
                                    print("Ela faz uma última pergunta...")
                                    
                                    print()
                                    
                                    lançamento = int(input("Em que ano foi lançado o python?: "))
                                    
                                    if lançamento == 1989:
                                        
                                        print("Ela está muito agradecida e te entrega uma chave estranha!")
                                        
                                        print()
                                        
                                        chave = input("Guardar ou devolver?: ")
                    
                                        if chave == "Guardar":
                                            
                                            print("Chave adicionada ao inventário")
                        
                                            inventário.append("Chave")
                                        
                                            menina = False
                                        
                                    else:
                                        
                                        print ()
                                        
                                        print("Esse ano é incorreto, -30 emocional")
                                        
                                        print ()
                                        
                                        emocional -= 20
                                        
                                else:
                                    print()
                                    print("ela descubriu que não é int! -20 emocional")
                                    print()
                                    emocional -= 20  
                                    
                                
                                
                            else: 
                                print()
                                print("ela ficou brava! -20 emocional")
                                print()
                                emocional -= 20
                                
                if escolha == "sala professor" and verdade:
                    
                    funcionario = {"hitpoints": 35, "ataque": 5}
                    
                    print()
                    
                    print("Você encontrou uma espada: +50 pontos de ataque")
                    
                    ataque += 50
                    
                    print()
                    
                    inventário.append("espada")
                    
                    print("espada adicionada ao inventário")
                    
                    print()
                    
                    verdade = False
                    
                    if elevador:
                    
                        print('O elevador esta lotado, você terá que ir de escada')
                    
                        print()
                    
                        print('O funcionario da casa do pao de queijo apareceu:')
                    
                        print('Ele quer te desafiar pra uma luta pois acabou de ser demitido.')
                    
                        print() 
                    
                        print('Player 1: {0} hitpoints, {1} de emocional, {2} de ataque' .format(player1, emocional, ataque))
                    
                        print("Funcionario demitido: hitpoints: {0}, ataque: {1}".format(funcionario["hitpoints"], funcionario["ataque"]))
                    
                        print()
                    
                        decisao=input('Voce deseja correr ou lutar?: ')
                    
                        if decisao =='lutar':
    
                            if ataque > funcionario["hitpoints"]:
                        
                                print('Player 1 atacou e causou uma morte emocional ao ex-funcionario, coitado!')
                            
                                print()
                            
                                print("Na luta, o ex-funcionario jogou um pão de queijo na sua cara")
                            
                                print()
                            
                                print("-5 hitpoints")
                                
                                player1 -= 5
                                
                                elevador = False
                                
                                print()
                                
                                print("elevador desbloqueado!")
                                
                                print()
                                
                                print("Você econtrou um papel com um enigma!")
                                
                                papel = "tdoesf"
                                
                                ver_enigma = input("Quer ver o enigma: sim ou não? ")
                                
                                if ver_enigma == "sim":
                                    
                                    print("o enigma diz: {0}".format(papel))
                                    
                                    inventário.append("tdoesf")
                                    
                                    print()
                                    
                                    print("enigma adicionado ao inventário")
                            
                        else:
                            
                            print('Voce é um frangolone')
                        
                            print()
                        

                            print("-15 emocional")
                        
                            emocional -= 15
                 
                if escolha == "sala coordenação":
                    
                    print()
                    
                    print("Você precisa de uma chave para entrar!")
                    
                    print()
                    
                    procura_chave = input("Quer abrir seu inventário para ver se tem uma chave? sim ou não?: ")
                    
                    if procura_chave == "sim":
                        
                        print(inventário)
                        
                    
                        if "Chave" in inventário:
                            
                            print("Deseja usar a chave?")
                            
                            utilizar_chave = input("sim ou não?: ")
                            
                            if utilizar_chave == "sim":
                                
                                print("Agora precisa chutar a contrasenha do PC")
                   
                                print()
                                
                                palavra = input("Quer abrir o inventário para ver se tem alguma pista? ")
                                
                                if palavra == "sim":
                                    
                                    print(inventário)
                                
                                contador = 0
                                
                                print()
                                
                                print("Voce tem 3 tentativas!")
                                
                                print()
                                
                                while contador <3 and senha:
                                    
                                    chute = input("qual é a senha?: ")
                                    
                                    if chute == "desoft":
                                    
                                        senha = False
                    
                                        print("Voce conseguiu alterar a data da entrega do EP")
                        
                                        print()
                    
                                        print("no computador da Carol da Costa, parabens!")
                        
                                        print()
                                
                                        print("Mas calma, ainda nao acabou. A secretaria da carol da Costa")
                                
                                        print("te viu hackeando o computador dela")
                                
                                        print("Ela está pedindo 60 hitpoints como suborno para manter em segredo")
                                
                                        segredo=input("Pagar ou correr o risco?: ")
                                
                                        if segredo == "Pagar":
                                    
                                            if player1 > 50:
                                    
                                                player1 -= 60
                                    
                                                print("Agora sim sua missao foi concluida!")
                                                
                                                game_over = True
                                                
                                                vencer = True
                                    
                                            elif player1 < 50:
                                        
                                                print("Voce nao tem hitpoints suficientes, vai ter que correr o risco")
                                                
                                                game_over = True
                                                
                                                vencer = True
                                    
                                            elif player1 == 50:
                                        
                                                player1-=50
                                        
                                                print("Voce pagou o suborno porem perdeu todos seus hitpoints e morreu")
                                        
                                                print("Porem o adiamento foinconcluido mesmo assim")
                                        
                                                print("e seus colegas vao fazer um belo EP para honrar a sua dificil missao. " )
                                                
                                                game_over = True
                                                
                                                vencer = True
                                
                                        else:
                                    
                                            print("Run away, voce tem o risco de ser jubilado")
                                        
                                            game_over = True
                                            
                                            vencer = True
                                    else:
                                        
                                        print("Dica: primeiro semestre")
                                        
                                        contador += 1
                                
                                game_over = True
                    
                                
                        else:
                        
                            print ()
                        
                            print("Voce nao tem a chave para esta sala")
                        
                            print()
                        
                        
                          
            else:
                
                print('O adiamento do EP não foi um sucesso')
                
                print()
                
                print("Sua indecisão foi sua ruína!")
                game_over = True
    
    if vencer:
        
        print("você conseguiu adiar o EP!")
        
    else:  
        
        print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()
    
    
