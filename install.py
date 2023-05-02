import os
from colorama import Fore, Back, init

init()

def init_install(self):
    self.route_install = "/home/" + self.get_user + "/Documentos"
    print(Fore.RED + "Inicializando instalación" + Fore.RESET)

init_install(self = "")
