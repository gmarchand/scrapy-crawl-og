# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
import csv
import os
import pymongo
from scrapy.conf import settings
from scrapy import log

class OgwwwplusPipeline(object):

	def __init__(self):
		self.ainit = ['url', 'referer','og_url','og_type','og_title','og_description','og_site_name','og_image','fb_appid','twitter_card_type','twitter_creator','twitter_site']
		# PROFILE
		self.profile = csv.writer(open('wwwplus_profile.csv', 'wb'),dialect=csv.excel)
		self.aprofile = ['profile_fname','profile_lname','profile_gender','fb_profile']
		self.aprofile.extend(self.ainit)
		self.profile.writerow(self.aprofile)

		# VIDEO
		self.video = csv.writer(open('wwwplus_video.csv', 'wb'),dialect=csv.excel)
		self.avideo = ['og_video','og_video_secure_url','og_video_type','video_actor','video_actor_role','video_director','video_series','video_release_date','video_tag','twitter_player']
		self.avideo.extend(self.ainit)
		self.video.writerow(self.avideo)

		# ARTICLE
		self.article = csv.writer(open('wwwplus_article.csv', 'wb'),dialect=csv.excel)
		self.aarticle = ['article_published_time','article_modified_time','article_section','article_author','article_tag']
		self.aarticle.extend(self.ainit)
		self.article.writerow(self.aarticle)
		
		#DEFAULT
		self.default = csv.writer(open('wwwplus_default.csv', 'wb'),dialect=csv.excel)
		self.default.writerow(self.ainit)

		
	def process_item(self, item, spider):
		ogType = item['og_type']
		strOgType = "".join(ogType)
		asOgType = strOgType.encode('latin-1')
		
		if strOgType == 'profile':
			log.msg("Item wrote to Profile CSV",level=log.INFO, spider=spider)
			self.profile.writerow([item[s] for s in self.aprofile])
		elif strOgType.startswith('video') or strOgType.startswith('tv'):
			log.msg("Item wrote to Video CSV",level=log.INFO, spider=spider)
			self.video.writerow([item[s] for s in self.avideo])
		elif strOgType == 'article':
			log.msg("Item wrote to Article CSV",level=log.INFO, spider=spider)
			self.article.writerow([item[s] for s in self.aarticle])
		else:
			log.msg("Item wrote to Default CSV",level=log.INFO, spider=spider)
			self.default.writerow([item[s] for s in self.ainit])
		#os.system("pause")
		return item

		
class OgPipelineMongo(object):

	def __init__(self):
	
		connection = pymongo.Connection(settings['MONGODB_SERVER'], settings['MONGODB_PORT'])
		# connexion a la bdd
		self.db = connection[settings['MONGODB_DB']]
		self.collection = self.db[settings['MONGODB_COLLECTION']]
		# purge de la base
		self.collection.remove()
		if self.__get_uniq_key() is not None:
			self.collection.create_index(self.__get_uniq_key(), unique=True)
		
		
	def process_item(self, item, spider):
		if self.__get_uniq_key() is None:
			self.collection.insert(dict(item))
		else:
			self.collection.update(
							{self.__get_uniq_key(): item[self.__get_uniq_key()]},
							dict(item),
							upsert=True)  
		log.msg("Item wrote to MongoDB database %s/%s" %
					(settings['MONGODB_DB'], settings['MONGODB_COLLECTION']),
					level=log.INFO, spider=spider)  
		return item

	def __get_uniq_key(self):
		if not settings['MONGODB_UNIQ_KEY'] or settings['MONGODB_UNIQ_KEY'] == "":
			return None
		return settings['MONGODB_UNIQ_KEY']