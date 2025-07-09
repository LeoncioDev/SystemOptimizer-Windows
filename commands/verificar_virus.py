import subprocess

def verificar_virus():
    print("Iniciando verificação de vírus...")

    # Comando para rodar a ferramenta de remoção de malware (com interface gráfica)
    comando = "mrt"  # Comando sem a opção /scan, para abrir a interface gráfica

    # Executa o comando
    subprocess.run(comando, shell=True)

    print("Verificação concluída. Se foram encontrados vírus, a ferramenta irá removê-los automaticamente.")

if __name__ == "__main__":
    verificar_virus()
