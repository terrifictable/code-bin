# Code by TerrificTable (https://github.com/TerrificTable)

# idk why i made this, mby someone will find it usefull or not
import requests

# make your gist and split variable nameas and values by "::"
# example url: https://gist.githubusercontent.com/TerrificTable/e599635d6d14dc17e32fe7c71579b6f4/raw/ceb35a20695a86aa4912f4e707863c67ca6d0ea5/test.aaa
content = str(requests.get('YOUR_RAW-gist.githubusercontent-URL').content.decode('utf-8')).replace("'", "").split("\n")

for c in content:
    new_content = c.split("::")

    print(new_content[0] + ": " + new_content[1]) # it will output the variable name and value


# make your gist and split variable nameas and values by "::"
# content = str(requests.get('RAW_gist.githubusercontent_URL').content.decode('utf-8')).replace("'", "").split('::')
# 
# if content[0].lower() == "YOUR_KEYWORD": # use this if you want to get a set keyword
#     print(content[0] + ": " + content[1])
