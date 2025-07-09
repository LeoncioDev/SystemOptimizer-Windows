# otimizador.py
import sys
from PyQt6.QtWidgets import QApplication
from gui.painel import PainelOtimizador

def main():
    app = QApplication(sys.argv)
    janela = PainelOtimizador()
    janela.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
