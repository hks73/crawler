import urllib
import json
from TwitterSearch import *

def get_photos(search_terms):
	try:
		tso = TwitterSearchOrder() # create a TwitterSearchOrder object
		tso.setKeywords(search_terms) # let's define all words we would like to have a look for
		tso.setLanguage('en') # we want to see German tweets only
		tso.setCount(40) # please dear Mr Twitter, only give us 7 results per page
		tso.setIncludeEntities(True) # and don't give us all those entity information

		# it's about time to create a TwitterSearch object with our secret tokens
		ts = TwitterSearch(
			consumer_key = 'b3RrA25ftevuRjUAtsiOv1ZKG',
			consumer_secret = '80rD93QtkiQphVR6ueJ3PPtaieoixOTb0EJWQ6YQh9eDMCVx9z',
			access_token = '16329367-vBuNh4kcRk1ID6S3sANokf0HDYRoAzBu9mVdVA5CU',
			access_token_secret = '9wlkuq4YeCS8QP61huKIG7fy10Gi6SrKe6OhkBm9R9hpX'
		 )

		total = 0

		list_of_media = []

		for tweet in ts.searchTweetsIterable(tso): # this is where the fun actually starts :)
			total += 1
			try:
				ent = tweet[u'entities']
				if u'media' in ent:
					media = ent[u'media']
					photo_url = media[0]['media_url']
					list_of_media.append(photo_url)
			except:
				pass

		print total
		
		return json.dumps(list_of_media)

	except TwitterSearchException as e: # take care of all those ugly errors if there are some
		print(e)

def construct_query(terms_list):
	#terms will be ORed
	term=''
	for i in terms_list:
		if term != '':
			term = term+" OR "+i
		else:
			term = i

	term = urllib.quote_plus(term)
	return term


if __name__ == '__main__':
	terms = ['osdc', '#osdc', 'osdconf'	, '#osdconf']

	query = construct_query(terms)
	print get_photos([query])