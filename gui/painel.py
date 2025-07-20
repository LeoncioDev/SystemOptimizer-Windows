from PyQt6.QtCore import Qt, QFile, QTextStream, pyqtSignal, QObject
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QGroupBox, QPushButton,
    QScrollArea, QMessageBox, QDialog, QCheckBox, QHBoxLayout,
    QTabWidget, QTextEdit, QSplitter
)
from .controller import Controller, WorkerThread


class DialogChecklistServicos(QDialog):
    def __init__(self, servicos, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Selecionar Serviços")
        self.setMinimumSize(400, 500)
        self.servicos = servicos
        self.checkboxes = []

        layout = QVBoxLayout()

        for servico in servicos:
            cb = QCheckBox(servico)
            cb.setChecked(True)
            self.checkboxes.append(cb)
            layout.addWidget(cb)

        btn_layout = QHBoxLayout()
        btn_ok = QPushButton("OK")
        btn_cancel = QPushButton("Cancelar")
        btn_ok.clicked.connect(self.accept)
        btn_cancel.clicked.connect(self.reject)
        btn_layout.addWidget(btn_ok)
        btn_layout.addWidget(btn_cancel)

        layout.addLayout(btn_layout)
        self.setLayout(layout)

    def get_selecionados(self):
        return [cb.text() for cb in self.checkboxes if cb.isChecked()]


class PainelOtimizador(QWidget):
    def __init__(self):
        super().__init__()
        self.controller = Controller()
        self.setWindowTitle("Painel de Otimização do Sistema")
        self.setGeometry(100, 100, 900, 600)

        self.splitter = QSplitter(Qt.Orientation.Horizontal)

        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout(self.main_widget)

        self.title_label = QLabel("</>LeoncioDev | Transformando ideias em código</>")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.title_label)

        self.main_layout.addWidget(self.criar_grupo_otimizacoes_gerais())
        self.main_layout.addWidget(self.criar_grupo_jogos())
        self.main_layout.addWidget(self.criar_grupo_manutencao())
        self.main_layout.addWidget(self.criar_grupo_extra())

        self.status_label = QLabel("")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.status_label)

        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)
        scroll_layout.addLayout(self.main_layout)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(scroll_widget)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(scroll_area)
        self.main_widget.setLayout(self.main_layout)

        self.splitter.addWidget(self.main_widget)

        self.console_tabs = QTabWidget()
        self.console_tabs.setMinimumWidth(300)

        self.log_text_edit = QTextEdit()
        self.log_text_edit.setReadOnly(True)
        self.console_tabs.addTab(self.log_text_edit, "Console de Logs")

        self.splitter.addWidget(self.console_tabs)
        self.splitter.setSizes([600, 300])

        final_layout = QVBoxLayout()
        final_layout.addWidget(self.splitter)
        self.setLayout(final_layout)

        self.threads = []

    def criar_grupo_otimizacoes_gerais(self):
        group = QGroupBox("🔧 Otimizações Gerais")
        layout = QVBoxLayout()
        layout.addWidget(self.criar_botao("✅ Limpar Arquivos Temporários", self.controller.limpar_temporarios, "Limpeza de arquivos temporários concluída."))

        btn_desabilitar = QPushButton("✅ Desativar Serviços Inúteis")
        btn_desabilitar.clicked.connect(lambda: self.abrir_dialogo_servicos("desabilitar", btn_desabilitar))
        layout.addWidget(btn_desabilitar)

        btn_reativar = QPushButton("♻️ Reativar Serviços")
        btn_reativar.clicked.connect(lambda: self.abrir_dialogo_servicos("reativar", btn_reativar))
        layout.addWidget(btn_reativar)

        layout.addWidget(self.criar_botao("✅ Ativar Perfil de Desempenho Máximo", self.controller.ativar_perfil_desempenho, "Perfil de desempenho ativado."))
        group.setLayout(layout)
        return group

    def criar_grupo_jogos(self):
        group = QGroupBox("🔥 Otimizações para Jogos")
        layout = QVBoxLayout()
        layout.addWidget(self.criar_botao("🎮 Ativar Modo de Jogo", self.controller.ativar_modo_jogo, "Modo Jogo ativado."))
        layout.addWidget(self.criar_botao("🎮 Ajustar Mouse e Teclado", self.controller.ajustar_mouse, "Mouse e teclado otimizados."))
        layout.addWidget(self.criar_botao("🔍 Verificar Dependências para Jogos", self.controller.verificar_dependencias_jogos, "Verificação de dependências concluída."))
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
        layout.addWidget(self.criar_botao("⚡ Desativar Efeitos Visuais", self.controller.desativar_efeitos_visuais, "Efeitos visuais desativados."))
        layout.addWidget(self.criar_botao("⚡ Reiniciar Windows Explorer", self.controller.reiniciar_explorer, "Windows Explorer reiniciado."))
        group.setLayout(layout)
        return group

    def criar_botao(self, texto, funcao, msg_sucesso):
        botao = QPushButton(texto)
        botao.clicked.connect(lambda: self.executar_acao(botao, funcao, msg_sucesso))
        return botao

    def abrir_dialogo_servicos(self, acao, botao_clicado):
        servicos = self.controller.obter_lista_servicos()
        dialogo = DialogChecklistServicos(servicos, self)
        if dialogo.exec() == QDialog.DialogCode.Accepted:
            selecionados = dialogo.get_selecionados()
            if not selecionados:
                QMessageBox.warning(self, "Atenção", "Nenhum serviço selecionado!")
                return

            if acao == "desabilitar":
                func = lambda: self.controller.desabilitar_servicos(selecionados)
                msg = "Serviços desabilitados."
            else:
                func = lambda: self.controller.reativar_servicos(selecionados)
                msg = "Serviços reativados."

            self.executar_acao(botao_clicado, func, msg)

    def executar_acao(self, botao, funcao, msg_sucesso):
        botao.setEnabled(False)
        self.status_label.setText("Executando...")
        self.log(f"Executando ação: {botao.text()}")

        thread = WorkerThread(funcao, success_msg=msg_sucesso)
        self.threads.append(thread)

        thread.log_signal.connect(self.log)
        thread.finished.connect(lambda msg: self.acao_finalizada(botao, msg))
        thread.error.connect(lambda err: self.acao_erro(botao, err))
        thread.start()

    def acao_finalizada(self, botao, msg):
        botao.setEnabled(True)
        self.status_label.setText(msg)
        self.log(f"✔️ {msg}")

    def acao_erro(self, botao, msg):
        botao.setEnabled(True)
        self.status_label.setText("")
        self.log(f"❌ Erro: {msg}")
        QMessageBox.critical(self, "Erro", msg)

    def log(self, texto):
        self.log_text_edit.append(texto)
        self.log_text_edit.verticalScrollBar().setValue(
            self.log_text_edit.verticalScrollBar().maximum()
        )
