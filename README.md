# Trust Labs Interview Assessment

1. 1000 pages
2. Keyword "Covid-19" + "economy" (or something similar)
---
# Summary
Urls are stored in text files denoting which file I found them in. I did this in a bit of an unconventional manner meaning I had to directly download some files. I used the second and third .war.wat file in the NOV/DEC 2020 bucket, I had 57 and 608 hits respectively. I would have run it on a third file to get 1000 links but I was pressed for time. I didn't automatically download the files and search through them due to issues described below -- long story short I believe environment variables are from hell..
To extract the URLS I extracted the JSON descriptions of the pages from the .warc.wat files and them passed them to extractURLS.py.
This bit of code, recursively traverses the JSON file, if any urls matched the keywords specified in go.py they were added to a list an exported. I searched based on covid and the economy seperately (to maximize my chance of getting a hit) and then took the intersection of those. (please ignore both .json files and the baseTest.py file; they were just files I used for testing)
---
# Process (for better or for worse)
Lets look at go.py --> how to extract info from webpage
Maybe work with WAT extracts? Easy to write code to extract URLS from JSON File
* Because my environment variables have decided they don't like me I am operating assuming the code I have altered in go.py iterates through all the JSON files for NOV/DEC 2020. If I have time I'll try to go back to fix it so I can finally access warcio.iterator
* Decided to just work with the WAT files --> means I dont need to use the warcio.iterator module that refuses to cooperate
* DISASTER, the WAT files are still .warc files, just with embedded JSON; guess I need to use warc.iterator regardless so time to fly blind again
* After writing extractUrls.py (purpose is to parse through JSON and extract info), have come to discover it works but is rather inefficient --> filters out URLS after. Fix: filter out non-urls while doing initial comparisons
  * Inefficienty seems to be a theme; because I cant use the warc package I'm parsing as a text file --> *wildly* inefficient; fix by using warc package
* Passing the json objects correctly, extractUrls.py returning empty list even when searching for "http"
  * Works with test cases/test json file I made, copied json from .wat file to check
  * Recurssion seems to stop after depth of 1 --> keys in dict are dictionaries themselves
  * That not the issue
* Issue found --> if value is a bool it skips to next key for some reason
  * FIXED: I used break instead of continue, rookie mistake
* NOW WORKS --> needed to filter URL by length because sometimes urls are in paragraphs (don't want to copy whole paragraphs)
* Code just takes a while to run --> started running at 4:02, have it set to 100 URLS (don't want it to keep running past my 6 hour limit)
  * Ended running at 4:11 (56 URLS approx. 10 min), reached the end if this .warc.wat file

---
# Problems
1. Need to install warcio.archiveiterator
   1. pip install warcio --> need to mess with env't variables, woohoo!
   2. Fixing my path has taken almost 40 minutes, might just have to work without it so I dont pass in anything blank
   3. 1 hour later the path is fixed but now it can't even find the module, this is turning out to be very bad, how can I search when I cant even access the data...
   4. Time to do this all *blind* because I have tried everything from changing env't variables to manually adding it in my code
2. Need to extract JSON objects from the WAT warc file
   1. All the JSON files are one line, start with {, maybe parse through .warc file like text file and take any lines starting with { and pass them as a JSON?
      1. Yes this worked