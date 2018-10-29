# @Author: Jorrell Templeton
# @Email: jazzonym@gmail.com
# @Date: 10/28/2018 (October 28, 2018)
# @Name: crawl.py

import re
import bs4
import urllib.request as urllib
import requests
import time

nsdeveloper_links = []
# site_links = [] <- Extra functionality
wiki_map = ['Main_Page', 'Current_Development', 'Developer_FAQ', 'Tools', 'Related_Projects', 'Project_Ideas', 'Summer_Projects', 'Installation', 'Troubleshooting', 'User_FAQ', 'HOWTOs', 'Category:Samples', 'Category:Models', 'Education', 'Contributed_Code', 'Papers']

for page in wiki_map:
  page_url = 'https://www.nsnam.org/wiki/' + page
  rawhtml = urllib.urlopen(page_url)
  page_soup = bs4.BeautifulSoup(rawhtml)
  hyperlinks = page_soup.find_all("a", href=True)

  for link in hyperlinks:
    if re.match(r"http:\/\/mailman\.isi\.edu\/pipermail\/ns-developers\/.*", link['href']):
      nsdeveloper_links.append(link)

  """ ------ Extra functionality ---------
    elif re.match(r"\/*((http(s?):\/\/)|www\.).*", link['href']):
      site_links.append(link['href'])
    else:
      site_links.append("https://nsnam.org" + link['href'])
  """

  for archive_link in nsdeveloper_links:
    status = requests.get(archive_link['href']).status_code
    if status >= 200 and status < 300:
      continue # <- Do nothing for live links
    else:
      print("[" + page + "] " + str(archive_link) + "\n") # <- Log dead ns-developer links

  """ -------- Extra functionality ---------    
  for hyperlink in site_links:
    try:
      status = requests.get(hyperlink).status_code
    except:
      continue 
    if status >= 200 and status < 300:
      continue <- Insert code
    else:
      continue <- Insert code
 """   
