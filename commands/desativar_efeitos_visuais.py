import subprocess

def desativar_efeitos_visuais():
    try:
        # Executa o comando para abrir as configurações de desempenho do Windows
        subprocess.run('SystemPropertiesPerformance', check=True)
        
        # Desmarcar a opção de "Ajustar para obter o melhor desempenho"
        # No caso, apenas ajustando a performance para a configuração ideal
        print("Desabilitando efeitos visuais...")

        # Comando do PowerShell para desabilitar os efeitos visuais
        subprocess.run(
            'powershell -Command "Set-ItemProperty -Path \'HKCU:\\Control Panel\\Desktop\' -Name UserPreferencesMask -Value 90"'
        )

        print("Efeitos visuais desativados com sucesso!")
    
    except subprocess.CalledProcessError as e:
        print(f"Erro ao tentar desabilitar os efeitos visuais: {e}")

# Executa a função
if __name__ == "__main__":
    desativar_efeitos_visuais()
