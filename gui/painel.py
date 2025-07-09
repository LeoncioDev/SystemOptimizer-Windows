# gui/painel.py
import subprocess
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QGroupBox, QPushButton, QScrollArea
from utils.helpers import show_error, safe_action

# Imports dos comandos
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
from commands.limpar_temp import limpar_temporarios as executar_limpeza_temp

def abrir_programas_inicializacao():
    try:
        subprocess.run("taskmgr /0 /startup", shell=True)
    except Exception as e:
        show_error(f"Erro ao abrir a tela de inicialização: {e}")

class PainelOtimizador(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Painel de Otimização do Sistema")
        self.setGeometry(100, 100, 600, 600)

        main_layout = QVBoxLayout()

        title_label = QLabel("</>LeoncioDev | Transformando ideias em código</>")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        main_layout.addWidget(title_label)

        main_layout.addWidget(self.criar_grupo_otimizacoes_gerais())
        main_layout.addWidget(self.criar_grupo_jogos())
        main_layout.addWidget(self.criar_grupo_manutencao())
        main_layout.addWidget(self.criar_grupo_extra())

        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)
        scroll_layout.addLayout(main_layout)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(scroll_widget)

        final_layout = QVBoxLayout()
        final_layout.addWidget(scroll_area)
        self.setLayout(final_layout)

    def criar_grupo_otimizacoes_gerais(self):
        group = QGroupBox("🔧 Otimizações Gerais")
        layout = QVBoxLayout()
        layout.addWidget(self.criar_botao("✅ Limpar Arquivos Temporários", self.limpar_temporarios))
        layout.addWidget(self.criar_botao("✅ Desativar Serviços Inúteis", self.desabilitar_servicos))
        layout.addWidget(self.criar_botao("✅ Ativar Perfil de Desempenho Máximo", self.ativar_perfil_desempenho))
        group.setLayout(layout)
        return group

    def criar_grupo_jogos(self):
        group = QGroupBox("🔥 Otimizações para Jogos")
        layout = QVBoxLayout()
        layout.addWidget(self.criar_botao("🎮 Ativar Modo de Jogo", self.ativar_modo_jogo))
        layout.addWidget(self.criar_botao("🎮 Ajustar Mouse e Teclado", self.ajustar_mouse))
        layout.addWidget(self.criar_botao("🚀 Desabilitar Programas de Inicialização", abrir_programas_inicializacao))
        group.setLayout(layout)
        return group

    def criar_grupo_manutencao(self):
        group = QGroupBox("🛠️ Manutenção do Sistema")
        layout = QVBoxLayout()
        layout.addWidget(self.criar_botao("🔍 Verificação de Vírus", self.verificar_virus))
        layout.addWidget(self.criar_botao("🔍 Verificar Arquivos Corrompidos", self.verificar_arquivos_corrompidos))
        layout.addWidget(self.criar_botao("🔍 Verificar Disco", self.verificar_disco))
        layout.addWidget(self.criar_botao("🔍 Atualização de Softwares", self.atualizar_softwares))
        group.setLayout(layout)
        return group

    def criar_grupo_extra(self):
        group = QGroupBox("🚀 Extra (Para Usuários Avançados)")
        layout = QVBoxLayout()
        layout.addWidget(self.criar_botao("⚡ Overclock Seguro", self.overclock))
        layout.addWidget(self.criar_botao("⚡ Desativar Efeitos Visuais", self.desativar_efeitos_visuais))
        layout.addWidget(self.criar_botao("⚡ Reiniciar Windows Explorer", self.reiniciar_explorer))
        group.setLayout(layout)
        return group

    def criar_botao(self, texto, funcao):
        botao = QPushButton(texto)
        botao.clicked.connect(funcao)
        return botao

    # === AÇÕES COM DECORADOR DE SUCESSO ===

    @safe_action("Limpeza de arquivos temporários concluída.")
    def limpar_temporarios(self):
        executar_limpeza_temp()

    @safe_action("Serviços inúteis desabilitados.")
    def desabilitar_servicos(self):
        desativar_servicos()

    @safe_action("Perfil de desempenho ativado.")
    def ativar_perfil_desempenho(self):
        ativar_perfil_desempenho()

    @safe_action("Modo Jogo ativado.")
    def ativar_modo_jogo(self):
        ativar_modo_jogo()

    @safe_action("Mouse e teclado otimizados.")
    def ajustar_mouse(self):
        otimizar_mouse_teclado()

    @safe_action("Verificação de vírus concluída.")
    def verificar_virus(self):
        verificar_virus()

    @safe_action("Verificação de arquivos concluída.")
    def verificar_arquivos_corrompidos(self):
        verificar_arquivos_corrompidos()

    @safe_action("Verificação de disco concluída.")
    def verificar_disco(self):
        verificar_disco()

    @safe_action("Atualização de softwares concluída.")
    def atualizar_softwares(self):
        atualizar_softwares()

    @safe_action("Nada será feito 😅 (sério mesmo?)")
    def overclock(self):
        pass

    @safe_action("Efeitos visuais desativados.")
    def desativar_efeitos_visuais(self):
        desativar_efeitos_visuais()

    @safe_action("Windows Explorer reiniciado.")
    def reiniciar_explorer(self):
        reiniciar_explorer()
