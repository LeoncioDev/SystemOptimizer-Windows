from PyQt6.QtCore import QObject, pyqtSignal, QThread
import traceback

from commands.ajustar_mouse import otimizar_mouse_teclado
from commands.ativar_modo_jogo import ativar_modo_jogo
from commands.ativar_perfil_desempenho import ativar_perfil_desempenho
from commands.atualizar_softwares import atualizar_softwares
from commands.desabilitar_servicos import ServicosController
from commands.desativar_efeitos_visuais import desativar_efeitos_visuais
from commands.reiniciar_explorer import reiniciar_explorer
from commands.verificar_arquivos_corrompidos import verificar_arquivos_corrompidos
from commands.verificar_disco import verificar_disco
from commands.verificar_virus import verificar_virus
from commands.limpar_temp import limpar_temporarios

# Import da função que verifica dependências
from commands.verificar_dependencias import verificar_dependencias  # ajuste o caminho se necessário

class WorkerThread(QThread):
    finished = pyqtSignal(str)
    error = pyqtSignal(str)
    log_signal = pyqtSignal(str)

    def __init__(self, func, success_msg="Ação concluída com sucesso!"):
        super().__init__()
        self.func = func
        self.success_msg = success_msg

    def run(self):
        try:
            def log_callback(msg):
                self.log_signal.emit(msg)

            self.log_signal.emit("➡️ Iniciando execução da função...")

            resultado = self.func(log_callback)

            if resultado:
                self.log_signal.emit(str(resultado))
            else:
                self.log_signal.emit("✔️ Ação executada sem retorno.")

            self.finished.emit(self.success_msg)

        except Exception as e:
            tb = traceback.format_exc()
            self.error.emit(f"❌ Erro ao executar a função:\n{e}\n\n{tb}")

class Controller(QObject):
    def __init__(self):
        super().__init__()
        self.servicos_controller = ServicosController()

    # Serviços
    def obter_lista_servicos(self):
        return self.servicos_controller.servicos

    def desabilitar_servicos(self, lista_selecionada=None, log_callback=None):
        if lista_selecionada is None:
            lista_selecionada = self.servicos_controller.servicos
        return self.servicos_controller.desabilitar_servicos(lista_selecionada, log_callback=log_callback)

    def reativar_servicos(self, lista_selecionada=None, log_callback=None):
        if lista_selecionada is None:
            lista_selecionada = self.servicos_controller.servicos
        return self.servicos_controller.reativar_servicos(lista_selecionada, log_callback=log_callback)

    # Ações gerais
    def limpar_temporarios(self, log_callback=None):
        return limpar_temporarios(log_callback=log_callback)

    def ativar_perfil_desempenho(self, log_callback=None):
        return ativar_perfil_desempenho(log_callback=log_callback)

    def ativar_modo_jogo(self, log_callback=None):
        return ativar_modo_jogo(log_callback=log_callback)

    def ajustar_mouse(self, log_callback=None):
        return otimizar_mouse_teclado(log_callback=log_callback)

    def verificar_virus(self, log_callback=None):
        return verificar_virus(log_callback=log_callback)

    def verificar_arquivos_corrompidos(self, log_callback=None):
        return verificar_arquivos_corrompidos(log_callback=log_callback)

    def verificar_disco(self, log_callback=None):
        return verificar_disco(log_callback=log_callback)

    def atualizar_softwares(self, log_callback=None):
        return atualizar_softwares(log_callback=log_callback)

    # NOVO método para verificar dependências para jogos
    def verificar_dependencias_jogos(self, log_callback=None):
        return verificar_dependencias(log_callback=log_callback)


    def desativar_efeitos_visuais(self, log_callback=None):
        return desativar_efeitos_visuais(log_callback=log_callback)

    def reiniciar_explorer(self, log_callback=None):
        return reiniciar_explorer(log_callback=log_callback)
