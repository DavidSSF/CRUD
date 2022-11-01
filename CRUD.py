x=0
while x==0:
    op1=str(input("Pressione Enter para começar: "))
    if op1=="":
        print("-----------------------------------------------------------------------\n")
        print("                         Bem Vindo ao Programa CRUD")
        print("                                      de")
        print("             💻   Anderson Melo da Silva  N.º05 1°B 2022    💻")
        print("             💻  David Saboia e Silva Filho  N.º13 1°B 2022 💻")
        print("\n-----------------------------------------------------------------------")
        nome="Sem dado"
        local="Sem dado"
        numero="Sem dado"
        email="Sem dado"
        senha="Sem dado"
        a=0
        while a==0:
            print("\n#Menu inicial#")
            print("\n1-Cadastrar")
            print("2-Ler")
            print("3-Deletar")
            print("4-Atualizar")
            print("5-Sair")
            op2=str(input("Escolha dentre as opções anteriores: "))
            if op2=="1":
                b=0
                while b==0:
                    nome=str(input("Escreva seu nome: "))
                    local=str(input("Qual sua localidade: "))
                    numero=str(input("Seu número de telefone: "))
                    email=str(input("Seu e-mail: "))
                    senha=str(input("Sua senha: "))
                    print("\nSeus dados de cadastros são:")
                    print("Nome: ",nome,"\nLocalidade: ",local,"\nTelefone: ",numero,"\nE-mail: ",email,"\nSenha: ",senha)
                    d=0
                    while d==0:
                        op=str(input("Você deseja-\n1-Confirmar\n2-Refazer\n"))
                        if op=="1":
                            if nome=="Sem dado" or local=="Sem dado" or numero=="Sem dado" or email=="Sem dado" or senha=="Sem dado" or nome==op1 or local==op1 and numero==op1 or email==op1 or nome=="sem dado" or local=="sem dado" or numero=="sem dado" or email=="sem dado" or senha=="sem dado":
                    	        print("\nHá campos sem dado.Por favor preencha os campos corretamente.\n")
                    	        b=0
                    	        d=1
                            else:
                    	        print("\nDados salvos\n")
                    	        b=1
                    	        d=1
                        if op=="2":
                            b=0
                            d=1
                        elif op!="1" and op!="2":
                            print("\nSem função\n")
            if op2=="2":
                print("\nÚltimos dados de cadastros são:")
                print("Nome: ",nome,"\nLocalidade: ",local,"\nTelefone: ",numero,"\nE-mail: ",email,"\nSenha: ",senha)
                op=str(input("Pressione Enter para ir ao menu inicial: "))
                if op==op:
                    a=0
            if op2=="3":
                if nome=="Sem dado" and local=="Sem dado" and numero=="Sem dado" and email=="Sem dado" and senha=="Sem dado":
                    print("\nNão há dados no cadastro.\n")
                if nome!="Sem dado" or local!="Sem dado" or numero!="Sem dado" or email!="Sem dado":
                    print("\nSeus dados de cadastros são:\n")
                    print("Nome: ",nome,"\nLocalidade: ",local,"\nTelefone: ",numero,"\nE-mail: ",email,"\nSenha: ",senha)
                    d=0
                    while d==0:
                        print("\nQual você deseja deletar:")
                        print("1-Nome")
                        print("2-Local")
                        print("3-Telefone")
                        print("4-E-mail")
                        print("5-Senha")
                        print("6-Todos os dados")
                        print("7-Voltar ao menu inicial")
                        op=(input())
                        if op=="1":
                            print("Deletado")
                            nome="Sem dado"
                            d=1
                        if op=="2":
                            print("Deletado")
                            local="Sem dado"
                            d=1
                        if op=="3":
                            print("Deletado")
                            numero="Sem dado"
                            d=1
                        if op=="4":
                            print("Deletado")
                            email="Sem dado"
                            d=1
                        if op=="5":
                            print("Deletado")
                            senha="Sem dado"
                            d=1
                        if op=="6":
                            print("Deletados")
                            nome="Sem dado"
                            local="Sem dado"
                            numero="Sem dado"
                            email="Sem dado"
                            senha="Sem dado"
                            d=1
                        if op=="7":
                            d=1
                        elif op!="1" and op!="2" and op!="3" and op!="4" and op!="5" and op!="6" and op!="7":
                            print("\nSem função\n")
                            d=0
            if op2=="4":
                if nome=="Sem dado" and local=="Sem dado" and numero=="Sem dado" and email=="Sem dado" and senha=="Sem dado":
                	print("\nVocê não tem nenhum dado salvo")
                if nome!="Sem dado" or local!="Sem dado" or numero!="Sem dado" or email!="Sem dado" or senha!="Sem dado":
                    c=0
                    print("\nSeus dados de cadastros são:")
                    print("Nome: ",nome,"\nLocalidade: ",local,"\nTelefone: ",numero,"\nE-mail: ",email,"\nSenha: ",senha)
                    d=0
                    while d==0:
                        print("Qual campo você quer Atualizar: \n")
                        print("1-Nome")
                        print("2-Local")
                        print("3-Telefone")
                        print("4-E-mail")
                        print("5-Senha")
                        print("6-Todos os dados")
                        print("7-Retornar ao menu inicial")
                        op=str(input())
                        if op=="1":
                            while c==0:
                                nome1=str(input("Digite seu novo Nome: "))
                                print("Você deseja:\n1-Salvar dado\n2-Refazer dado")
                                op=str(input())
                                if op=="1":
                                    nome=nome1
                                    c=1
                                    d=1
                                if op=="2":
                                    c=0
                                elif op!="1" and op!="2":
                                    print("\nSem função\n")
                                    c=0
                        if op=="2":
                            while c==0:
                                local1=str(input("Digite seu novo Local: "))
                                print("Você deseja:\n1-Salvar dado\n2-Refazer dado")
                                op=str(input())
                                if op=="1":
                                    local=local1
                                    c=1
                                    d=1
                                if op=="2":
                                    c=0
                                elif op!="1" and op!="2":
                                    print("\nSem função\n")
                        if op=="3":
                            while c==0:
                                numero1=str(input("Digite seu novo Número: "))
                                print("Você deseja:\n1-Salvar dado\n2-Refazer dado")
                                op=str(input())
                                if op=="1":
                                    numero=numero1
                                    c=1
                                    d=1
                                if op=="2":
                                    c=0
                                elif op!="1" and op!="2":
                                    print("\nSem função\n")
                        if op=="4":
                            while c==0:
                                email1=str(input("Digite seu novo E-mail: "))
                                print("Você deseja:\n1-Salvar dado\n2-Refazer dado")
                                op=str(input())
                                if op=="1":
                                    email=email1
                                    c=1
                                    d=1
                                if op=="2":
                                    c=0
                                elif op!="1" and op!="2":
                                    print("\nSem função\n")
                        if op=="5":
                            while c==0:
                                senha1=str(input("Digite seu novo Senha: "))
                                print("Você deseja:\n1-Salvar dado\n2-Refazer dado")
                                op=str(input())
                                if op=="1":
                                    senha=senha1
                                    c=1
                                    d=1
                                if op=="2":
                                    c=0
                                elif op!="1" and op!="2":
                                    print("\nSem função\n")
                        if op=="6":
                            while c==0:
                                nome1=str(input("Escreva seu nome: "))
                                local1=str(input("Qual sua localidade: "))
                                numero1=str(input("Seu número de telefone: "))
                                email1=str(input("Seu e-mail: "))
                                senha1=str(input("Sua senha: "))
                                e=0
                                while e==0:
                                    print("Você deseja:\n1-Salvar dados\n2-Refazer dados")
                                    op=str(input())
                                    if op=="1":
                                        nome=nome1
                                        local=local1
                                        numero=numero1
                                        email=email1
                                        senha=senha1
                                        c=1
                                        e=1
                                        d=1
                                    if op=="2":
                                        c=0
                                        e=1
                                    elif op!="1" and op!="2":
                                        print("\nSem função\n")
                                        e=0
                        if op=="7":
                            d=1
                        elif op!="1" and op!="2" and op!="3" and op!="4" and op!="5" and op!="6" and op!="7":
                            print("\nSem função\n")
            if op2=="5":
                b=0
                while b==0:
                    op=str(input("Você deseja:\n1-Sair\n2-Voltar ao menu incial\n"))
                    if op=="1":
                        print("--------------------")
                        print("❌Fim do Programa❌")
                        print("--------------------")
                        a=1
                        b=1
                        x=1
                    if op=="2":
                        b=1
                    elif op!="1" and op!="2":
                        print("\nSem função\n")
                        b=0
            if op2=="1010":
            	print("---------------------------")
            	print("🎉Herbert Melhor Professor🎉")
            	print("---------------------------")
            	a=1
            if op2!="1" and op2!="2" and op2!="3" and op2!="4" and op2!="5" and op2!="1010":
                print("\nSem função")