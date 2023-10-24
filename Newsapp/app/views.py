from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here.
def index(request):
    newsapi=NewsApiClient(api_key="674993bef0974f42bfca1cfe3779b72a")
    top=newsapi.get_top_headlines(sources='techcrunch')
    l=top['articles']
    news=[]
    des=[]
    img=[]
    for i in range(len(l)):
        f=l[i]
        news.append(f['title'])
        des.append(f['description'])
        img.append(f['urlToImage'])
    mylist=zip(news,des,img)
    return render(request,"app/index.html",context={"mylist":mylist})
