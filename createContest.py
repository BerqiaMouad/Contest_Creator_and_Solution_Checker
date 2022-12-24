#!/usr/bin/env python3

from termcolor import colored
from bs4 import BeautifulSoup as bs
import requests 
import os
import sys
import time

contestNumber = sys.argv[1]

url = 'https://codeforces.com/contest/' + str(contestNumber)


def progressBar(progress, total):
    percent = 100 * (progress / total)
    bar = '█' * int(percent) + '-' * (100 - int(percent))
    print(colored(f"\r▏{bar}▕ : {percent:.2f}%", 'green', attrs=['bold']), end="\r")


def choseLang():
    print("1. C++ \n2. Java \n3. Python")
    lang = input("Please chose your language (1, 2 or 3): ")
    return lang


def sample(did):
    if(not(did)):
        pr = input("Do you want to copy an existing code as a sample? (YES / NO): ")
        did = True
    else:
        pr = input("Please enter YES or NO: ")
    if(pr.lower() == "yes"):
        return True
    elif(pr.lower() == "no"):
        return False
    else:
        print(colored("Bad choice! ", 'red', attrs=['bold']), end="")
        sample(did)

def initProblem(problem, dir, lang, hasSample):
    if(lang == "1" and hasSample):
        os.system("cp /bin/sample.cpp " + dir + "/" + problem + ".cpp")
    elif(lang == "1" and not(hasSample)):
        os.system("touch " + dir + '/' + problem + ".cpp")
    elif(lang == "2" and hasSample):
        os.system("cp /bin/sample.java " + dir + "/" + problem + ".java")
    elif(lang == "2" and not(hasSample)):
        os.system("touch " + dir + '/' + problem + '.java')
    elif(lang == "3" and hasSample):
        os.system("cp /bin/sample.py "+ dir + "/" + problem + ".py")
    elif(lang == "3" and not(hasSample)):
        os.system("touch " + dir + "/" + problem + ".py")
    else:
        print(colored("ERROR: " + lang + " is not in the list!", 'red', attrs=['bold']))
        return -1

    problemUrl = url + '/problem/' + problem
    problemPage = requests.get(problemUrl)
    problemSoup = bs(problemPage.content, 'html.parser')

    testCount = 1

    for testIn, testOut in zip(problemSoup.find_all(class_="input"), problemSoup.find_all(class_="output")):
        fileIn = open(dir + '/' + 'in' + str(testCount) + '.txt', 'w')
        fileExpected = open(dir + '/' + 'expected' + str(testCount) + '.txt', 'w')

        ct = 0
        for inputExample in testIn.find('pre'):
            l = inputExample.text.split("\n")
            for i in l:
                if(i == ''):
                    continue
                fileIn.write(i + "\n")
        
        print("Got sample input#" + str(testCount) + " ✓")
        time.sleep(0.2)
        for outputExample in testOut.find('pre'):
            l = outputExample.text.split("\n")
            for i in l:
                if(i == ''):
                    continue
                fileExpected.write(i + "\n")

        print("Got sample output#" + str(testCount) + " ✓")
        time.sleep(0.2)
        fileIn.close()
        fileExpected.close()
        

        testCount += 1
    
    return 0;

page = requests.get(url)

soup = bs(page.content, 'html.parser')

numOfProblems = len(soup.find_all(class_="id"))

os.mkdir(contestNumber)

progress = 0;

lang = choseLang()
hasSample = sample(False)
l = []

for i in range(numOfProblems):
    os.system("clear")
    progressBar(i, numOfProblems)
    print()
    print()
    for j in l:
        print(colored(j, 'green', attrs=['bold']))

    print()
 
    dir = chr(65 + i);
    os.mkdir('./' + sys.argv[1] + '/' + dir)
    initialize = initProblem(chr(65 + i), os.path.abspath(os.getcwd()) + '/' + str(contestNumber) + '/' + dir, lang, hasSample)
    if(initialize == -1):
        os.system("rm -r " + os.getcwd() + '/' + str(contestNumber))
        exit(-1)
    os.system("clear")
    progressBar(i+1, numOfProblems)
    print()
    print()
    l.append("Created " + dir)
    for j in l:
        print(colored(j, 'green', attrs=['bold']))

print()
print()
print("===============================")
print(colored("Contest created successfully ✓", 'green', attrs=['bold']))
print("===============================")
print()
print("Complete problemset : " + url + "/problems")
print()
