import subprocess
import os
import winreg

def verificar_dotnet_framework(log_callback=None):
    def log(msg):
        if log_callback:
            log_callback(msg)
        else:
            print(msg)

    log("Verificando .NET Framework...")
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                             r"SOFTWARE\Microsoft\NET Framework Setup\NDP\v4\Full")
        value, _ = winreg.QueryValueEx(key, "Release")
        winreg.CloseKey(key)

        if value >= 528040:
            log(".NET Framework 4.8 ou superior está instalado.")
        else:
            log(".NET Framework instalado é inferior à versão 4.8.")
            log("Baixe e instale a versão mais recente do .NET Framework: https://dotnet.microsoft.com/en-us/download/dotnet-framework")

    except FileNotFoundError:
        log(".NET Framework 4.x não encontrado.")
        log("Baixe e instale o .NET Framework mais recente: https://dotnet.microsoft.com/en-us/download/dotnet-framework")
    except Exception as e:
        log(f"Erro ao verificar .NET Framework: {e}")

def verificar_visual_cpp_redistributables(log_callback=None):
    def log(msg):
        if log_callback:
            log_callback(msg)
        else:
            print(msg)

    log("Verificando Visual C++ Redistributables...")
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                             r"SOFTWARE\Classes\Installer\Dependencies\Microsoft.VC142.CRT,x64,amd64,14.27,bundle")
        winreg.CloseKey(key)
        log("Visual C++ Redistributable 2015-2019 encontrado.")
    except FileNotFoundError:
        log("Visual C++ Redistributable 2015-2019 não encontrado.")
        log("Baixe e instale o Visual C++ Redistributable (2015-2022): https://learn.microsoft.com/en-US/cpp/windows/latest-supported-vc-redist")
    except Exception as e:
        log(f"Erro ao verificar Visual C++ Redistributable: {e}")

def verificar_directx_runtime(log_callback=None):
    def log(msg):
        if log_callback:
            log_callback(msg)
        else:
            print(msg)

    log("Verificando DirectX Runtime...")
    try:
        system32_path = os.path.join(os.environ['WINDIR'], 'System32')
        d3d9_path = os.path.join(system32_path, 'd3d9.dll')
        if os.path.isfile(d3d9_path):
            log("DirectX Runtime encontrado.")
        else:
            log("DirectX Runtime não encontrado.")
            log("Baixe e instale o DirectX Runtime mais recente: https://www.microsoft.com/en-us/download/details.aspx?id=35")
    except Exception as e:
        log(f"Erro ao verificar DirectX Runtime: {e}")

def verificar_dependencias(log_callback=None):
    def log(msg):
        if log_callback:
            log_callback(msg)
        else:
            print(msg)

    log("==== Iniciando verificação das dependências para jogos ====")
    verificar_dotnet_framework(log_callback)
    verificar_visual_cpp_redistributables(log_callback)
    verificar_directx_runtime(log_callback)
    log("==== Verificação concluída ====")


if __name__ == "__main__":
    verificar_dependencias()
