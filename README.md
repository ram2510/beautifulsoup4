# BeautifulSoup 4 Projects

I used the Jupyter notebook for my beautifulsoup projects you can use any text editor but you will not be able to view my code if you don't have jupyter notebook installed

## Download Juypter notebook:-
You can download the jupyter notebook as a conda package if you have conda installed(it's pre loaded with the anconda distribution but not with the miniconda distribution) use the command in your conda pompt 
```
conda install jupyter notebook
```
this should succesfully download the notebook

Now to run the jupyter notebook type 
```
jupyter notebook
``` 
in your conda prompt 


## Download Python 3.x :-
I made all of my projects using python3, it will be replaced in the future by its succesor but I belive the changes in the syntax will be minimal so if you have python version other than 3.X look out for changes in my code

[To download python](https://www.python.org/downloads/)

## Download Beautifulsoup4 :- 
You can download beautifulsoup 4 from the command prompt using the command 
```
pip3 install bs4
```
or manually download it from the link given below

[To download BeautifulSoup4](https://pypi.org/project/beautifulsoup4/#files)

## PROJECTS
My projects using bs4

### Web scrapper

I created a basic web scrapping program that parses through a wikipedia Asian countries page and displays all the Asian countries in a table using the pandas library
To view the source code I would suggest you to view it using jupyter notebook

### Video scarapper

I created a program which asks for you the keywords that you type in the the YouTube search bar this program will display the results and then you have to enter the title number of the video that you want to download and this program will give you the link to download that video


### Wikipedia crawler

If you want to search sachin tendulkar on the cricket wikipedia page but you are too lazy to write the full name so the chances are you will not get the desired webpage using other wiki crawlers
This script takes a starting webpage name(eg = cricket) and a noun/pronoun(eg = sachin) as input it starts the starts web crawling with the title of the web page you gave as the input and crawls till you get the desired output as the noun/pronoun. It will start matching the links on the webpage using the difflib SequencMatcher module it will show you whether the links corresponds to the link or the webpage you want if found it will print the link
