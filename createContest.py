#!/usr/bin/env python3

from termcolor import colored
from bs4 import BeautifulSoup as bs
import requests 
import os
import sys

contestNumber = sys.argv[1]

url = 'https://codeforces.com/contest/' + str(contestNumber)


def progressBar(progress, total):
    percent = 100 * (progress / total)
    bar = '|' * int(percent) + '-' * (100 - int(percent))
    print(colored(f"\r|{bar}| : {percent:.2f}%", 'green', attrs=['bold']), end="\r")


def initProblem(problem, dir):
    os.system("cp /bin/sample.cpp " + dir + "/" + problem + ".cpp")
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
        
        for outputExample in testOut.find('pre'):
            l = outputExample.text.split("\n")
            for i in l:
                if(i == ''):
                    continue
                fileExpected.write(i + "\n")

        fileIn.close()
        fileExpected.close()

        testCount += 1

page = requests.get(url)

soup = bs(page.content, 'html.parser')

numOfProblems = len(soup.find_all(class_="id"))

os.mkdir(contestNumber)

progress = 0;

for i in range(numOfProblems):
    dir = chr(65 + i);
    os.mkdir('./' + sys.argv[1] + '/' + dir)
    initProblem(chr(65 + i), os.path.abspath(os.getcwd()) + '/' + str(contestNumber) + '/' + dir)
    os.system("clear")
    progressBar(i+1, numOfProblems)

print()
print()
print("===============================")
print(colored("Contest created successfully ✓", 'green', attrs=['bold']))
print("===============================")
print()
print("Complete problemset : " + url + "/problems")
print()
