import os

def atualizar_softwares():
    print("Atualizando softwares desatualizados...")

    # Comando para atualizar todos os aplicativos instalados via winget
    os.system("winget upgrade --all")

    print("Atualização de softwares concluída.")

if __name__ == "__main__":
    atualizar_softwares()
