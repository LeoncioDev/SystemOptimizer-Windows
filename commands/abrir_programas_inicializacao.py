import subprocess

def abrir_msconfig_servicos(log_callback=None):
    if log_callback:
        log_callback("Abrindo MSConfig...")
    try:
        subprocess.run("msconfig", shell=True, check=True)
        if log_callback:
            log_callback("MSConfig aberto com sucesso.")
    except subprocess.CalledProcessError as e:
        if log_callback:
            log_callback(f"Erro ao abrir MSConfig: {e}")

def abrir_taskmgr_servicos(log_callback=None):
    if log_callback:
        log_callback("Abrindo Gerenciador de Tarefas na aba 'Serviços'...")
    try:
        subprocess.run("taskmgr /0 /services", shell=True, check=True)
        if log_callback:
            log_callback("Gerenciador de Tarefas aberto com sucesso.")
    except subprocess.CalledProcessError as e:
        if log_callback:
            log_callback(f"Erro ao abrir Gerenciador de Tarefas: {e}")

def abrir_ferramenta_servicos(escolha="1", log_callback=None):
    """Chama a ferramenta escolhida; escolha: '1' = MSConfig, '2' = Task Manager."""
    if escolha == "1":
        abrir_msconfig_servicos(log_callback)
    elif escolha == "2":
        abrir_taskmgr_servicos(log_callback)
    else:
        if log_callback:
            log_callback("Opção inválida! Escolha '1' ou '2'.")
