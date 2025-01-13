import re

text = '''{"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},
{"id":10},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}], "errors":[{"code":3,
"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable [153]"}]}
'''


matches = re.findall(r'(?<="id":)(\d+)', text)

numbers = list(map(int, matches))
print(numbers)


# output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 648, 649, 650, 651, 652, 653]
# regex(regular expression) is pattern matchinh tool used to search, validate, extract and manipulate data efficiently
# regex is used for 
# data validation, search and validation, web scraping, file manupulation and programming and automation

