import tkinter as tk
from tkinter import messagebox

def overclock():
    # Criar a janela principal invisível (não será exibida na tela)
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal
    
    # Exibir o pop-up
    messagebox.showinfo("Aviso", "Tá de brincadeira né?? Overclock no painel de otimização??")

if __name__ == "__main__":
    overclock()
