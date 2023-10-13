import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(3)

pyautogui.click(x=745, y=586)
pyautogui.write("eoliveiradeliz@gmail.com")

pyautogui.press("tab")
pyautogui.write("12345")

pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

tabela = pd.read_csv('produtos.csv')
print(tabela)

# for linha in tabela.index:
pyautogui.click(x=1013, y=425)

pyautogui.write("codigo")
pyautogui.press("tab")
pyautogui.write("marca")
pyautogui.press("tab")
pyautogui.write("tipo")
pyautogui.press("tab")
pyautogui.write("categoria")
pyautogui.press("tab")
pyautogui.write("preco")
pyautogui.press("tab")
pyautogui.write("custo")
pyautogui.press("tab")
pyautogui.write("obs")
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.scroll(50000)
