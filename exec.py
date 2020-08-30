import getpass
from src.Login import Login
from src.Driver import Driver
from src.Factory import Factory

print('\033[1m<<< Qual fluxo deseja executar? >>>\033[0m')
print('\033[1m===================================\033[0m')
print('\033[92m[comment]:\033[0m Comentar em algum post')
print('\033[92m[extract]:\033[0m Extrair seguidores de algum perfil')
print('\033[1m===================================')

flow = input('\033[94m Fluxo: \033[0m')
username = input('Seu login: ')
password = input('Sua senha: ')

driver = Driver().get()

factory = Factory().get(driver, flow)
login = Login(driver, username, password)

login.execute()
factory.execute()