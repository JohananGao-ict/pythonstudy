from urllib import request
import re
#断点调试 坑 7i
class  Spider():
    url = 'https://www.panda.tv/cate/lol'
    root_pattern ='<div class="video-info">([\s\S]*?)</div>'
    name_pattern = '</li>([\s\S]*?)</span>' 
    number_pattern = '<span class="video-number">([\s\S]*?)</span>'

    # 获取数据的页面
    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        #bytes
        htmls = r.read()
        htmls = str(htmls,encoding='utf-8')
        return htmls
    
    # 从页面上抓取数据
    def __analysis(self,htmls):
        root_html = re.findall(Spider.root_pattern, htmls)
        anchors = []
        for html in root_html:
            name = re.findall(Spider.name_pattern, html)
            number = re.findall(Spider.number_pattern, html)
            anchor = {'name':name,'number':number}
            anchors.append(anchor)
        # print(anchors[0])
        return anchors

    # 数据取杂质（空格换行）strip() 字符串去空格换行
    def __refine(self, anchors):
        l = lambda anchor:{
            'name':anchor['name'][0].strip(),
            'number':anchor['number'][0]
            }
        return map(l,anchors) #map类  对字典每一个序列进行l这个函数

    # 对抓取的数据进行排序 reverse=True 倒序
    def __sort(self, anchors):
        anchors = sorted(anchors, key=self.__sort_seed, reverse=True)
        return anchors

    # 给 key 写的函数 说明用那个进行排序
    def __sort_seed(self, anchors):
        r = re.findall('\d*', anchors['number'])
        number = float(r[0])
        if '万' in anchors['number']:
            number *= 10000
        return number

    # 显示排名
    def __show(self, anchors):
        for rank in range(0,len(anchors)):
            print('rank '+ str(rank +1)+'   : '+anchors[rank]['name']+'    '+anchors[rank]['number']+'人')

    # 主程序
    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        anchors =list(self.__refine(anchors))
        print(anchors[0])
        anchors= self.__sort(anchors)
        self.__show(anchors[:20])

s = Spider()
s.go()

