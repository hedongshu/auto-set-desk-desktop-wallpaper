from urllib import request
import ssl
import os
import datetime
import subprocess
ssl._create_default_https_context = ssl._create_unverified_context

root_path = ''  # 设置图片路径, 默认当前路径
root_path = os.getcwd() if root_path == '' else root_path

now = datetime.datetime.now().strftime('%Y-%m-%d')
img_path = root_path + '/' + now + '.png'


def cbk(a, b, c):
    '''回调函数
    @a: 已经下载的数据块
    @b: 数据块大小
    @c: 远程文件大小
    '''
    per = 100 * (a*b) / c
    if per >= 100:
        per = 100
    print('下载图片进度: {}'.format(int(per)))


def set_img(file_url):
    '''设置壁纸
    @file_url: 图片路径
    '''
    SCRIPT = '''/usr/bin/osascript<<END
    tell application "Finder"
    set desktop picture to POSIX file "{}"
    end tell
    '''.format(file_url)
    subprocess.Popen(SCRIPT, shell=True)


def main():
    # 下载图片
    url = 'https://cn.bing.com/th?id=OHR.SalcombeDevon_ZH-CN5806331292_1920x1080.jpg&rf=LaDigue_1920x1080.jpg&pid=hp'

    try:
        res = request.urlretrieve(url, img_path, cbk)
        print('图片存储路径:', img_path)
        set_img(img_path)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
