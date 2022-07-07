# import library
import re
from urllib.request import urlopen

# getting data
url = "https://github.com/shahzaibkhan"
page = urlopen(url)
html = page.read().decode("utf-8")

# Using pattern to find the require data
pattern = "<a.*?Link--primary.*?>.*?</a.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
link = match_results.group()
link_caption = re.sub("<.*?>", "", link)
print(link_caption)