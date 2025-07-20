import subprocess
import re

def ativar_perfil_desempenho(log_callback=None):
    try:
        if log_callback:
            log_callback("Obtendo lista de perfis de energia disponíveis...")

        resultado = subprocess.run(['powercfg', '/list'], capture_output=True, text=True, check=True)
        
        guids = re.findall(r'([a-f0-9\-]{36})\s+\(.*\)', resultado.stdout, re.IGNORECASE)
        
        if not guids:
            msg = "Nenhum perfil de energia encontrado."
            if log_callback:
                log_callback(msg)
            return msg

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

        if log_callback:
            log_callback(msg)
            log_callback(f"Ativando o perfil {perfil_selecionado}...")

        subprocess.run(['powercfg', '/setactive', perfil_selecionado], check=True)

        sucesso_msg = "Perfil ativado com sucesso!"
        if log_callback:
            log_callback(sucesso_msg)
        return sucesso_msg

    except subprocess.CalledProcessError as e:
        erro_msg = f"Erro ao executar comando do sistema: {e}"
        if log_callback:
            log_callback(erro_msg)
        return erro_msg
    except Exception as e:
        erro_msg = f"Erro inesperado: {e}"
        if log_callback:
            log_callback(erro_msg)
        return erro_msg

if __name__ == "__main__":
    resultado = ativar_perfil_desempenho()
    print(resultado)
