import subprocess
import re

def ativar_perfil_desempenho():
    try:
        # Executa "powercfg /list" para obter os perfis disponíveis
        resultado = subprocess.run(['powercfg', '/list'], capture_output=True, text=True)

        # Expressão regular para encontrar GUIDs dos perfis
        guids = re.findall(r'([a-f0-9\-]+)  \(.+\)', resultado.stdout, re.IGNORECASE)

        if not guids:
            print("Nenhum perfil de energia encontrado.")
            return

        print("Perfis disponíveis:", guids)

        # Perfis conhecidos
        perfil_alto_desempenho = "8c5e7fd6-6e8b-4f47-a3c5-c7c9be10dcf0"
        perfil_max_desempenho = "e9a42b02-d5df-448d-aa00-03f14749eb61"

        # Verifica se "Desempenho Máximo" está disponível
        if perfil_max_desempenho in guids:
            perfil_selecionado = perfil_max_desempenho
            print("Ativando perfil: Desempenho Máximo")
        elif perfil_alto_desempenho in guids:
            perfil_selecionado = perfil_alto_desempenho
            print("Ativando perfil: Alto Desempenho")
        else:
            # Se nenhum dos dois estiver disponível, pega o primeiro da lista
            perfil_selecionado = guids[0]
            print(f"Ativando perfil alternativo: {perfil_selecionado}")

        # Ativa o perfil selecionado
        subprocess.run(['powercfg', '/setactive', perfil_selecionado], check=True)
        print("Perfil de desempenho ativado com sucesso!")

    except subprocess.CalledProcessError as e:
        print(f"Erro ao tentar ativar o perfil de desempenho: {e}")

if __name__ == "__main__":
    ativar_perfil_desempenho()
