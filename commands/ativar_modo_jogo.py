import subprocess

def ativar_modo_jogo(log_callback=None):
    try:
        if log_callback:
            log_callback("Abrindo diretamente as configurações do Modo de Jogo...")
        subprocess.run(["cmd", "/c", "start ms-settings:gaming-gamemode"], shell=True)
    except Exception as e:
        if log_callback:
            log_callback(f"Erro ao ativar o Modo de Jogo: {e}")
        else:
            raise
