#from warcio.archiveiterator import ArchiveIterator
import re
import requests
import sys
import extractUrls as e
import json
import json5.parser 

# Formating search criteria for links
#regex = re.compile(
#    "(youtu\.be/|youtube\.com/(watch\?(.*\&)?v=|(embed|v)/))([^?&\"'>]+)"
#)

urlList = []

# Will find urls containing the following phrases
searchParamCovid = ["covid", "corona","Covid","Corona", "新冠病毒"] # JSON search file is case sensistive
searchParamEcon  = ["jobs", "economy", "Economy", "Jobs", "病毒"]


# Searching the 72k files in the NOV/DEC Bucket --> downloaded this file for testing
file_name = "https://commoncrawl.s3.amazonaws.com/crawl-data/CC-MAIN-2020-50/wat.paths.gz"

if len(sys.argv) > 1:
    file_name = sys.argv[1]

# Loop through .warc.wat file (here just opening already downloaded file, switch to parse through fill .gz file later)
# Have the sense this might be inefficient (126k lines means 126k comparison)
with open("CC-MAIN-20201123153826-20201123183826-00637.warc.wat", "r", encoding="utf-8") as wat :
    for line in wat :
        if "{" == line[:1] :
            obj = json.dumps(line)
            cov_list = set(e.extract_urls(obj, searchParamCovid))
            eco_list = set(e.extract_urls(obj, searchParamEcon))
            urlList + list(cov_list.intersection(eco_list)) # Need covid AND economy (Intersection of two sets)

#stream = None
#if file_name.startswith("http://") or file_name.startswith("https://"):
#    stream = requests.get(file_name, stream=True).raw
#else:
#    stream = open(file_name, "rb")

# Loop through all files in stream

# Here its working with warc files --> dont need
#for record in ArchiveIterator(stream):
#    if record.rec_type == "warcinfo":
#        continue
#
#    if not ".com/" in record.rec_headers.get_header(
#        "WARC-Target-URI"
#    ):
#        continue
#
#    entries = entries + 1
#    contents = (
#        record.content_stream()
#        .read()
#        .decode("utf-8", "replace")
#    )
#    m = regex.search(contents)
#    if m:
#        matching_entries = matching_entries + 1
#        hits = hits + 1
#        m = regex.search(contents, m.end())
#
#    while m:
#        m = regex.search(contents, m.end())
#        hits = hits + 1
