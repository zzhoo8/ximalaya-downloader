# coding:utf-8
import math
import os
import re

import requests
from pyquery import PyQuery as pq
from downloader.common.enums.error import Error
from downloader.common.exceptions import BusinessException

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}


class Album(object):
    id = None
    title = None
    nickname = None
    url = None
    tracks = []

    def __init__(self, **args):
        for key in args.keys():
            if hasattr(self, key):
                setattr(self, key, args[key])

    def from_ximalaya(self) -> None:
        """
        喜马拉雅专辑内容
        :return:
        """
        if not self.url:
            raise BusinessException(Error.ALBUM_ERROR)
        self.id = re.search('\\d+', self.url)[0]
        # 301跳转
        # curl -L 'https://www.ximalaya.com/album/xxx'
        resp = requests.get(url=self.url, headers=headers, allow_redirects=True)
        if resp.status_code != 200:
            raise BusinessException(Error.XIMALAYA_ERROR)
        dom = pq(resp.text)
        # 专辑标题
        self.title = dom('h1.title').text()
        # id = anchor_sound_list
        dom = dom('#anchor_sound_list')
        # 一页30单曲, 专辑共有声音数, 用来计算分页
        track_count = dom('.head h2')
        track_count = re.search('\(\\d+\)', track_count.text())[0]
        track_count = int(track_count[1:-1])
        print('专辑 %s 共有 %d 声音' % (self.id, track_count))

        tracks = list()
        p = 1
        while p <= math.ceil(track_count / 30):
            print('专辑 %s 第 %d 页的声音列表' % (self.id, p))
            print('%sp%d' % (self.url, p))
            resp = requests.get(url='%sp%d' % (self.url, p), headers=headers, allow_redirects=True)
            if resp.status_code != 200:
                raise BusinessException(Error.XIMALAYA_ERROR)
            dom = pq(resp.text)
            # id = anchor_sound_list
            dom = dom('#anchor_sound_list')
            track_doms = dom('ul li')
            for track_dom in track_doms:
                track = Track()
                _dom = pq(track_dom)('a')
                track.id = _dom.attr('href').split('/')[3]
                track.title = _dom('.title').text()

                # http://www.ximalaya.com/tracks/36107141.json有声音下载地址
                resp = requests.get(url='http://www.ximalaya.com/tracks/%s.json' % track.id, headers=headers)
                if resp.status_code != 200:
                    continue
                resp = resp.json()
                track.play_path = resp.get('play_path')
                tracks.append(track)
            p += 1
        print('专辑 %s 共找到 %d 声音' % (self.id, len(tracks)))
        self.tracks = tracks

    def download(self):
        """
        下载专辑
        :return:
        """
        print('正在下载专辑 %s' % self.id)
        try:
            os.mkdir(self.title)
            os.chdir(self.title)
        except Exception as e:
            print(e)
        for track in self.tracks:
            # print('%s %s' % (track.title, track.play_path))
            track.download()


class Track(object):
    id = None
    title = None
    play_path = None

    def __init__(self, **args):
        for key in args.keys():
            if hasattr(self, key):
                setattr(self, key, args[key])

    def download(self):
        """
        下载声音
        :return:
        """
        # requests下载文件参考 https://blog.csdn.net/mrjiale/article/details/81436380
        if not self.play_path:
            raise BusinessException(Error.TRACK_ERROR)
        print('正在下载Track %s %s, 下载地址 %s' % (self.id, self.title, self.play_path))
        resp = requests.get(url=self.play_path, stream=True)
        extension = self.play_path.split('.')[-1]
        f = open('%s.%s' % (self.title, extension), "wb")
        for chunk in resp.iter_content(chunk_size=512):
            if chunk:
                f.write(chunk)
