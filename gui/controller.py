import traceback
from PyQt6.QtCore import QObject, pyqtSignal, QThread

from commands.ajustar_mouse import otimizar_mouse_teclado
from commands.ativar_modo_jogo import ativar_modo_jogo
from commands.ativar_perfil_desempenho import ativar_perfil_desempenho
from commands.atualizar_softwares import atualizar_softwares
from commands.desabilitar_servicos import desativar_servicos
from commands.desativar_efeitos_visuais import desativar_efeitos_visuais
from commands.reiniciar_explorer import reiniciar_explorer
from commands.verificar_arquivos_corrompidos import verificar_arquivos_corrompidos
from commands.verificar_disco import verificar_disco
from commands.verificar_virus import verificar_virus
from commands.limpar_temp import limpar_temporarios

class WorkerThread(QThread):
    finished = pyqtSignal(str)
    error = pyqtSignal(str)

    def __init__(self, func, success_msg="Ação concluída com sucesso!"):
        super().__init__()
        self.func = func
        self.success_msg = success_msg

    def run(self):
        try:
            self.func()
            self.finished.emit(self.success_msg)
        except Exception as e:
            tb = traceback.format_exc()
            self.error.emit(f"{e}\n{tb}")

class Controller(QObject):
    def __init__(self):
        super().__init__()

    def limpar_temporarios(self):
        limpar_temporarios()

    def desabilitar_servicos(self):
        desativar_servicos()

    def ativar_perfil_desempenho(self):
        ativar_perfil_desempenho()

    def ativar_modo_jogo(self):
        ativar_modo_jogo()

    def ajustar_mouse(self):
        otimizar_mouse_teclado()

    def verificar_virus(self):
        verificar_virus()

    def verificar_arquivos_corrompidos(self):
        verificar_arquivos_corrompidos()

    def verificar_disco(self):
        verificar_disco()

    def atualizar_softwares(self):
        atualizar_softwares()

    def overclock(self):
        raise NotImplementedError("Função de overclock ainda não implementada.")

    def desativar_efeitos_visuais(self):
        desativar_efeitos_visuais()

    def reiniciar_explorer(self):
        reiniciar_explorer()
