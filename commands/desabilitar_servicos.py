import subprocess
from datetime import datetime

class ServicosController:
    def __init__(self):
        self.servicos = [
            "SessionEnv", "WpcMonSvc", "diagsvc", "DiagTrack", "XblAuthManager", "RasMan",
            "Netlogon", "pla", "workfolderssvc", "SCPolicySvc", "RemoteRegistry", "XblGameSave",
            "WbioSrvc", "BDESVC", "ScDeviceEnum", "lfsvc", "icssvc", "XboxNetApiSvc",
            "WerSvc", "PhoneSvc", "InventorySvc", "Sysmain", "XboxGipSvc",
            "Fax", "TabletInputService", "dmwappushservice", "MapsBroker",
            "diagnosticshub.standardcollector.service", "RetailDemo", "PcaSvc",
            "WMPNetworkSvc", "TrkWks", "DPS"
        ]

    def desabilitar_servicos(self, servicos_selecionados=None, log_callback=None):
        servicos = servicos_selecionados if servicos_selecionados is not None else self.servicos
        return self._alterar_estado_servicos(servicos, startup_type="Disabled", parar=True, log_callback=log_callback)

    def reativar_servicos(self, servicos_selecionados=None, log_callback=None):
        servicos = servicos_selecionados if servicos_selecionados is not None else self.servicos
        return self._alterar_estado_servicos(servicos, startup_type="Manual", parar=False, log_callback=log_callback)

    def _alterar_estado_servicos(self, servicos, startup_type, parar=True, log_callback=None):
        log = []
        for servico in servicos:
            try:
                if parar:
                    msg = f"Parando serviço: {servico}"
                    if log_callback:
                        log_callback(msg)
                    else:
                        print(msg)

                    subprocess.run(
                        ["powershell", "-Command", f"Stop-Service -Name '{servico}' -Force"],
                        check=True)

                msg = f"Configurando {servico} para StartupType {startup_type}"
                if log_callback:
                    log_callback(msg)
                else:
                    print(msg)

                subprocess.run(
                    ["powershell", "-Command", f"Set-Service -Name '{servico}' -StartupType {startup_type}"],
                    check=True)

                if not parar:
                    msg = f"Iniciando serviço: {servico}"
                    if log_callback:
                        log_callback(msg)
                    else:
                        print(msg)

                    subprocess.run(
                        ["powershell", "-Command", f"Start-Service -Name '{servico}'"],
                        check=True)

                sucesso = f"[OK] {servico} configurado para {startup_type}."
                if log_callback:
                    log_callback(sucesso)
                log.append(sucesso)

            except subprocess.CalledProcessError as e:
                erro = f"[ERRO] {servico}: {e}"
                if log_callback:
                    log_callback(erro)
                log.append(erro)
            except Exception as e:
                erro = f"[ERRO] {servico}: {e}"
                if log_callback:
                    log_callback(erro)
                log.append(erro)

        self._salvar_log(log)
        return log

    def _salvar_log(self, linhas_log):
        with open("log_servicos.txt", "a", encoding="utf-8") as f:
            f.write(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\n")
            for linha in linhas_log:
                f.write(linha + "\n")


# Instância única para funções globais
_sc = ServicosController()

def desabilitar_servicos(servicos_selecionados=None, log_callback=None):
    return _sc.desabilitar_servicos(servicos_selecionados, log_callback=log_callback)

def reativar_servicos(servicos_selecionados=None, log_callback=None):
    return _sc.reativar_servicos(servicos_selecionados, log_callback=log_callback)


if __name__ == "__main__":
    # Exemplo: imprime log em tempo real no console
    def imprimir_log(mensagem):
        print(mensagem)

    resultado_log = desabilitar_servicos(log_callback=imprimir_log)
    for linha in resultado_log:
        print(linha)
