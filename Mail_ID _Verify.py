import re

string = "amit@example.com, amit@abc.com, amit@amit"
pattern = r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)'

result = re.findall(pattern, string)
print(result)