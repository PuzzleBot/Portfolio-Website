import requests
import unittest

class BlogContent:
    def __init__(self):
        retrieveBlogFromSource()

    def retrieveBlogFromSource(self):
        response = requests.GET()
        self.blogTitle = ""
        self.blogText = ""
        return {"blogTitle":blogTitle, "blogEntry":blogText}

    def cacheBlog(self):
        return

    def toJson(self):
        return {"blogTitle":blogTitle, "blogEntry":blogText}


class testBlogRetrieve(unittest.TestCase):
    def fetchTest():
        testContent = BlogContent()
        testContent.retrieveBlogFromSource()

if __name__ == '__main__':
    unittest.main()
