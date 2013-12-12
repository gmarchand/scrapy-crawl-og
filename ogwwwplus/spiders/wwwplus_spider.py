from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector

from ogwwwplus.items import OgWwwPlusItem

class WwwplusSpider(CrawlSpider):
	name = "wwwplus"
	allowed_domains = ["www.xxx.fr","yyy.zzz.tv","uuu.vvv.tv"]
	start_urls = ["http://www.xxx.fr","http://yyy.zzz.tv", "http://uuu.vvv.tv/"]
	rules = (
		Rule(SgmlLinkExtractor(allow=('.*',),deny=('/breve\.ajax\.php','/compte\.ajax\.php','/programme\.ajax\.php','/ajax/', )), callback='parse_item', follow = True),
	)

	def parse_item(self, response):
		hxs = HtmlXPathSelector(response)
		item = OgWwwPlusItem()
		item['name'] = self.name
		item['url'] = response.url
		item['referer'] = response.request.headers.get('Referrer', None)
		item['og_url'] = hxs.select('/html/head/meta[contains(@property, "og:url")]/@content').extract()
		item['og_type'] = hxs.select('/html/head/meta[contains(@property, "og:type")]/@content').extract()
		item['og_title'] = hxs.select('/html/head/meta[contains(@property, "og:title")]/@content').extract()
		
		
		item['og_description'] = hxs.select('/html/head/meta[contains(@property, "og:description")]/@content').extract()
		item['og_site_name'] = hxs.select('/html/head/meta[contains(@property, "og:site_name")]/@content').extract()
		
		# IMAGE
		item['og_image'] = hxs.select('/html/head/meta[contains(@property, "og:image")]/@content').extract()
		item['og_image_url'] = hxs.select('/html/head/meta[contains(@property, "og:image_url")]/@content').extract()
		
		# VIDEO
		item['og_video'] = hxs.select('/html/head/meta[contains(@property, "og:video")]/@content').extract()
		item['og_video_url'] = hxs.select('/html/head/meta[contains(@property, "og:video_url")]/@content').extract()
		item['og_video_secure_url'] = hxs.select('/html/head/meta[contains(@property, "og:video:secure_url")]/@content').extract()
		item['og_video_type'] = hxs.select('/html/head/meta[contains(@property, "og:video:type")]/@content').extract()
		item['og_video_width'] = hxs.select('/html/head/meta[contains(@property, "og:video_width")]/@content').extract()
		item['og_video_height'] = hxs.select('/html/head/meta[contains(@property, "og:video_height")]/@content').extract()
		item['video_actor'] = hxs.select('/html/head/meta[contains(@property, "video:actor")]/@content').extract()
		item['video_actor_role'] = hxs.select('/html/head/meta[contains(@property, "video:actor:role")]/@content').extract()
		item['video_director'] = hxs.select('/html/head/meta[contains(@property, "video:director")]/@content').extract()
		item['video_series'] = hxs.select('/html/head/meta[contains(@property, "video:series")]/@content').extract()
		item['video_release_date'] = hxs.select('/html/head/meta[contains(@property, "video:release_date")]/@content').extract()
		item['video_tag'] = hxs.select('/html/head/meta[contains(@property, "video:tag")]/@content').extract()
		
		
		# PROFILE
		item['profile_fname'] = hxs.select('/html/head/meta[contains(@property, "profile:first_name")]/@content').extract()
		item['profile_lname'] = hxs.select('/html/head/meta[contains(@property, "profile:last_name")]/@content').extract()
		item['profile_gender'] = hxs.select('/html/head/meta[contains(@property, "profile:gender")]/@content').extract()
		item['fb_profile'] = hxs.select('/html/head/meta[contains(@property, "fb:profile_id")]/@content').extract()
		
		# ARTICLE
		item['article_published_time'] = hxs.select('/html/head/meta[contains(@property, "article:published_time")]/@content').extract()
		item['article_modified_time'] = hxs.select('/html/head/meta[contains(@property, "article:modified_time")]/@content').extract()
		item['article_section'] = hxs.select('/html/head/meta[contains(@property, "article:section")]/@content').extract()
		item['article_author'] = hxs.select('/html/head/meta[contains(@property, "article:author")]/@content').extract()
		item['article_tag'] = hxs.select('/html/head/meta[contains(@property, "article:tag")]/@content').extract()
		
		# Facebook 
		item['fb_appid'] = hxs.select('/html/head/meta[contains(@property, "fb:app_id")]/@content').extract()
		
		#TWITTER
		item['twitter_card_type'] = hxs.select('/html/head/meta[contains(@name, "twitter:card")]/@value').extract()
		item['twitter_creator'] = hxs.select('/html/head/meta[contains(@name, "twitter:creator")]/@value').extract()
		item['twitter_site'] = hxs.select('/html/head/meta[contains(@name, "twitter:site")]/@value').extract()
		item['twitter_player'] = hxs.select('/html/head/meta[contains(@name, "twitter:player")]/@value').extract()


		return item


class StreetSpider(WwwplusSpider):
	http_user = 'cstreet'
	http_pass = 'cstreet!welcome'
	name = "street"
	allowed_domains = ["xxx.yyy.com"]
	start_urls = ["http://xxx.yyy.com"]
	rules = (
		Rule(SgmlLinkExtractor(allow=('.*',),deny=('/admin/')), callback='parse_item', follow = True),
	)
	
	def parse_item(self, response):
		WwwplusSpider.parse_item(self,response)
