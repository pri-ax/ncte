# If you are running this code for the first time, you should: 
# 1. Make sure you have python installed (this was written on version 2.7)
# 2. Install the the 'newspaper' python package from http://newspaper.readthedocs.io/en/latest/user_guide/install.html#install
# 26

from newspaper import Article
import csv

all_articles = []

with open('/Users/prioberoi/Dropbox/pro bono projects/ncte/media.csv', 'rb') as csvfile:
	media = csv.reader(csvfile, delimiter = ",")
	next(media)

	for row in media:

		eachArticle = []

		media_id = row[1]
		eachArticle.append(media_id)

		url = row[0]
		# this is the media link url
		# print(url)
		url.encode("utf-8")
		eachArticle.append(url)

		article = Article(url)
		# this downloads the content from the url 
		article.download()

		# if you want to see the html for this article, uncomment this code
		# article.html
		try:
			article.parse()
		except:
			continue

		# article title
		# print(article.title)
		title = article.title
		eachArticle.append(title.encode("utf-8"))

		# article authors
		authors = article.authors
		eachArticle.append(", ".join(str(item) for item in authors))

		# date the article was published
		# print(article.publish_date)
		eachArticle.append(article.publish_date)

		# get text from the article
		# print(article.text)
		text = article.text

		# retrieve link for image at the top of the article
		# print(article.top_image)

		# apply some natural language processing on the article
		article.nlp()

		# get keywords from the article
		# print(article.keywords)
		keywords = article.keywords
		eachArticle.append(", ".join(str(item) for item in keywords))

		# get article summary
		# print(article.summary)

		all_articles.append(eachArticle)

	# uncomment the line below to print everything to the console
	# print(all_articles)
	with open('/Users/prioberoi/Dropbox/pro bono projects/ncte/media_details.csv', 'wb') as myfile:
		writer = csv.writer(myfile)
		writer.writerow(['media_id', 'url', 'title', 'authors', 'date_published', 'keywords'])
		writer.writerows(all_articles)

