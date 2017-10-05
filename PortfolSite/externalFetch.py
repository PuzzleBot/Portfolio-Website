# https://stackoverflow.com/questions/29153271/sending-tls-1-2-request-in-python-2-6

import urllib2
import ssl
import json

class XKCDcontent:
    def __init__(self):
        self.retrieveComicFromSource()

    def retrieveComicFromSource(self):
        # Specify TLS 1.2
        ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)

        # Send a request to XKCD, get the latest comic
        url = 'https://xkcd.com/info.0.json'
        response = urllib2.urlopen(url, context=ctx)
        responseContent = response.read()
        if response.getcode() < 400:
            responseDict = json.loads(responseContent)
            self.title = responseDict["safe_title"]
            self.hoverText = responseDict["alt"]
            self.comicNumber = responseDict["num"]
            self.imageLink = responseDict["img"]
        return {"xkcdTitle":self.title, "xkcdHoverText":self.hoverText, "xkcdComicNum":self.comicNumber, "xkcdImageLink":self.imageLink}

    def cacheComic(self):
        return

    def toJson(self):
        return {"xkcdTitle":self.title, "xkcdHoverText":self.hoverText, "xkcdComicNum":self.comicNumber, "xkcdImageLink":self.imageLink}
