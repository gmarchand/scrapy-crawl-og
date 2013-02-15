# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class OgWwwPlusItem(Item):
    # define the fields for your item here like:
	name = Field()
	url= Field()
	referer = Field()
	og_url= Field()
	og_type= Field()
	og_title= Field()
	og_description= Field()
	og_site_name= Field()
	og_image= Field()
	og_image_url= Field()
	og_video= Field()
	og_video_url= Field()
	og_video_secure_url= Field()
	og_video_type= Field()
	og_video_width= Field()
	og_video_height= Field()
	video_actor= Field()
	video_actor_role= Field()
	video_director= Field()
	video_series= Field()
	video_release_date= Field()
	video_tag= Field()
	profile_fname= Field()
	profile_lname= Field()
	profile_gender= Field()
	fb_profile= Field()
	article_published_time= Field()
	article_modified_time= Field()
	article_section= Field()
	article_author= Field()
	article_tag= Field()
	fb_appid= Field()
	twitter_card_type= Field()
	twitter_creator= Field()
	twitter_site= Field()
	twitter_player= Field()
	
