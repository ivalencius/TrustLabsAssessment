from warcio.archiveiterator import ArchiveIterator
import re
import requests
import sys

# Formating search criteria for links
regex = re.compile(
    "(youtu\.be/|youtube\.com/(watch\?(.*\&)?v=|(embed|v)/))([^?&\"'>]+)"
)

entries = 0
matching_entries = 0
hits = 0

# Searching the 72k files in the NOV/DEC Bucket
file_name = "https://commoncrawl.s3.amazonws.com/CC-MAIN-2020-50/wat.paths.gz"

if len(sys.argv) > 1:
    file_name = sys.argv[1]

stream = None
if file_name.startswith("http://") or file_name.startswith(
    "https://"
):
    stream = requests.get(file_name, stream=True).raw
else:
    stream = open(file_name, "rb")

# Here its filtering out files that arent warcinfo --> change to WAT
for record in ArchiveIterator(stream):
    if record.rec_type == "watinfo":
        continue

    if not ".com/" in record.rec_headers.get_header(
        "WARC-Target-URI"
    ):
        continue

    entries = entries + 1
    contents = (
        record.content_stream()
        .read()
        .decode("utf-8", "replace")
    )
    m = regex.search(contents)
    if m:
        matching_entries = matching_entries + 1
        hits = hits + 1
        m = regex.search(contents, m.end())

    while m:
        m = regex.search(contents, m.end())
        hits = hits + 1

print(
    "Python: "
    + str(hits)
    + " matches in "
    + str(matching_entries)
    + "/"
    + str(entries)
)