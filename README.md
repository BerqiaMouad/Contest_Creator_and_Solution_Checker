# This is a personal project 

Using this mini project you can get all the problems and theire input data and the expected data.
Also, you can code your solution and test it locally using the check.py script.

## 1. Setup

To be able to run these scripts you need to setup some stuff.

First you need to put the two scripts in your /bin directory.
Then you should give them the rights to be executed.

run the following command in the /bin directory after copying the two scripts:
`chmod u+x`

Now you need to install some dependencies:

### Python3 and pip

In your terminal run the following commands:

`sudo apt update `
`sudo apt install python3 `
`sudo apt install python3-pip `

### termcolor and beautifulsoup

run this command:

`pip3 install termcolor `
`pip3 install bs4 `


### Creating and Testing 

##### To create a new directory containing the contest you want you should run the folloing command

`createContest.py number_of_the_contest `

You can get the number of the contest when you open its link for exemple:

` https://codeforces.com/contest/1772/ `

Here the number of the contest is 1772

After that you should enter the directory of the contest (its name will be the number of the problem).

##### To test a problem you want, access the directory of the problem then type the following command

` check.py `

