import json
import os
import tkinter
from tkinter.filedialog import askopenfilename

from selenium import webdriver


def create_rep_in_git():
    driver = webdriver.Edge('/Users/Mohamed/Downloads/msedgedriver')
    data = json.load(open('D:\passwords.json'))
    password = data['github_password']
    username = data['github_username']
    driver.get('https://github.com/login')
    while True:
        try:
            driver.find_element_by_xpath('/html/body/div[3]/main/div/div[4]/form/input[2]').send_keys(username)
            driver.find_element_by_xpath('/html/body/div[3]/main/div/div[4]/form/input[3]').send_keys(password)
            driver.find_element_by_xpath('/html/body/div[3]/main/div/div[4]/form/input[14]').click()
            break
        except:
            pass
    while True:
        try:
            driver.find_element_by_xpath('/html/body/div[4]/div/aside[1]/div[2]/div[1]/div/h2/a').click()
            break
        except:
            pass
    while True:
        try:
            driver.find_element_by_xpath('/html/body/div[4]/main/div/form/div[2]/auto-check/dl/dd/input').send_keys(
                repository_name)
            driver.find_element_by_xpath('/html/body/div[4]/main/div/form/div[4]/div[4]/div[1]/label/input[2]').click()
            driver.find_element_by_xpath('/html/body/div[4]/main/div/form/div[4]/button').submit()
            driver.quit()
            break
        except:
            pass


def cmd_upload_to_rep():
    url = 'https://github.com/Alimohamad21/{}.git'.format(repository_name)
    cmd2 = 'git remote add origin {}'.format(url)
    os.chdir(directory)
    os.system(
        'cmd /c "git init&git add .&git commit -m "First commit"&git branch -M main&{}&git push -f origin main"'.format(
            cmd2))


def cmd_update_rep():
    commit_name = input('Please enter a short description for your commit:')
    os.chdir(directory)
    os.system(
        'cmd /c "git add .&git commit -m "{}"&git push -f origin main"'.format(
            commit_name))


choice = input('1-New Repository\n2-Exisiting Repository\nPlease choose an option form the above:')
root = tkinter.Tk()
root.withdraw()
directory = tkinter.filedialog.askdirectory()
if choice == '1':
    repository_name = input('Please enter a name for your repo:')
    repository_name = repository_name.replace(' ', '-')
    create_rep_in_git()
    cmd_upload_to_rep()
if choice == '2':
    cmd_update_rep()
input('Press any button to exit')
