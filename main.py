'''
Build a program to make a get request to the website, modity the url query with a custom command inputted by a user, then scrape the webiste to return the result as a list.
Then iterate through the list as output back to the user as standard output. 
'''

import requests
import urllib
import bs4 as bs

output = []

base_url = 'https://explainshell.com'

user_input = input("Type what you want to search in Explain Shell: ")

#URL encoding the user input
user_input_changed = urllib.parse.quote(user_input)

r = requests.get(base_url + "/explain?cmd=" + user_input_changed)

#creating bs4 object to parse through
soup = bs.BeautifulSoup(r.text, 'html.parser')

#putting the websites return in a list
for paragraph in soup.find_all('tr'):
    output.append(str(paragraph.text))

#printing the output
if len(output) > 0:
    for data in range(len(output)):
        print(output[data])
else:
    print(f"No page was found for {user_input}")
