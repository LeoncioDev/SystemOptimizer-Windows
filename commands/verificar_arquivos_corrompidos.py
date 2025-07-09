import subprocess

def verificar_arquivos_corrompidos():
    print("Iniciando verificação de arquivos corrompidos...")
    
    # Executando o comando sfc /scannow e exibindo a saída no console
    subprocess.run("sfc /scannow", shell=True)
    
    print("Verificação concluída. Se foram encontrados arquivos corrompidos, eles foram reparados.")

if __name__ == "__main__":
    verificar_arquivos_corrompidos()
