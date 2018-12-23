from bs4 import BeautifulSoup
import urllib2


response = urllib2.urlopen('http://www.gutenberg.org/cache/epub/1112/pg1112.html')
html = response.read()
soup = BeautifulSoup(html, 'html.parser')
my_file = open("Romeo.txt","w")
my_file.write(soup.body.get_text().encode('utf-8'))
my_file.close()
