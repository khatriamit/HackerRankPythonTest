"""

 
TODO 1:
CSS colors are defined using a hexadecimal (HEX) notation for the combination of Red, Green, and Blue color values (RGB).
Specifications of HEX Color Code

■ It must start with a '#' symbol.
■ It can have  3 or 6  digits.
■ Each digit is in the range of 0  to F. (1,...,9,0,A,B,C,D,E and F).
■  A-F letters can be lower case. (a,b,c,d,e and f are also valid digits).
Valid Hex Color Codes
#FFF
#025
#F0A1FB
Invalid Hex Color Codes
#fffabg
#abcf
#12365erff
You are given N lines of CSS code. Your task is to print all valid Hex Color Codes, in order of their occurrence from top to bottom.
CSS Code Pattern
Selector
{
	Property: Value;
}
Input Format
The first line contains N, the number of code lines.
The next N lines contains CSS Codes.
Constraints  0 < N < 50
Output Format: Output the color codes with '#' symbols on separate lines.
Sample Input
11
#BED
{
    color: #FfFdF8; background-color:#aef;
    font-size: 123px;
    background: -webkit-linear-gradient(top, #f9f9f9, #fff);
}
#Cab
{
    background-color: #ABC;
    border: 2px dashed #fff;
}
Sample Output
#FfFdF8
#aef
#f9f9f9
#fff
#ABC
#fff

ss_list=[
    '#BED',
    '{',
    '    color: #FfFdF8; background-color:#aef;',
    '    font-size: 123px;', '',
    '}',
    '#Cab',
    '{',
    '    background-color: #ABC;',
    '    border: 2px dashed #fff;',
    '}'
]
sstr='#BED{    color: #FfFdF8; background-color:#aef;    font-size: 123px;}#Cab{    background-color: #ABC;    border: 2px dashed #fff;}'
"""

import re

T = int(input())
in_css = False
for _ in range(T):
    s = input()
    if "{" in s:
        in_css = True
    elif "}" in s:
        in_css = False
    elif in_css:
        for color in re.findall("#[0-9a-fA-F]{3,6}", s):
            print(color)
