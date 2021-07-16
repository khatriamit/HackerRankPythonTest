"""

You are given an HTML code snippet of N lines.
Your task is to print start tags, end tags and empty tags separately.

Format your results in the following way:

2
<html><head><title>HTML Parser - I</title></head>
<body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>

Start : html
Start : head
Start : title
End   : title
End   : head
Start : body
-> data-modal-target > None
-> class > 1
Start : h1
End   : h1
Empty : br
End   : body
End   : html
"""

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for attr in attrs:
            print("->", " > ".join(map(str, attr)))

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, data, attrs):
        print("Empty :", data)
        for attr in attrs:
            print("->", " > ".join(map(str, attr)))


html = ""
for i in range(int(input())):
    html += input()
parser = MyHTMLParser()
parser.feed(html)
