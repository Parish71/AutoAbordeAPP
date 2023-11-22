# Codigo criado por Rafael Parish, Cientista de Dados HS, Analista de Dados Google, Engenheiro de Dados XP
# Toda e Qualquer Duvida Quanto a sua utilização não hesitar em entrar contato Comigo por LinkedIn ou outras redes sociais.


# Importando as bibliotecas (Lembre-se de instala-las antes de rodar o codigo)

import pyperclip
import pyautogui

# Insira entre os """"""  A sua mensagem de abordagem personalizada

mensagem_abordagem = f"""
Olá, como estão? Eu sou o Rafael Parish, atualmente Voluntário da Fundação Estudar, 
uma organização sem fins lucrativos de incentivo à educação e transformação social, 
que conecta membros de lideranças de sucesso, identificando e desenvolvendo lideranças, 
habilidades e carreiras.

Eu posso explicar melhor a vocês do que se trata para uma possível parceria?
"""

# Tempo de execução entre ações (Minha sugestão é que para computadores mais fracos seja 5-6 e para mais rapidos 2-3)

pyautogui.PAUSE = 2

# Definindo a quantidade de vezes que o loop será executado

quantidade_loops = 3

# abrir uma nova aba e ir para o instagram:

pyautogui.hotkey("ctrl", "t")
# configure o localizador para as coordenadas do preencher site
pyautogui.click(x=230, y=66)
pyperclip.copy("www.instagram.com")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

# abrir uma nova aba e ir para o planilha de metrificação:
pyautogui.hotkey("ctrl", "t")
# configure o localizador para as coordenadas do preencher site
pyautogui.click(x=230, y=66)
# Insira no Parentesis sua planilha atual de Leads (Minha sugestão é criar uma planilha a parte para este processo com o interesse de não desconfigurar a planilha geral)
pyperclip.copy("https://docs.google.com/spreadsheets/d/1nKTuzdwQxp-BM6r5vcU3GGR_tEU4pC_kI8zlI3rBuf0/edit#gid=1969456097")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

# clicando no lead atual (O primeiro lead da sua lista deve estar nesta coordenada)
pyautogui.click(x=158, y=303)


cell_counter = 1

for _ in range(quantidade_loops):
    
    pyautogui.click()

    # Copiando o conteúdo de contato do lead
    pyautogui.hotkey("ctrl", "c")
    pyautogui.press("enter")
    pyautogui.press("enter")

    # voltando para o instagram
    pyautogui.hotkey("ctrl", "shift", "tab")

    # configurar as coordenadas para clicar no botão Pesquisar
    pyautogui.click(x=32, y=304)

    # configurar as coordenadas para clicar no escrever do Pesquisar
    pyautogui.click(x=239, y=237)
    pyautogui.hotkey("ctrl", "v")

    # clicando no botão do usuario procurado
    pyautogui.click(x=231, y=278)

    pyautogui.PAUSE = 3

    # clicar no botao de acesso ao mensager
    pyautogui.click(x=606, y=174)

    # clicando no botão Escrever Mensagem(CORRIGIR)
    pyautogui.click(x=582, y=730)

    # Preenchendo a mensagem 
    pyperclip.copy(mensagem_abordagem)
    pyautogui.hotkey("ctrl", "v")
    
    # Envio da abordagem
    pyautogui.press("enter")

    # voltando para a metrificação em planilhas
    pyautogui.hotkey("ctrl", "shift", "tab")

    # Movendo o cursor para a célula abaixo
    pyautogui.moveTo(x=158, y=303)

    # Ajuste o valor 20 se necessário (Analisar zoom pelo video tutorial)
    pyautogui.move(0, 15 * cell_counter) 


    cell_counter = cell_counter + 1

print('Abordagens feitas com sucesso!')
