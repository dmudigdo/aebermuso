# Trying to get to work on old version

from bs4 import BeautifulSoup

ifhandle = open("aebersoldfulllist.html")

soup = BeautifulSoup(ifhandle,"lxml")

h2tags = soup('h2')

muso = ""

for h2tag in h2tags:
    # h2 of an album contains 3 elements, other h2s don't
    if len(h2tag.contents) == 3:
        # 2nd element (index 1) of h2 contains title.
        # Most titles are in 'volume <i>title</i>' format, but one (vol 92) is in
        # 'volume title format. Also vol 98 has a non-ASCII character in it. 
        # So instead of just using foo.text, to deal with the above exceptions:
        if len(h2tag.contents[1]) > 1:
            title = h2tag.contents[1].contents[0].encode('utf8') + \
                    h2tag.contents[1].contents[1].contents[0].encode('utf8')
        else:
            title = h2tag.contents[1].contents[0].encode('utf8')
            
        # next <p> sibling of the h2 contains muso list
        musos = h2tag.find_next_sibling('p').text
        if muso in musos:
            print title
            print musos
