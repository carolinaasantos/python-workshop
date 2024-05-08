# Importa bibliotecas
import pyautogui
import time

# Pausa para esperar cada ação aconteccer
pyautogui.PAUSE = 0.5

# PASSO 1: Entrar no sistema

# Para abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=855, y=600) # Direcionar o mouse
pyautogui.click(x=855, y=600)

# Entrar no site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

# PASSO 2: Fazer login

# Selecionar espaço para digitar email
pyautogui.click(x=685, y=451)

# Escrever email, senha e logar
pyautogui.write("email@gmail.com")
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("senha123")
pyautogui.click(x=955, y=645) # clique no botao de login
time.sleep(3)
#time.sleep(5)
#print(pyautogui.position()) - para verificar o local do mouse

# PASSO 3: Importar a base de produtos pra cadastrar
import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=653, y=294)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim
