from PyQt6.QtCore import Qt, QFile, QTextStream
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QGroupBox, QPushButton,
    QScrollArea, QMessageBox
)
from .controller import Controller, WorkerThread


class PainelOtimizador(QWidget):
    def __init__(self):
        super().__init__()
        self.controller = Controller()
        self.setWindowTitle("Painel de Otimização do Sistema")
        self.setGeometry(100, 100, 600, 600)

        self.main_layout = QVBoxLayout()

        # Título com objectName para aplicar no QSS
        self.title_label = QLabel("</>LeoncioDev | Transformando ideias em código</>")
        self.title_label.setObjectName("titleLabel")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.title_label)

        self.main_layout.addWidget(self.criar_grupo_otimizacoes_gerais())
        self.main_layout.addWidget(self.criar_grupo_jogos())
        self.main_layout.addWidget(self.criar_grupo_manutencao())
        self.main_layout.addWidget(self.criar_grupo_extra())

        # Status label com objectName para QSS
        self.status_label = QLabel("")
        self.status_label.setObjectName("statusLabel")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.status_label)

        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)
        scroll_layout.addLayout(self.main_layout)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(scroll_widget)

        final_layout = QVBoxLayout()
        final_layout.addWidget(scroll_area)
        self.setLayout(final_layout)

        self.set_style_from_file()  # Carrega o QSS para estilizar o painel

    def set_style_from_file(self):
        qss_file = QFile("gui/style.qss")
        if qss_file.open(QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text):
            stream = QTextStream(qss_file)
            qss = stream.readAll()
            self.setStyleSheet(qss)
            qss_file.close()
        else:
            print("Erro: Não foi possível abrir o arquivo style.qss")

    def criar_grupo_otimizacoes_gerais(self):
        group = QGroupBox("🔧 Otimizações Gerais")
        layout = QVBoxLayout()
        layout.addWidget(self.criar_botao("✅ Limpar Arquivos Temporários", self.controller.limpar_temporarios, "Limpeza de arquivos temporários concluída."))
        layout.addWidget(self.criar_botao("✅ Desativar Serviços Inúteis", self.controller.desabilitar_servicos, "Serviços inúteis desabilitados."))
        layout.addWidget(self.criar_botao("✅ Ativar Perfil de Desempenho Máximo", self.controller.ativar_perfil_desempenho, "Perfil de desempenho ativado."))
        group.setLayout(layout)
        return group

    def criar_grupo_jogos(self):
        group = QGroupBox("🔥 Otimizações para Jogos")
        layout = QVBoxLayout()
        layout.addWidget(self.criar_botao("🎮 Ativar Modo de Jogo", self.controller.ativar_modo_jogo, "Modo Jogo ativado."))
        layout.addWidget(self.criar_botao("🎮 Ajustar Mouse e Teclado", self.controller.ajustar_mouse, "Mouse e teclado otimizados."))
        group.setLayout(layout)
        return group

    def criar_grupo_manutencao(self):
        group = QGroupBox("🛠️ Manutenção do Sistema")
        layout = QVBoxLayout()
        layout.addWidget(self.criar_botao("🔍 Verificação de Vírus", self.controller.verificar_virus, "Verificação de vírus concluída."))
        layout.addWidget(self.criar_botao("🔍 Verificar Arquivos Corrompidos", self.controller.verificar_arquivos_corrompidos, "Verificação de arquivos concluída."))
        layout.addWidget(self.criar_botao("🔍 Verificar Disco", self.controller.verificar_disco, "Verificação de disco concluída."))
        layout.addWidget(self.criar_botao("🔍 Atualização de Softwares", self.controller.atualizar_softwares, "Atualização de softwares concluída."))
        group.setLayout(layout)
        return group

    def criar_grupo_extra(self):
        group = QGroupBox("🚀 Extra (Para Usuários Avançados)")
        layout = QVBoxLayout()
        layout.addWidget(self.criar_botao("⚡ Overclock Seguro", self.controller.overclock, "Nada será feito 😅 (sério mesmo?)"))
        layout.addWidget(self.criar_botao("⚡ Desativar Efeitos Visuais", self.controller.desativar_efeitos_visuais, "Efeitos visuais desativados."))
        layout.addWidget(self.criar_botao("⚡ Reiniciar Windows Explorer", self.controller.reiniciar_explorer, "Windows Explorer reiniciado."))
        group.setLayout(layout)
        return group

    def criar_botao(self, texto, funcao, msg_sucesso):
        botao = QPushButton(texto)
        botao.setObjectName("actionButton")  # Para estilo QSS
        botao.clicked.connect(lambda: self.executar_acao(botao, funcao, msg_sucesso))
        return botao

    def executar_acao(self, botao, funcao, msg_sucesso):
        botao.setEnabled(False)
        self.status_label.setText("Executando...")

        self.thread = WorkerThread(funcao, success_msg=msg_sucesso)
        self.thread.finished.connect(lambda msg: self.acao_finalizada(botao, msg))
        self.thread.error.connect(lambda err: self.acao_erro(botao, err))
        self.thread.start()

    def acao_finalizada(self, botao, msg):
        botao.setEnabled(True)
        self.status_label.setText(msg)

    def acao_erro(self, botao, msg):
        botao.setEnabled(True)
        self.status_label.setText("")
        QMessageBox.critical(self, "Erro", msg)
