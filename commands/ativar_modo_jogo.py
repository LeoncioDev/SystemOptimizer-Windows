import subprocess

def ativar_modo_jogo():
    try:
        # Abrir diretamente as configurações do Modo de Jogo no Windows 10/11
        subprocess.run(["cmd", "/c", "start ms-settings:gaming-gamemode"], shell=True)
        print("Abrindo diretamente as configurações do Modo de Jogo...")

    except Exception as e:
        print(f"Erro ao ativar o Modo de Jogo: {e}")
