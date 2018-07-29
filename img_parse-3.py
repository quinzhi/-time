# Download image from yandex.re
# the image size is original
# work slow and ez be ban
# u can change the sleep time to chanege the speed


from bs4 import BeautifulSoup
import urllib2
import time
from urlparse import urlsplit
from os.path import basename
def parseImgUrl(url):
    try:
        print '[+] Finding Url for image on '+url
        urlContent = urllib2.urlopen(url)
        soup = BeautifulSoup(urlContent, 'lxml')
        imgurl = soup.findAll('a', {'class' : 'directlink largeimg'})
        return imgurl
    except Exception, e:
        print e

def downloadImages(image):
    print '[+]Downloadng image ...'
    imgcontent = urllib2.urlopen(image).read()
    imgFileName = basename(urlsplit(image)[2])
    imgFile = open(imgFileName,"wb")
    imgFile.write(imgcontent)
    imgFile.close()
    return imgFileName

def main():
    count = 0
    for i in range(4,13):  # the page range
        Url = 'https://yande.re/post?page='+str(i)+'&tags=atago_%28kancolle%29' # the source url
        image = parseImgUrl(Url)
        for i in image:
            count += 1
            if count%20 == 0:  # sleep every 20 times
                time.sleep(20)
            url = i.get('href')
            downloadImages(url)

if __name__ =='__main__':
    main()
