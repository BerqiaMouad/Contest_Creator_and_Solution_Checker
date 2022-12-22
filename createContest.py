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

    for test in problemSoup.find_all(class_="sample-test"):
        fileIn = open(dir + '/' + 'in' + str(testCount) + '.txt', 'w')
        fileExpected = open(dir + '/' + 'expected' + str(testCount) + '.txt', 'w')
        for inputExample in test.find_all(class_="test-example-line"):
            fileIn.write(inputExample.text+'\n')
            
        for outputExample in test.find_all(class_="output"):
            fileExpected.write("\n".join(outputExample.find('pre').text.split()))
            fileExpected.write("\n")

        fileIn.close()
        fileExpected.close()
        testCount+=1

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
