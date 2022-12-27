#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import os
import clipboard


langs = []

langs.append("GNU G++20 11.2.0 (64 bit, winlibs)")
langs.append("Java 11.0.6")
langs.append("PyPy 3.9.10 (7.3.9, 64bit)")


options = webdriver.ChromeOptions()
options.add_experimental_option('debuggerAddress', 'localhost:9014')

driver = webdriver.Chrome(options=options)

pt = str(os.getcwd())

problem = ""
pt[len(pt) - 1]
ind = len(pt) - 1
while pt[ind] != '/':
	problem += pt
	ind-=1
problem = problem[::-1]

contest = ""

ind = len(pt) - 3
while pt[ind] != '/':
	contest += pt[ind]
	ind-=1

contest = contest[::-1]

driver.get("https://codeforces.com/contest/" + contest + '/submit/' + problem)

ext = ""
lang = 0
if os.path.exists(pt+"/"+problem+".cpp"):
	ext = ".cpp"
	lang = 1
elif os.path.exists(pt+"/"+problem+".java"):
	ext = ".java"
	lang = 2
else:
	ext = ".py"
	lang = 3


selectLang = Select(driver.find_element(By.NAME, "programTypeId"))

selectLang.select_by_visible_text(langs[lang - 1])

sourceCode = open(pt + "/" + pt[len(pt) - 1] + ext)

codeToSubmit = sourceCode.read()

sourceCode.close()

subFile = driver.find_element_by_xpath("//input[@type='file']")

subFile.send_keys(pt + "/" + pt[len(pt) - 1] + ext)

driver.find_element(By.CLASS_NAME, "submit").click()
