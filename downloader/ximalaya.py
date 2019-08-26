# coding:utf-8
import sys

from downloader.models.ximalaya import Album

if __name__ == '__main__':
    # if len(sys.argv) < 2:
    #     print('请输入专辑id')
    #     exit(1)
    # album = Album(url=sys.argv[1])
    album = Album(url='https://www.ximalaya.com/lishi/6703398/')
    album.from_ximalaya()
    album.download()
