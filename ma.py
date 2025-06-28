import os
from pystyle import Colors, Colorate

def main():
    while True:
        os.system("cls")
        print(Colorate.Diagonal(Colors.blue_to_purple, """
         ██████╗ ██████╗ ███╗   ███╗██████╗                 
        ██╔════╝██╔═══██╗████╗ ████║██╔══██╗                
        ██║     ██║   ██║██╔████╔██║██████╔╝                
        ██║     ██║   ██║██║╚██╔╝██║██╔═══╝                 
        ╚██████╗╚██████╔╝██║ ╚═╝ ██║██║                     
        ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝                     
                                                    
███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗ 
████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝
██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗
██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
╔══════════════════════════════════════════════════╗
║##################################################║ 
║#  1:перезагружить        2:диспечер задачб      #║ 
║#                                                #║ 
║#  3:проводник            4:регэдит              #║ 
║#                                                #║ 
║#  5:дисп устойвств     6:заменить cmd  на ps    #║ 
║#                                                #║ 
║#                 99:выход                       #║ 
║#                                                #║                                                                                                                        
║################# By taylor ######################║                        
╚══════════════════════════════════════════════════╝"""))

        choice = input(Colorate.Diagonal(Colors.blue_to_purple, "выбери: "))

        if choice == "1":
            os.system("shutdown -r -t 0")
            os.system("shutdown -r -t 0")
        elif choice == "2":
            print(Colorate.Diagonal(Colors.blue_to_purple, "готово!"))
            os.system("taskmgr.exe")
            print(Colorate.Diagonal(Colors.blue_to_purple, "готово!"))
        elif choice == "3":
            os.system("explorer.exe")
            print(Colorate.Diagonal(Colors.blue_to_purple, "готово!"))
        elif choice == "4":
            os.system("regedit")
            print(Colorate.Diagonal(Colors.blue_to_purple, "готово!"))
        elif choice == "5":
            os.system("devmgmt.msc")
            print(Colorate.Diagonal(Colors.blue_to_purple, "готово!"))
        elif choice == "6":
            os.system("powershell")
            exit()
            print(Colorate.Diagonal(Colors.blue_to_purple, "готово!"))
        elif choice == "99":
            exit()
        else:
            exit()

if __name__ == "__main__":
    main()