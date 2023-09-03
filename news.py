import requests
import emailnews

api_key = "7eea166de041429fac3f4f5c3c8a03fa"
url = "https://newsapi.org/v2/everything?q=tesla" \
      "&sortBy=publishedAt" \
      "&apiKey=7eea166de041429fac3f4f5c3c8a03fa" \
      "&language=en"

request = requests.get(url)
content = request.json()
article = content["articles"]
body = ""

for title in article[0:25]:
    body = body + title['title'] + '\n' + title['description'] + '\n' + title['url'] + 2*'\n'
body = body.encode('utf-8')
emailnews.sent_mail(message=body)
