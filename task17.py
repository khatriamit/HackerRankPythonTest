"""

You are given an HTML code snippet of  lines. 
Your task is to print the single-line comments, multi-line comments and the data.
Print the result in the following format:

Sample Input
4
<!--[if IE 9]>IE9-specific content
<![endif]-->
<div> Welcome to HackerRank</div>
<!--[if IE 9]>IE9-specific content<![endif]-->


Sample Output
>>> Multi-line Comment
[if IE 9]>IE9-specific content
<![endif]
>>> Data
 Welcome to HackerRank
>>> Single-line Comment
[if IE 9]>IE9-specific content<![endif]
Current Buffer (saved locally, editable)   
"""

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if "\n" not in data:
            print(">>> Single-line Comment")
            print(data)
        elif "\n" in data:
            print(">>> Multi-line Comment")
            print(data)

    def handle_data(self, data):
        if data != "\n":
            print(">>> Data")
            print(data)


html = ""
for i in range(int(input())):
    html += input()
parser = MyHTMLParser()
parser.feed(html)
