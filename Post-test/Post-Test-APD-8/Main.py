
from Autentifikasi import login
from Manajemen_film import menu_utama
import os
from time import sleep

if __name__ == "__main__":
    login()
    menu_utama()
    
    sleep(1)
    os.system("cls" if os.name == "nt" else "clear")