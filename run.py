# coding:utf-8
import sys

from downloader.models.ximalaya import Album

if __name__ == '__main__':
    if len(sys.argv) == 2:
        # 命令行引入专辑url
        url = sys.argv[1]
    else:
        # 直接写专辑url到变量中
        url = 'https://www.ximalaya.com/lishi/11538383/'
    album = Album(url=url)
    album.from_ximalaya()
    album.download()
