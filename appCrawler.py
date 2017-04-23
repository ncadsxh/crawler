from lxml import html
import requests

class AppCrawler:

	def __init__(self, starting_url, depth):
		self.starting_url = starting_url
		self.depth = depth
		self.current_depth = 0
		self.depth_links = []
		self.appLists = []

	def crawl(self):
		app = self.get_app_from_link(self.starting_url)
		self.appLists.append(app)
		self.depth_links.append(app.links)

		while self.depth > self.current_depth:
			current_links = []
			for link in self.depth_links[self.current_depth]:
				current_app = self.get_app_from_link(link)
				current_links.extend(current_app.links)
				self.appLists.append(current_app)
			self.current_depth += 1
			self.depth_links.append(current_links)





	def get_app_from_link(self, links):
		start_page = requests.get(links)
		tree = html.fromstring(start_page.text)

		name = tree.xpath('//h1[@itemprop="name"]/text()')[0]
		developer = tree.xpath('//div[@class="left"]/h2/text()')[0]
		price = tree.xpath('//div[@class="price"]/text()')[0]
		links = tree.xpath('//div[@class="center-stack"]//*/a[@class="artwork-link"]/@href')

		app = App(name, developer, price, links)

		return app

class App:
	def __init__(self, name, developer, price, links):
		self.name = name
		self.price = price
		self.developer = developer
		self.links = links

	def __str__(self):
		return("name: " + self.name
			+ "\ndeveloper: " + self.developer
			+ "\nprice: " + self.price)


crawler = AppCrawler("https://itunes.apple.com/ca/app/candy-crush-saga/id553834731?mt=8", 2)
crawler.crawl()

for app in crawler.appLists:
	print(app)

