import subprocess
import time

def abrir_msconfig_servicos():
    """Abre o MSConfig (sem ir direto para a aba 'Serviços', pois não há comando específico)."""
    subprocess.run("msconfig", shell=True)

def abrir_taskmgr_servicos():
    """Abre o Gerenciador de Tarefas na aba 'Serviços'."""
    subprocess.run("taskmgr /0 /services", shell=True)

# Escolha qual abrir
print("Escolha uma opção:")
print("1 - Abrir MSConfig")
print("2 - Abrir Gerenciador de Tarefas na aba 'Serviços'")
opcao = input("Digite o número da opção desejada: ")

if opcao == "1":
    abrir_msconfig_servicos()
elif opcao == "2":
    abrir_taskmgr_servicos()
else:
    print("Opção inválida!")
