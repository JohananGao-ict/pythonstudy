import re
#元字符
# \d 匹配数字[0-9] \D相反
# \w 匹配单词[a-zA-Z0-9_] \W相反
# \s 空白字符 \S
#[a-z]{3,6}?    加？表示非贪恋模式，默认贪婪模式
a = 'C|C++|Java|C#|Python|Javasciript'
r = re.findall('Python',a)
if len(r) > 0:
    print('字符串中包含Python') 
b = 'abcd1578_&*!'
r = re.findall('\w',b)
print(r)

# re.sub()

# while True:
#     print(input().strip('吗？')+'!')

