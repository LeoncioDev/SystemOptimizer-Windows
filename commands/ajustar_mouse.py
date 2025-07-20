import subprocess

def otimizar_mouse_teclado(log_callback=None):
    try:
        if log_callback:
            log_callback("Ajustando configurações do mouse...")

        subprocess.run(['reg', 'add', r'HKEY_CURRENT_USER\Control Panel\Mouse', '/v', 'MouseSpeed', '/t', 'REG_DWORD', '/d', '0', '/f'], check=True)
        subprocess.run(['reg', 'add', r'HKEY_CURRENT_USER\Control Panel\Mouse', '/v', 'MouseThreshold1', '/t', 'REG_DWORD', '/d', '0', '/f'], check=True)
        subprocess.run(['reg', 'add', r'HKEY_CURRENT_USER\Control Panel\Mouse', '/v', 'MouseThreshold2', '/t', 'REG_DWORD', '/d', '0', '/f'], check=True)
        subprocess.run(['reg', 'add', r'HKEY_CURRENT_USER\Control Panel\Mouse', '/v', 'MouseSensitivity', '/t', 'REG_DWORD', '/d', '6', '/f'], check=True)

        if log_callback:
            log_callback("Configuração do mouse ajustada para reduzir o input lag.")

        if log_callback:
            log_callback("Ajustando configurações do teclado...")

        subprocess.run(['reg', 'add', r'HKEY_CURRENT_USER\Control Panel\Keyboard', '/v', 'KeyboardDelay', '/t', 'REG_DWORD', '/d', '0', '/f'], check=True)
        subprocess.run(['reg', 'add', r'HKEY_CURRENT_USER\Control Panel\Keyboard', '/v', 'KeyboardSpeed', '/t', 'REG_DWORD', '/d', '31', '/f'], check=True)

        if log_callback:
            log_callback("Configurações de teclado ajustadas para otimizar o desempenho em jogos.")

    except subprocess.CalledProcessError as e:
        if log_callback:
            log_callback(f"Erro ao tentar ajustar as configurações: {e}")
        else:
            raise
