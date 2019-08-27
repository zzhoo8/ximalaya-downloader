# coding:utf-8
import sys

from downloader.models.ximalaya import Album

if __name__ == '__main__':
    if len(sys.argv) == 2:
        url = sys.argv[1]
    else:
        url = 'https://www.ximalaya.com/lishi/2677885/'
    album = Album(url=url)
    album.from_ximalaya()
    album.download()
