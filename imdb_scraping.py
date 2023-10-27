from urllib import request
from urllib.request import Request
from bs4 import BeautifulSoup
import json

def soupfunction(url):
     request_site=Request(url,headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"})
     html=request.urlopen(request_site).read()
     soup=BeautifulSoup(html,'html.parser')
     return soup


def alllink():
    urls=[]
    mymovies=[]
    soup=soupfunction("https://m.imdb.com/chart/top/")
    for i in soup.findAll("a"):
        links=i.get("href")
        urls.append(links)

    urls=["https://m.imdb.com"+x.strip() for x in urls if x is not None and x.startswith("/title/tt")]
    for link in urls:
        if link not in mymovies:
            mymovies.append(link)
    return mymovies

def getmovieInfo():
    datalist=[]
    mymovies=alllink()
    for i in mymovies[:250]:
        soup=soupfunction(i)
        titleClass = soup.find("div", {'class': "sc-acac9414-0 jFcAtv"})
        title = titleClass.find("span").text
        ratingClass = soup.find("div", {"class": "sc-bde20123-2 gYgHoj"})
        rating = ratingClass.find("span").text
        imgClass = soup.find("meta", property="og:image")
        minimal_poster = imgClass['content']
        genreClass = soup.find("div", {"class": "ipc-chip-list__scroller"})
        genre = genreClass.find("span").text
        directorClass = soup.find("div", {"class": "ipc-metadata-list-item__content-container"})
        director = directorClass.find("a").text
        mydata={
            "Name: ": title,
            "Rating: ": rating,
            "Poster: ": minimal_poster,
            "Genre: ": genre,
            "Director: ": director
        }
        datalist.append(mydata)
        print(len(datalist))
    jsonfile=open("finalmovies.json","w")
    json.dump(datalist,jsonfile)
if __name__ == '__main__':
    getmovieInfo()