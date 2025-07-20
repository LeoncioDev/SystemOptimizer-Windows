import subprocess

def verificar_disco(log_callback=None):
    def log(msg):
        if log_callback:
            log_callback(msg)
        else:
            print(msg)

    log("🔍 Iniciando verificação de disco...")

    try:
        # Rodar chkdsk com flags de correção e recuperação de setores
        process = subprocess.Popen("chkdsk /f /r", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)

        for line in process.stdout:
            log(line.strip())

        process.stdout.close()
        retcode = process.wait()

        if retcode == 0:
            log("✅ Verificação de disco concluída com sucesso.")
        else:
            log(f"⚠️ Comando finalizado com código {retcode}. Verifique manualmente.")

    except Exception as e:
        log(f"❌ Erro ao executar a verificação de disco: {e}")

if __name__ == "__main__":
    verificar_disco()
