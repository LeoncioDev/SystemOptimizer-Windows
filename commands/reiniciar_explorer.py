import os
import time

def reiniciar_explorer():
    print("Reiniciando o Windows Explorer...")

    # Finalizar o processo do Windows Explorer
    os.system("taskkill /f /im explorer.exe")
    
    # Aguardar um momento para garantir que o processo foi finalizado
    time.sleep(2)
    
    # Iniciar o Windows Explorer novamente
    os.system("start explorer.exe")
    
    print("Windows Explorer reiniciado com sucesso.")

if __name__ == "__main__":
    reiniciar_explorer()
