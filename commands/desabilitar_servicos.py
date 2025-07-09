import subprocess

# Lista de serviços a serem desativados
servicos = [
    "SessionEnv", "WpcMonSvc", "diagsvc", "DiagTrack", "XblAuthManager", "RasMan",
    "Netlogon", "pla", "workfolderssvc", "SCPolicySvc", "RemoteRegistry", "XblGameSave",
    "WbioSrvc", "BDESVC", "ScDeviceEnum", "lfsvc", "icssvc", "XboxNetApiSvc",
    "WerSvc", "PhoneSvc", "InventorySvc", "Sysmain", "XboxGipSvc"
]

def desativar_servicos():
    for servico in servicos:
        print(f"Desativando e parando serviço: {servico}")
        try:
            # Comando para parar o serviço
            subprocess.run(["powershell", "-Command", f"Stop-Service -Name {servico} -Force"], check=True)
            # Comando para desativar o serviço (modo de inicialização desativado)
            subprocess.run(["powershell", "-Command", f"Set-Service -Name {servico} -StartupType Disabled"], check=True)
            print(f"{servico} desativado com sucesso!")
        except subprocess.CalledProcessError as e:
            print(f"Erro ao desativar {servico}: {e}")
        except Exception as e:
            print(f"Erro inesperado ao desativar {servico}: {e}")

if __name__ == "__main__":
    desativar_servicos()
