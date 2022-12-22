#!/usr/bin/env python3

from termcolor import colored
import os 


# function to test each test at a time
def test(out, expected, testNum):
	print(colored("test #" + str(testNum) + ":"))
	file_1 = open(out, 'r')
	file_2 = open(expected, 'r')

	lines1 = file_1.readlines();
	lines2 = file_2.readlines();

	diff =[]
	test =[]

	for i in range(len(lines2)):
		if(lines2[i] != lines1[i]):
			diff.append([lines1[i], lines2[i]])
			test.append(i+1)

	if(len(diff) == 0):
		print(colored('Passed ✓', 'green', attrs=['bold']))
	else:
		print(colored('Wrong Answer ✗', 'red', attrs=['bold']))
		print("++++++++++++++++++++++++++++")
		print()
		for i in range(len(diff)):
			print(colored("On test #"+str(test[i])+":", 'green'))
			print()
			print(colored('Output', attrs=['bold']))
			print()
			for j in diff[i][0]:
				print(j, end="")
			print("\n===========================")
			print(colored('Expected', attrs=['bold']))
			print()
			for j in diff[i][1]:
				print(j, end="")
			print("\n===========================")

	file_1.close()
	file_2.close()

index = 1
while os.path.exists(os.path.abspath(os.getcwd()) + "/in" + str(index) + ".txt"):
	os.system("g++ "+ str(os.getcwd())[-1] + ".cpp -o " + str(os.getcwd())[-1])
	os.system("./" + str(os.getcwd())[-1] + " < in" + str(index) + ".txt > out"+str(index)+".txt")
	test("out"+str(index)+".txt", "expected"+str(index)+".txt", index)
	index+=1

