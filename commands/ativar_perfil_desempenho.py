import subprocess
import re

def ativar_perfil_desempenho():
    try:
        # Executa "powercfg /list" para obter os perfis disponíveis
        resultado = subprocess.run(['powercfg', '/list'], capture_output=True, text=True, check=True)
        
        # Expressão regular para extrair GUIDs dos perfis
        guids = re.findall(r'([a-f0-9\-]{36})\s+\(.*\)', resultado.stdout, re.IGNORECASE)
        
        if not guids:
            return "Nenhum perfil de energia encontrado."

        # Perfis conhecidos (padrão do Windows)
        perfil_alto_desempenho = "8c5e7fd6-6e8b-4f47-a3c5-c7c9be10dcf0"
        perfil_max_desempenho = "e9a42b02-d5df-448d-aa00-03f14749eb61"

        if perfil_max_desempenho in guids:
            perfil_selecionado = perfil_max_desempenho
            msg = "Ativando perfil: Desempenho Máximo"
        elif perfil_alto_desempenho in guids:
            perfil_selecionado = perfil_alto_desempenho
            msg = "Ativando perfil: Alto Desempenho"
        else:
            perfil_selecionado = guids[0]
            msg = f"Ativando perfil alternativo: {perfil_selecionado}"

        # Ativa o perfil selecionado
        subprocess.run(['powercfg', '/setactive', perfil_selecionado], check=True)
        return f"{msg} - Perfil ativado com sucesso!"

    except subprocess.CalledProcessError as e:
        return f"Erro ao executar comando do sistema: {e}"
    except Exception as e:
        return f"Erro inesperado: {e}"

if __name__ == "__main__":
    resultado = ativar_perfil_desempenho()
    print(resultado)
