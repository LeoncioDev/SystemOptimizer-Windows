from PyQt6.QtWidgets import (
    QWidget, QTabWidget, QVBoxLayout, QTextEdit, QDialog,
    QHBoxLayout, QPushButton
)
from PyQt6.QtCore import Qt

class ConsoleTabs(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Console de Logs")
        self.resize(700, 400)

        layout = QVBoxLayout()
        self.tabs = QTabWidget()
        layout.addWidget(self.tabs)

        # Botão para limpar a aba ativa
        btn_layout = QHBoxLayout()
        self.btn_limpar = QPushButton("Limpar Aba")
        self.btn_limpar.clicked.connect(self.limpar_aba_atual)
        btn_layout.addWidget(self.btn_limpar)
        btn_layout.addStretch()
        layout.addLayout(btn_layout)

        self.setLayout(layout)

        # Abas iniciais
        self.add_tab("Geral")
        self.add_tab("Serviços")
        self.add_tab("Jogos")
        self.add_tab("Manutenção")
        self.add_tab("Extra")

    def add_tab(self, nome):
        text_edit = QTextEdit()
        text_edit.setReadOnly(True)
        self.tabs.addTab(text_edit, nome)

    def escrever_log(self, nome_aba, texto):
        for i in range(self.tabs.count()):
            if self.tabs.tabText(i) == nome_aba:
                text_edit = self.tabs.widget(i)
                text_edit.append(texto)
                # Auto-scroll para o fim
                cursor = text_edit.textCursor()
                cursor.movePosition(cursor.MoveOperation.End)
                text_edit.setTextCursor(cursor)
                break

    def limpar_aba_atual(self):
        current = self.tabs.currentWidget()
        if current:
            current.clear()
