import subprocess

def atualizar_softwares(log_callback=None):
    try:
        if log_callback:
            log_callback("Iniciando atualização de softwares desatualizados...")

        # Executa o winget upgrade --all com flags para aceitar acordos automaticamente
        processo = subprocess.Popen(
            ["winget", "upgrade", "--all", "--accept-source-agreements", "--accept-package-agreements"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
            universal_newlines=True,
            shell=True
        )

        for linha in processo.stdout:
            if log_callback:
                log_callback(linha.rstrip())

        processo.stdout.close()
        retorno = processo.wait()

        if retorno == 0:
            msg = "Atualização de softwares concluída com sucesso."
            if log_callback:
                log_callback(msg)
            return msg
        else:
            msg = f"Erro na atualização dos softwares. Código de saída: {retorno}"
            if log_callback:
                log_callback(msg)
            return msg

    except Exception as e:
        erro = f"Erro inesperado durante atualização: {e}"
        if log_callback:
            log_callback(erro)
        return erro

if __name__ == "__main__":
    atualizar_softwares()
