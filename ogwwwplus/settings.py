# Scrapy settings for ogwwwplus project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'ogwwwplus'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['ogwwwplus.spiders']
NEWSPIDER_MODULE = 'ogwwwplus.spiders'
ITEM_PIPELINES = ['ogwwwplus.pipelines.OgwwwplusPipeline','ogwwwplus.pipelines.OgPipelineMongo']

USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
DEPTH_LIMIT = 3
LOG_LEVEL = 'INFO'
LOG_STDOUT = True
LOG_ENABLED = True
#LOG_FILE=scrapy.log
MONGODB_SERVER = 'localhost'
MONGODB_PORT = 27017
MONGODB_DB = 'scrapy'
MONGODB_COLLECTION = 'items'
MONGODB_UNIQ_KEY = 'url'

