import subprocess

def verificar_arquivos_corrompidos(log_callback=None):
    def log(msg):
        if log_callback:
            log_callback(msg)
        else:
            print(msg)

    log("🔍 Iniciando verificação de arquivos corrompidos...")

    try:
        # Executa o comando e captura a saída linha a linha
        process = subprocess.Popen("sfc /scannow", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
        for line in process.stdout:
            log(line.strip())

        process.stdout.close()
        retcode = process.wait()
        if retcode == 0:
            log("✅ Verificação concluída. Se foram encontrados arquivos corrompidos, eles foram reparados.")
        else:
            log(f"⚠️ Comando finalizado com código {retcode}. Verifique manualmente.")

    except Exception as e:
        log(f"❌ Erro ao executar a verificação: {e}")

if __name__ == "__main__":
    verificar_arquivos_corrompidos()
