from flask import Flask, render_template, url_for, flash, redirect,request,session
from passlib.hash import sha256_crypt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import pyautogui
import autoit
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route("/",methods=['GET', 'POST'])
def index():
    return'<h1>hello</h1>'


@app.route("/main", methods=['GET', 'POST'])
def main():
    session.clear()
    return render_template('main.html')

@app.route("/pro", methods=['GET', 'POST'])
def pro():
    return render_template('pro.html')

@app.route("/Upload", methods=['GET', 'POST'])
def Upload():
    path=request.form['path']
    print(path)
    session['path']=path
    seed()
    url=session['uri']
    return render_template('main.html', value=url, title='Seeding')


@app.route("/upload", methods=['GET', 'POST'])
def upload():
    return render_template('upload.html')

@app.route("/new", methods=['GET', 'POST'])
def new():
    return render_template('new.html')

@app.route("/seed", methods=['GET', 'POST'])
def seed():
    return render_template('seed.html')

def seed():
    browser = webdriver.Chrome(executable_path='C:\webdrivers\chromedriver')
    browser.set_window_position(-10000,0)
    browser.implicitly_wait(20)
    browser.get('https://btorrent.xyz/')
    browser.find_element_by_xpath('//*[@id="view"]/div/div[1]/div[4]/button').click()
    time.sleep(5)
    autoit.control_focus("Open","")
    p=session['path']
    autoit.control_set_text("Open", "Edit1", p)
    autoit.control_click("Open", "Button1")
    button=browser.find_element_by_xpath('/html/body/div[2]/div/div[3]/div[1]/ul/li[2]/a')
    z=button.get_attribute('href')
    session['uri']=z
    print(z)
    time.sleep(3)


if __name__ == '__main__':
    app.run(debug=True)
