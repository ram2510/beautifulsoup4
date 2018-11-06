import urllib.request as req # we import necessary libraries
import bs4 as bs 
from difflib import SequenceMatcher

start_link = "https://en.wikipedia.org/wiki/" # this is necessary for connection
keyword = input('enter the starting page with which you would like to start the crawling please make sure it is related to the word which you want\n=')
target_word = input('please enter the word noun/pronoun you are looking for\n=') # we ask for the word user is looking for
if (len(target_word.split())>=2): # if the word consist of more than 2 word we will seperate them with a _ not by space
    word = ''
    for j in range(len(target_word.split())):
        word = word + target_word.split()[j]
        if j != len(target_word.split())-1:
            word = word + '_'
final_word1 = word
url = start_link + keyword # this will our url
sauce = req.urlopen(url) # we start the connection
soup = bs.BeautifulSoup(sauce,'lxml') # we convert it into a beautiful soup library
conten_div= soup.find(id="mw-content-text").find(class_="mw-parser-output") # we will look for the keyword in this section
crawl_to = conten_div.find_all('a') # a tag is for links
for links in crawl_to: # for all the links this for loop will check whether the target word is there or not 
    y = str(links.get('title')) # this will get the title
    if (len(y.split()))>=2: # if its more than 2 words spaces will be replaced by _
        word = ''
        for i in range(len(y.split())):
            word = word + y.split()[i]
            if i != len(y.split())-1:
                word = word +'_'

    final_word = word
    prob = SequenceMatcher(None,final_word1,final_word).ratio() # this will be used to check whether the words are same
    if prob > 0.5:
        crosscheck = input(f'is this the noun/pronun you were looking for {final_word}?y or n').lower()
        if crosscheck == 'y':
            print("heres's your link enjoy!!!\n")
            print(start_link+final_word)
            break
        else:
            print('your target word could not be found sorry!')
            pass
        