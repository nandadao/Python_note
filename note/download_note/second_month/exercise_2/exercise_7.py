import requests
import multiprocessing

# 获取章节地址列表
def text():
    list_ = []
    response = requests.get('https://www.17k.com/list/3015690.html')
    html = response.text
    for line in html.split():
        if 'href' in line and 'chapter' in line :
            url = line.split('"')[-2]
            list_.append("www.17k.com"+url)
    return list_

# 传入一个章节地址，和第几章，返回该章节网页内容
def download(url,num):
    response = requests.get('https://'+url)
    txt_ = response.content
    # 存放的位置
    with open('../xs/第%d章.html'%num,mode='wb') as f:
        f.write(txt_)














#
# jobs = []
# num= 0
# for url in text():
#     num += 1
#     p = multiprocessing.Process(target = download,args=(url,num))
#     jobs.append(p)
#     p.start()
#
# [i.join() for i in jobs]