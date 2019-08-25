# coding:utf-8
import sys

from downloader.models.ximalaya import Album

if __name__ == '__main__':
    # if len(sys.argv) < 2:
    #     print('请输入专辑id')
    #     exit(1)
    # album_id = sys.argv[1]
    album_id = '7785486'
    album = Album(id=album_id)
    album.from_ximalaya()
    album.download()
