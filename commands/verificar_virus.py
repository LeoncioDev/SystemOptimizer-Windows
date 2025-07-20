import subprocess

def verificar_virus(log_callback=None):
    def log(msg):
        if log_callback:
            log_callback(msg)
        else:
            print(msg)

    log("🛡️ Iniciando verificação de vírus...")

    try:
        # Executa a ferramenta de remoção de malware (Malicious Software Removal Tool) com interface gráfica
        comando = "mrt"
        subprocess.run(comando, shell=True, check=True)
        log("✅ Verificação concluída. Se foram encontrados vírus, a ferramenta irá removê-los automaticamente.")
    except subprocess.CalledProcessError as e:
        log(f"❌ Erro durante a verificação de vírus: {e}")
    except Exception as e:
        log(f"❌ Erro inesperado: {e}")

if __name__ == "__main__":
    verificar_virus()
