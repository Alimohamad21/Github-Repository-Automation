import json
import os
import tkinter
from tkinter.filedialog import askopenfilename

from selenium import webdriver


class Git:
    def __init__(self):
        self.directory = ""
        self.repository_name = ""
        self.driver = None
        self.url = "https://github.com/Alimohamad21/"

    def log_into_git(self):
        self.driver = webdriver.Edge('/Users/Mohamed/Downloads/msedgedriver')
        data = json.load(open('D:\passwords.json'))
        password = data['github_password']
        username = data['github_username']
        self.driver.get('https://github.com/login')
        while True:
            try:
                self.driver.find_element_by_xpath('/html/body/div[3]/main/div/div[4]/form/input[2]').send_keys(username)
                self.driver.find_element_by_xpath('/html/body/div[3]/main/div/div[4]/form/div/input[1]').send_keys(
                    password)
                self.driver.find_element_by_xpath('/html/body/div[3]/main/div/div[4]/form/div/input[12]').click()
                break
            except:
                pass

    def create_rep_in_git(self):
        while True:
            try:
                self.driver.find_element_by_xpath(
                    '/html/body/div[4]/div/aside[1]/div[2]/div[1]/div/h2/a').click()  # test
                break
            except:
                pass
        while True:
            try:
                self.driver.find_element_by_xpath(
                    '/html/body/div[4]/main/div/form/div[2]/auto-check/dl/dd/input').send_keys(
                    self.repository_name)
                self.driver.find_element_by_xpath(
                    '/html/body/div[4]/main/div/form/div[4]/div[4]/div[1]/label/input[2]').click()
                self.driver.find_element_by_xpath('/html/body/div[4]/main/div/form/div[4]/button').submit()
                self.driver.minimize_window()
                break
            except:
                pass

    def cmd_upload_to_rep(self):
        self.url = self.url + format(self.repository_name) + '.git'
        cmd2 = 'git remote add origin {}'.format(self.url)
        os.chdir(self.directory)
        commit = '{commited automatically using https://github.com/Alimohamad21/Github-Repository-Automation}'
        os.system(
            f'cmd /c "git init&git add .&git commit -m "{commit}"&git branch -M main&{cmd2}&git push -f origin main"')

    def update_existing_repository(self):
        commit_name = input('Please enter a short description for your commit:')
        commit_name += ' {commited automatically using https://github.com/Alimohamad21/Github-Repository-Automation}'
        os.chdir(self.directory)
        os.system(
            f'cmd /c "git pull origin main&git add .&git commit -m "{commit_name}"&git push -f origin main"')
        self.log_into_git()
        self.driver.maximize_window()
        self.driver.get('https://github.com/Alimohamad21?tab=repositories')
        while True:
            try:
                self.driver.find_element_by_xpath(
                    '/html/body/div[4]/main/div[2]/div/div[2]/div[2]/div/div[2]/ul/li[1]/div[1]/div[1]/h3/a').click()
                break
            except:
                pass

    def new_repository(self):
        self.repository_name = input('Please enter a name for your repo:')
        self.repository_name = self.repository_name.replace(' ', '-')
        self.log_into_git()
        self.create_rep_in_git()
        self.cmd_upload_to_rep()
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.find_element_by_xpath(
            '/html/body/ytd-app/div/tp-yt-app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]/ytd-guide-section-renderer[1]/div/ytd-guide-entry-renderer[3]/a/tp-yt-paper-item/yt-formatted-string')


choice = input('1-New Repository\n2-Existing Repository\nPlease choose an option from the above:')
root = tkinter.Tk()
root.withdraw()
git = Git()
git.directory = tkinter.filedialog.askdirectory()
if choice == '1':
    git.new_repository()
if choice == '2':
    git.update_existing_repository()
input('Press any button to exit')
