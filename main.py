from string import ascii_lowercase

lista = ascii_lowercase

def crip(text='', letras='', base=3):
        from unidecode import unidecode

        text = unidecode(text.strip().lower())
        crip = str()

        for i in text:
                if not i in letras and i != ' ':
                        continue
                try:
                        crip += i if i == ' ' else letras[letras.index(i) + base]
                except:
                        crip += letras[(letras.index(i) + base) - 26]
        return crip


def descrip(crip='', letras='', base=3):
        crip = crip.strip().lower()
        texto = str()
        for i in crip:
                texto += i if i == ' ' else letras[letras.index(i) - base]
        return texto


vr = '\033[32;1m'
f = '\033[37;1m'
n = '\033[1m'

banner = f'''{vr}   ______   _    ____
  / ____/  (_)  / __/  _____   ____ _
 / /      / /  / /_   / ___/  / __ `/
/ /___   / /  / __/  / /     / /_/ /
\____/  /_/  /_/    /_/      \__,_/{f}'''

per = 's'
while per == 's':
        print('\x1b[2J\x1b[1;1H')
        print(banner)
        try:
                rsp = input(f'\n{n}[ {vr}1{f} ] > {vr}Criptografar{f}\n[ {vr}2{f} ] > {vr}Descriptografar{f}\n\n[ {vr}0{f} ] {vr}Sair\n\n>>>{f} ').strip()[0]
        except:
                continue
        if rsp == '0': break
        if not rsp in '120': continue
        try:
                b = int(input(f"Digite a base: (\033[33;1menter para padrão{f}) "))
        except:
                b = 3
        match rsp:
                case '1':
                        texto = input('Texto para criptografar: \033[4;1m').strip().lower()
                        print(f'\033[m{f}Seu texto: {vr}{crip(texto, lista, b)}{f}')
                case '2':
                        crip = input('Texto para descriptografar: \033[1;4m').strip().lower()
                        print(f'\033[m{f}Seu texto: {vr}{descrip(crip, lista, b)}{f}')
        per = input('Deseja voltar? [s/n] ').strip().lower()[0]
