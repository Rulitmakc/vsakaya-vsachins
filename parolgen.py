import random
from pystyle import Colors, Colorate
import os
print(Colorate.Horizontal(Colors.green_to_blue,"брасай кубек"))
cubik = random.randint(0,6)
print( cubik)

let = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
sum = "~!@#$%^&*()_+-=,./<>?;:"
cif ="1234567890"
def main():
    print(Colorate.Vertical(Colors.cyan_to_blue, """
         ██████╗  █████╗ ██████╗  ██████╗ ██╗          ██████╗ ███████╗███╗   ██╗
         ██╔══██╗██╔══██╗██╔══██╗██╔═══██╗██║         ██╔════╝ ██╔════╝████╗  ██║
         ██████╔╝███████║██████╔╝██║   ██║██║         ██║  ███╗█████╗  ██╔██╗ ██║
         ██╔═══╝ ██╔══██║██╔══██╗██║   ██║██║         ██║   ██║██╔══╝  ██║╚██╗██║
         ██║     ██║  ██║██║  ██║╚██████╔╝███████╗    ╚██████╔╝███████╗██║ ╚████║
         ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝
                            """))
    print(Colorate.Horizontal(Colors.blue_to_purple, "пароль =>  "))

print(Colorate.Vertical(Colors.cyan_to_blue, """
         ██████╗  █████╗ ██████╗  ██████╗ ██╗          ██████╗ ███████╗███╗   ██╗
         ██╔══██╗██╔══██╗██╔══██╗██╔═══██╗██║         ██╔════╝ ██╔════╝████╗  ██║
         ██████╔╝███████║██████╔╝██║   ██║██║         ██║  ███╗█████╗  ██╔██╗ ██║
         ██╔═══╝ ██╔══██║██╔══██╗██║   ██║██║         ██║   ██║██╔══╝  ██║╚██╗██║
         ██║     ██║  ██║██║  ██║╚██████╔╝███████╗    ╚██████╔╝███████╗██║ ╚████║
         ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝
       ╔══════════════════════════════════╗
       ║#                                #║
       ║#        [1]:generator           #║
       ║#         99 выход               #║
       ║##############PRO-V1##############║
       ╚══════════════════════════════════╝"""))
choice = input(Colorate.Horizontal(Colors.cyan_to_blue, "=> "))
if choice == "1":
    print(Colorate.Horizontal(Colors.green_to_cyan, "-генератор паролей"))
    dlina = input(Colorate.Horizontal(Colors.cyan_to_blue, "выдите длинну: "))
    un = input(Colorate.Horizontal(Colors.cyan_to_blue, "использовать цифры? да/нет: "))
    us = input(Colorate.Horizontal(Colors.cyan_to_blue, "использовать символы да/нет: "))
    chars = let

    if (un == "да"):
        chars += cif

    if (us == "да"):
        chars += sum
    password = ""
    for  i in range (int(dlina)):
        r_char = random.choice(chars)
        password += r_char
        os.system("cls")
        main()
        print(password)

elif choice == "99":
    exit()

else:
    exit()