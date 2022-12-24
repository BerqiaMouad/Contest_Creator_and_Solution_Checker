# This is a personal project 

Using this mini project you can get all the problems and theire input data and the expected data.
Also, you can code your solution and test it locally using the check.py script.

PS: This tool only works on linux !

## 1. Setup

To be able to run these scripts you need to setup some stuff.

First you need to put the two scripts in your /bin directory.
Then you should give them the rights to be executed.

run the following command in the /bin directory after copying the two scripts:
`chmod u+x`

Now you need to install some dependencies:

### Python3 and pip

In your terminal run the following commands:

``` 
sudo apt update 
sudo apt install python3 
sudo apt install python3-pip 
```

### termcolor and beautifulsoup

run this command:

```
pip3 install termcolor
pip3 install bs4 
pip3 install clipboard
pip3 install selenium

```


## 2. Creating and Testing 

##### To create a new directory containing the contest you want you should run the folloing command

`createContest.py number_of_the_contest `

You can get the number of the contest when you open its link for exemple:

` https://codeforces.com/contest/1772/ `

Here the number of the contest is 1772

You will be prompted to chose the programming language you like to use, chose one by selecting the number (1, 2 or 3)

Then you will be asked if you want to use a code as a sample, you should have already created a file in the bin directory to be able to use it as a sample and you have to name it "sample.(extension of your language)" for example: sample.cpp or sample.py

After that you should access the directory of the contest (its name will be the number of the problem).

##### To test a problem you want, access the directory of the problem then type the following command

` check.py `


## 3. Submiting solution

##### To submit your solution you will need to execute ` sub.py ` script. (You should be in the directory of the problem)


