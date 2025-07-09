import os
import shutil

def limpar_temporarios():
    temp_paths = [
        os.environ.get('TEMP'),
        os.environ.get('TMP'),
        'C:\\Windows\\Prefetch'
    ]
    
    for path in temp_paths:
        if path and os.path.exists(path):
            try:
                # Verifica se o caminho corresponde à pasta 'Prefetch' (não deve remover pastas)
                if path == 'C:\\Windows\\Prefetch':
                    # Limpa apenas os arquivos na pasta Prefetch
                    for file in os.listdir(path):
                        file_path = os.path.join(path, file)
                        if os.path.isfile(file_path):
                            try:
                                os.remove(file_path)  # Remove o arquivo
                                print(f"Arquivo {file} removido com sucesso!")
                            except Exception as e:
                                print(f"Erro ao remover o arquivo {file}: {e}")
                    print(f"Arquivos temporários em {path} limpos com sucesso!")
                else:
                    # Remove arquivos da pasta %TEMP% ou %TMP%
                    for file in os.listdir(path):
                        file_path = os.path.join(path, file)
                        try:
                            if os.path.isfile(file_path):
                                os.remove(file_path)  # Remove o arquivo
                                print(f"Arquivo {file} removido com sucesso!")
                            elif os.path.isdir(file_path):
                                shutil.rmtree(file_path)  # Remove diretórios
                                print(f"Pasta {file} removida com sucesso!")
                        except Exception as e:
                            print(f"Erro ao remover {file_path}: {e}")
                    print(f"Arquivos temporários em {path} limpos com sucesso!")
            except Exception as e:
                print(f"Erro ao limpar {path}: {e}")
        else:
            print(f"Não foi possível localizar o diretório: {path}")

    print("Limpeza de arquivos temporários concluída com sucesso!")
