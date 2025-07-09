import subprocess
import tkinter as tk
from tkinter import messagebox

def otimizar_mouse_teclado():
    try:
        # Ajustes para o mouse: Desabilitar aceleração e configurar sensibilidade ideal
        print("Ajustando configurações do mouse...")
        
        # Desabilitar aceleração do mouse
        subprocess.run(['reg', 'add', r'HKEY_CURRENT_USER\Control Panel\Mouse', '/v', 'MouseSpeed', '/t', 'REG_DWORD', '/d', '0', '/f'], check=True)
        subprocess.run(['reg', 'add', r'HKEY_CURRENT_USER\Control Panel\Mouse', '/v', 'MouseThreshold1', '/t', 'REG_DWORD', '/d', '0', '/f'], check=True)
        subprocess.run(['reg', 'add', r'HKEY_CURRENT_USER\Control Panel\Mouse', '/v', 'MouseThreshold2', '/t', 'REG_DWORD', '/d', '0', '/f'], check=True)
        
        # Ajustar a sensibilidade do mouse para 6 (padrão)
        subprocess.run(['reg', 'add', r'HKEY_CURRENT_USER\Control Panel\Mouse', '/v', 'MouseSensitivity', '/t', 'REG_DWORD', '/d', '6', '/f'], check=True)
        
        print("Configuração do mouse ajustada para reduzir o input lag.")

        # Ajustes para o teclado: Reduzir o tempo de resposta e aumentar a velocidade de digitação
        print("Ajustando configurações do teclado...")
        
        # Definir o tempo de resposta do teclado para o mínimo (sem delay)
        subprocess.run(['reg', 'add', r'HKEY_CURRENT_USER\Control Panel\Keyboard', '/v', 'KeyboardDelay', '/t', 'REG_DWORD', '/d', '0', '/f'], check=True)
        
        # Definir a velocidade de repetição de teclas para o máximo
        subprocess.run(['reg', 'add', r'HKEY_CURRENT_USER\Control Panel\Keyboard', '/v', 'KeyboardSpeed', '/t', 'REG_DWORD', '/d', '31', '/f'], check=True)

        print("Configurações de teclado ajustadas para otimizar o desempenho em jogos.")
    
    except subprocess.CalledProcessError as e:
        print(f"Erro ao tentar ajustar as configurações: {e}")

# Função para criar a interface gráfica
def criar_interface():
    root = tk.Tk()
    root.title("Otimização de Mouse e Teclado")

    def on_button_click():
        print("Iniciando a otimização de mouse e teclado...")
        otimizar_mouse_teclado()
        messagebox.showinfo("Sucesso", "Otimizações de mouse e teclado concluídas!")

    button = tk.Button(root, text="Otimizar Mouse e Teclado", command=on_button_click)
    button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    criar_interface()
