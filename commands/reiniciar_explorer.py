import os
import time

def reiniciar_explorer(log_callback=None):
    def log(msg):
        if log_callback:
            log_callback(msg)
        else:
            print(msg)

    try:
        log("🛠️ Reiniciando o Windows Explorer...")

        # Finalizar o processo do Windows Explorer
        ret_kill = os.system("taskkill /f /im explorer.exe")
        if ret_kill == 0:
            log("✔️ Processo explorer.exe finalizado.")
        else:
            log(f"⚠️ Falha ao finalizar explorer.exe (código {ret_kill}), talvez não estava rodando.")

        # Aguardar um momento para garantir que o processo foi finalizado
        time.sleep(2)

        # Iniciar o Windows Explorer novamente
        ret_start = os.system("start explorer.exe")
        if ret_start == 0:
            log("✔️ Windows Explorer iniciado com sucesso.")
        else:
            log(f"⚠️ Falha ao iniciar o Windows Explorer (código {ret_start}).")

        log("✅ Reinício do Windows Explorer concluído com sucesso.")

    except Exception as e:
        log(f"❌ Erro ao reiniciar o Windows Explorer: {e}")

if __name__ == "__main__":
    reiniciar_explorer()
