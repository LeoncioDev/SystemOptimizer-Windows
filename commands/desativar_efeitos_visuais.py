import subprocess
import os

def desativar_efeitos_visuais(log_callback=None):
    def log(msg):
        if log_callback:
            log_callback(msg)
        else:
            print(msg)
    try:
        path = os.path.join(os.environ['WINDIR'], 'System32', 'SystemPropertiesPerformance.exe')
        subprocess.Popen([path])
        log("Janela de configurações de desempenho aberta.")
    except Exception as e:
        log(f"Erro ao abrir configurações: {e}")
