import os
import subprocess
from getpass import getuser
from signal import signal, SIGINT
from time import sleep
from colorama import Fore, Back, init

init()

class LaravelCLI():
    def __init__(self):
        os.system('clear')
        self.banner()
    
    def handler(signal_received, frame):
        print("\n")
        resInput = input("Se precionó Ctrl+c. ¿Desea terminar Laravel CLI ahora? y/n: ")
        if (resInput == 'y'):
            print(Back.RED + Fore.WHITE + "\n Saliendo de la aplicaicón " + Fore.RESET + Back.RESET)
            os.system('clear')
            exit(0)

    signal(SIGINT, handler)

    def banner(self):
        print(Fore.RED)
        print(' _                               _   _____  _     _____ ')
        print('| |                             | | /  __ \| |   |_   _|')
        print('| |     __ _ _ __ __ ___   _____| | | /  \/| |     | |  ')
        print("| |    / _` | '__/ _` \ \ / / _ \ | | |    | |     | |  ")
        print('| |___| (_| | | | (_| |\ V /  __/ | | \__/\| |_____| |_ ')
        print('\_____/\__,_|_|  \__,_| \_/ \___|_|  \____/\_____/\___/')
        print('\t\t\tBy WH117' + Fore.RESET)
        self.checkLaravelVersion()
        self.createData()
    
    def checkLaravelVersion(self):
        self.usuario = getuser()
        self.route = input("Raíz del proyecto: ")
        self.route = "php /home/" + self.usuario + "/" + self.route + "/artisan"
        #subprocess.Popen("php /home/" + self.usuario + "/" + self.route + "/artisan --version | grep 'Laravel Framework' | awk '{print $3}'", shell=True).wait()
        os.system(self.route + " --version | grep 'Laravel Framework' | awk '{print $3}'")
        res = input("Desea crear migraciones, modelos y controladores? Y/N: ")
        if (res == 'Y'):
            self.createData()
        else:
            exit(0)

    def createData(self):
        self.data = input("Entidad: ")
        os.system(self.route + " make:migration create" + self.data + "_table")
        os.system(self.route + " make:model " + self.data + "Model")
        os.system(self.route + " make:controller " + self.data + "Controller")
        res = input("Desea crear mas entidades? Y/N=> ")
        if (res == 'Y'):
            self.createData()
        else:
            exit(0)

if __name__ == '__main__':
    lc = LaravelCLI()
