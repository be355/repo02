D_of_Bat = {'Batalhão 1': [3500, 1500],'Batalhão 2': [3500, 1500],'Batalhão 3': [3500, 1500],'Batalhão 4': [3500, 1500]}
L_of_Mod = []
def show_bat() -> None:
    global D_of_Bat
    print('Lista dos Batalhões presentes:')
    print()
    print(f'{'Nome':15}    {'Não Dobradores':20}{'Dobradores':20}')
    L_of_Bat = list(D_of_Bat.keys())
    L_of_Bat.sort()
    for i in L_of_Bat:
        print(f'{i:15} => {D_of_Bat[i][0]:15}{D_of_Bat[i][1]:15}')
def add_bat() -> None:
    global D_of_Bat, L_of_Mod
    while True:
        print('''Digite "sair" para cancelar a operação''')
        nome = input('Insira o nome do Batalhão a ser adicionado:')
        if nome == 'sair':
            print('Operação cancelada.')
            return
        elif nome == '':
            print('Nome inválido.')
        elif nome in D_of_Bat:
            print('Batalhão já existe.')
        else:
            while True:
                num1 = input('Insira o número de não dobradores do Batalhão a ser adicionado:')
                if num1 == 'sair':
                    return
                elif num1 != '' and num1.isdigit():
                    num2 = input('Insira o número de dobradores do Batalhão a ser adicionado:')
                    if num2 == 'sair':
                        return
                    elif num2 != '' and num2.isdigit():
                        Lofnum = [int(num1), int(num2)]
                        D_of_Bat[nome] = Lofnum
                        L_of_Mod.append(('a', nome, num1, num2))
                        print('Operação Bem sucedida')
                        return
                    else:
                        print('Número inválido.')
                else:
                    print('Número inválido.')
def exclude_bat() -> None:
    global D_of_Bat, L_of_Mod
    print('Batalhões disponíveis para Exclusão:')
    L_of_Bat = list(D_of_Bat.keys())
    for i in L_of_Bat:
        print(i)
    print()
    while True:
        print('''Digite "sair" para cancelar a operação''')
        nome = input('Insira o nome do batalhão a ser removido:')
        if nome == 'sair':
            print('Operação cancelada.')
            return
        if nome != '':
            if nome in D_of_Bat:
                del D_of_Bat[nome]
                L_of_Mod.append(('e', nome))
                print('Operação Bem sucedida.')
                return
            else:
                print('Batalhão não encontrado.')   
        else:
            print('Nome inválido.')

def show_mod() -> None:
    global L_of_Mod
    if L_of_Mod == []:
        print('Nenhuma modificação registrada.')
        return
    else:
        print('Modificações Realizadas:')
        print()
        for i in L_of_Mod:
            ind = i[0]
            if ind == 'a':
                print(f'Adicionado: Batalhão: {i[1]}, Não Dobradores: {i[2]}, Dobradores: {i[3]}')
            if ind == 'e':
                print(f'Removido: Batalhão: {i[1]}')
            if ind == 'm':
                print(f'''Modificado: Batalhão: {i[1]}, Diferença de Não Dobradores: {i[2]}, Diferença de Dobradores: {i[3]}.
Observação adicionada: {i[4]}''')
def mod_bat() -> None:
    global D_of_Bat, L_of_Mod
    print('Batalhões disponíveis para modificação:')
    L_of_Bat = list(D_of_Bat.keys())
    for n in range(1,len(L_of_Bat)+1):
        print(f'{n}-{L_of_Bat[n-1]}')
    print()
    while True:
        print('Digite "sair" para cancelar a operação.')
        print()
        inp = input('Escolha o número do Batalhão a ser modificado:')
        if inp =='sair':
            print('Operação Cancelada.')
            return
        try:
            inp = int(inp)
            inp -= 1
        except:
            print('Valor inválido.')
            continue
        V_of_nd, V_of_d = D_of_Bat[L_of_Bat[inp]]            
        print(f'Batalhão Selecionado: {L_of_Bat[inp]}')
        print(f'Não Dobradores: {V_of_nd}, Dobradores: {V_of_d}')
        print()
        print('Digite "sair" para cancelar a operação.')
        while True:
            print('Digite o número de Não Dobradores a ser adicionado/removido:')
            print('Utilize "-" para remover.')
            inp_nd = input()
            if inp_nd =='sair':
                print('Operação Cancelada.')
                return
            else:
                try:
                    inp_nd = int(inp_nd)
                except:
                    print('Valor inválido.')
                    continue
                if V_of_nd + inp_nd < 0:
                    print('Número de Não Dobradores não pode ser negativo.')
                    continue
                print(f'Número de Não Dobradores Modificado: {V_of_nd + inp_nd}')
                print('Digite "sair" para cancelar a operação.')
                while True:
                    print('Digite o número de Dobradores a ser adicionado/removido:')
                    print('Utilize "-" para remover.')
                    inp_d = input()
                    if inp_d =='sair':
                        print('Operação Cancelada.')
                        return
                    else:
                        try:
                            inp_d = int(inp_d)
                        except:
                            print('Valor inválido.')
                            continue
                        if V_of_d + inp_d < 0:
                            print('Número de Dobradores não pode ser negativo.')
                            continue
                        print(f'Número de Dobradores Modificado: {V_of_d + inp_d}')
                        while True:
                            print('Digite a observação:')
                            inp_obs = input()
                            if inp_obs =='sair':
                                print('Operação Cancelada.')
                                return
                            else:
                                L_of_Mod.append(('m', L_of_Bat[inp], inp_nd, inp_d, inp_obs))
                                D_of_Bat[L_of_Bat[inp]] = [V_of_nd + inp_nd, V_of_d + inp_d]
                                print('Operação Bem sucedida.')
                                return

if __name__ == '__main__':
    while True:
        print('''
Menu:

1- Status dos Batalhões
2- Adicionar Batalhão
3- Remover batalhão
4- Modificar números do Batalhão
5- Mostrar Modificações

Digite "sair" para encerrar o programa''')
        i = input()
        print()
        if i == '1':
            show_bat()
        elif i == '2':
            add_bat()
        elif i == '3':
            exclude_bat()
        elif i == '4':
            mod_bat()
        elif i == '5':
            show_mod()
        elif i == 'sair':
            print('Programa encerrado.')
            break
        else:
            print('Opção não identificada')