from selenium import webdriver  
from selenium.webdriver.common.by import By  
 
# Получаем в переменную browser указатель на браузер  
browser=webdriver.Chrome()  

# Переходим на страницу, на которой находится форма для авторизации  
browser.get('http://127.0.0.1:5500/avtoriz.html')  

# заполняем поле логин, привязываемся к элементу через его имя  
login=browser.find_element(by=By.ID, value='login')  
login.send_keys('Кривко')  

# заполняем поле пароля, привязываемся к элементу через его id  
password=browser.find_element(by=By.ID, value='password')  
password.send_keys('')  
 
#Получаем указатель на кнопку "Вход", привязываемся к элементу через его css_selector  
button=browser.find_element(by=By.CSS_SELECTOR, value='#registrbtn')  
 
#Нажимаем на кнопку входа  
button.click()