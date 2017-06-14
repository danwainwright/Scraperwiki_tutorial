import scraperwiki
html = scraperwiki.scrape('http://inmo.ie/6022')
import lxml.html
root = lxml.html.fromstring(html) # turn our HTML into an lxml object
td = root.cssselect('td') # get all the <tr> tags
for tr in trs:
     record td.text_content() # just the text inside the HTML tag
for td in tds:
     record = { "td" : td.text_content } # column name and value
     try:
          scraperwiki.sqlite.save(["td"], record) # save the records one by one
     except:
          record = { "td" : "NO ENTRY" } # column name and value
          scraperwiki.sqlite.save([ "td"], record) # save the records one by one
