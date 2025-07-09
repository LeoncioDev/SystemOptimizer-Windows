import subprocess

def verificar_disco():
    print("Iniciando verificação de disco...")

    # Executando o comando chkdsk /f /r e exibindo a saída no console
    subprocess.run("chkdsk /f /r", shell=True)
    
    print("Verificação de disco concluída.")

if __name__ == "__main__":
    verificar_disco()
