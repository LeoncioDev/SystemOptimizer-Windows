import os
import shutil

def limpar_temporarios(log_callback=None):
    def log(msg):
        if log_callback:
            log_callback(msg)
        else:
            print(msg)

    temp_paths = [
        os.environ.get('TEMP'),
        os.environ.get('TMP'),
        r'C:\Windows\Prefetch'
    ]

    for path in temp_paths:
        if not path or not os.path.exists(path):
            log(f"⚠️ Diretório não encontrado ou não acessível: {path}")
            continue

        log(f"🧹 Limpando arquivos temporários em: {path}")

        try:
            if path == r'C:\Windows\Prefetch':
                # Apaga somente arquivos (não pastas) dentro do Prefetch
                for entry in os.listdir(path):
                    file_path = os.path.join(path, entry)
                    if os.path.isfile(file_path):
                        try:
                            os.remove(file_path)
                            log(f"✔️ Arquivo removido: {entry}")
                        except Exception as e:
                            log(f"❌ Erro ao remover arquivo {entry}: {e}")
                log(f"✅ Limpeza de arquivos em {path} concluída.")
            else:
                # Para TEMP e TMP apaga arquivos e pastas recursivamente
                for entry in os.listdir(path):
                    entry_path = os.path.join(path, entry)
                    try:
                        if os.path.isfile(entry_path):
                            os.remove(entry_path)
                            log(f"✔️ Arquivo removido: {entry}")
                        elif os.path.isdir(entry_path):
                            shutil.rmtree(entry_path)
                            log(f"✔️ Pasta removida: {entry}")
                    except Exception as e:
                        log(f"❌ Erro ao remover {entry}: {e}")
                log(f"✅ Limpeza completa em {path}")
        except Exception as e:
            log(f"❌ Erro inesperado ao limpar {path}: {e}")

    log("🎉 Limpeza de arquivos temporários finalizada com sucesso!")

