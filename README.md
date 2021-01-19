# Trust Labs Interview Assessment

1. 1000 pages
2. Keyword "Covid-19" + "economy" (or something similar)

# Process (for better or for worse)
Lets look at go.py --> how to extract info from webpage
Maybe work with WAT extracts? Easy to write code to extract URLS from JSON File
* Because my environment variables have decided they don't like me I am operating assuming the code I have altered in go.py iterates through all the JSON files for NOV/DEC 2020. If I have time I'll try to go back to fix it so I can finally access warcio.iterator
* Decided to just work with the WAT files --> means I dont need to use the warcio.iterator module that refuses to cooperate
* DISASTER, the WAT files are still .warc files, just with embedded JSON; guess I need to use warc.iterator regardless so time to fly blind again
* After writing extractUrls.py (purpose is to parse through JSON and extract info), have come to discover it works but is rather inefficient --> filters out URLS after. Fix: filter out non-urls while doing initial comparisons
  * Inefficienty seems to be a theme; because I cant use the warc package I'm parsing as a text file --> *wildly* inefficient; fix by using warc package
# Problems
1. Need to install warcio.archiveiterator
   1. pip install warcio --> need to mess with env't variables, woohoo!
   2. Fixing my path has taken almost 40 minutes, might just have to work without it so I dont pass in anything blank
   3. 1 hour later the path is fixed but now it can't even find the module, this is turning out to be very bad, how can I search when I cant even access the data...
   4. Time to do this all *blind* because I have tried everything from changing env't variables to manually adding it in my code
2. Need to extract JSON objects from the WAT warc file
   1. All the JSON files are one line, start with {, maybe parse through .warc file like text file and take any lines starting with { and pass them as a JSON?
   2. YES --> JSON.parse(__text__)