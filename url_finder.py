from html.parser import HTMLParser
from urllib.request import urlopen

from urllib import parse

class LinkFinder(HTMLParser):

	def __init__(self, base_url, page_url):
		super().__init__()
		self.base_url = base_url
		self.page_url = page_url
		self.links = set()


	def handle_starttag(self, tag, attrs):
		if tag == 'a':
			for (attribute, value) in attrs:
				if attribute == 'href':
					url = parse.urljoin(self.base_url, value)
					self.links.add(url)
					# print(url)

		



	def page_links(self):
		return self.links


	def error(self, message):
		pass
	
def get_url(page_url):
	html_string = ''
	try:
		response = urlopen(page_url)
		if response.getheader('content-type') =='text/html':
			html_bytes = response.read()
			html_string = html_bytes.decode("utf-8")
		# finder = LinkFinder(Spider.base_url, page_url)
		# finder.feed(html_string)
		print(html_string)
	except:
		print('Error: can not crawl page')
		return set()
	return 0


# result = LinkFinder('http://stats.nba.com/', 'http://stats.nba.com/')
# get_url('http://stats.nba.com/')

