from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time


green_c = '\33[92m'
reset_c = '\033[0m'



print(green_c+"     ,--.   ,--.,-----. ,--------.,------.        "+reset_c)
print(green_c+"      \  `.'  /'  .-.  ''--.  .--'|  .---'        "+reset_c)
print(green_c+"       \     / |  | |  |   |  |   |  `--,         "+reset_c)
print(green_c+"        \   /  '  '-'  '   |  |   |  `---.        "+reset_c)
print(green_c+"         `-'    `-----'    `--'   `------'        "+reset_c)
print(green_c+"     ,------. ,-----. ,------.                    "+reset_c)
print(green_c+"     |  .---''  .-.  '|  .--. '                   "+reset_c)
print(green_c+"     |  `--, |  | |  ||  '--'.'                   "+reset_c)
print(green_c+"     |  |`   '  '-'  '|  |\  \                    "+reset_c)
print(green_c+"     `--'     `-----' `--' '--'                   "+reset_c)
print(green_c+"     ,-------. ,-----.  ,---.  ,--. ,--.  ,---.   "+reset_c)
print(green_c+"     `--.   / '  .-.  ''   .-' |  .'   / /  O  \  "+reset_c)
print(green_c+"       /   /  |  | |  |`.  `-. |  .   ' |  .-.  | "+reset_c)
print(green_c+"      /   `--.'  '-'  '.-'    ||  |\   \|  | |  | "+reset_c)
print(green_c+"     `-------' `-----' `-----' `--' '--'`--' `--' "+reset_c)
print("\n\n\n")

print("     Program ten automatycznie głosuje na najlepszą szkołę w województwie Mazowieckim :).\n     Należy pozostawić włączone, a głosowanie wygra napewno Zośka. \n     Efektywność programu: 6 głosów na ZOŚKĘ w ciągu minuty.\n     Aby wyłączyć program należy zamknąć otwarte okno przeglądarki,\n     a następnie zamknąć to czarne okienko które wyskoczyło.\n\n")

input("          Aby rozpocząć pracę programu, naciśnij enter..\n\n\n")                                                                                                                                     


driver = webdriver.Chrome(executable_path='c:/chromedriver.exe')
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfb7peOYj6iylCGI45Cj_85NDULEcix_ejjf4xoyjdc6PkM-A/viewform") 
time.sleep(4)





while True:


    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div/div/div/div[2]/div/div/span/div/div[4]/label"))).click()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div/div[1]/div"))).click()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a"))).click()

   

    time.sleep(3)
