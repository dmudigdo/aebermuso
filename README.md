# Aebersold's Musicians

This Python script searches a list of Jamey Aebersold Playalongs for albums by a particular musician.

## Motivation

For the longest time, I have wanted to figure out which JAPs have Ron Carter playing bass on them. Some JAPs (the earlier ones perhaps?) are notoriously known to not have top-notch rhythm section players, and a good guide to picking out the good ones, is to see who played on the album.

## Usage

Dependency: Beautiful Soup. Go [here](https://www.crummy.com/software/BeautifulSoup/) to set it up (if you haven't already). Then, for now, everything is hard-coded, i.e. the muso search name and the source file:

    python aebermuso.py

## Source File

At the moment, for the album musician details I am using an old source file from Wikipedia, ```aebersoldfulllist.html``` included in this repository. It being a Wiki entry, the format is inconsistent, so I had to do some hacks to deal with quirks on individual album entries that would cause a crash (e.g. one album had a non-ASCII character in the title etc.). The [current Wikipedia entry](https://en.m.wikipedia.org/wiki/List_of_songs_in_Aebersold%27s_"Play-A-Long"_series) has even more quirks to deal with, it was easier to use the old file.

## Future Improvements

- Prompt user for muso search keyword
- Scrape it straight from Wikipedia instead of using the included (past-downloaded) file (as I mentioned, this will need some advanced string hacking to pick out the musicians... the Wiki entries are quite inconsistently formatted)
- Make a database of title/musician (ditto)
- Search by title (can already do this on Jamey's site, but good to have for completeness)
- Search by title + musician
- Scrape it from Jamey's site, maybe it's not so inconsistently formatted? Also less likely to change format
- Suggestions?

## Note

Yes, I know I could have just searached [Jamey's site](http://jazzbooks.com/jazz/category/AEBALL), but where's the fun in that?