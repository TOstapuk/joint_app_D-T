# This is the main Python file for our backend.

#from newscatcher import Newscatcher, describe_url
# import Newscatcher as nc
#import json
#import newspaper
import feedparser
import json

#url for rss wired
wired_business_rss = 'https://www.wired.com/feed/category/business/latest/rss'
bleeping_computer_rss = 'https://www.bleepingcomputer.com/feed/'
krebs_onsecurity_rss = 'https://krebsonsecurity.com/feed/'
google_security_rss = 'https://news.google.com/rss/search?q=Cyber+Security'
att_security_rss = 'https://cybersecurity.att.com/site/blog-all-rss'
schneier_security_rss = 'https://www.schneier.com/feed/atom/'
techcrunch_rss = 'https://techcrunch.com/feed/'
thn_security_rss = 'https://feeds.feedburner.com/TheHackersNews'
theverge_rss = 'https://www.theverge.com/rss/index.xml'
nvd_rss = 'https://nvd.nist.gov/feeds/xml/cve/misc/nvd-rss.xml'


#parses the rss url
wired = feedparser.parse(wired_business_rss)
bleeping = feedparser.parse(bleeping_computer_rss)
krebs = feedparser.parse(krebs_onsecurity_rss)
google = feedparser.parse(google_security_rss)
att = feedparser.parse(att_security_rss)
schneier = feedparser.parse(schneier_security_rss)
techcrunch = feedparser.parse(techcrunch_rss)
thn = feedparser.parse(thn_security_rss)
theverge = feedparser.parse(theverge_rss)
nvd = feedparser.parse(nvd_rss)

#take the top 5 entries using arithmetic
for i in range(5):
    #print('\nWired Title' + str(i) + ' - ' + wired.entries[i].title + ' | ' + wired.entries[i].description)
    print('\nBleeping Title' + str(i) + ' - ' + bleeping.entries[i].title + ' | ' + bleeping.entries[i].description)
    print('\nKrebs Title' + str(i) + ' - ' + krebs.entries[i].title + ' | ' + krebs.entries[i].description)
    print('\nNVD Title' + str(i) + ' - ' + nvd.entries[i].title + ' - ' + nvd.entries[i].description)