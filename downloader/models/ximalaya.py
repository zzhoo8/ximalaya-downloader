# coding:utf-8
import requests
from pyquery import PyQuery as pq
from downloader.common.enums.error import Error
from downloader.common.exceptions import BusinessException


class Album(object):
    id = None
    title = None
    nickname = None
    tracks = []

    def __init__(self, **args):
        for key in args.keys():
            if hasattr(self, key):
                setattr(self, key, args[key])

    def from_ximalaya(self) -> None:
        if not self.id:
            raise BusinessException(Error.ALBUM_ERROR)
        # 301跳转
        # curl -L 'https://www.ximalaya.com/album/xxx'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
        }
        resp = requests.get(url='https://www.ximalaya.com/album/' + self.id, headers=headers, allow_redirects=True)
        if resp.status_code != 200:
            raise BusinessException(Error.XIMALAYA_ERROR)
        dom = pq(resp.text)
        # id = anchor_sound_list
        dom = dom('#anchor_sound_list')
        track_doms = dom('ul li')
        tracks = list()
        for track_dom in track_doms:
            track = Track()
            _dom = pq(track_dom)('a')
            track.id = _dom.attr('href')
            track.title = _dom('.title').text()
            tracks.append(track)


class Track(object):
    id = None
    title = None
    play_path = None

    def __init__(self, **args):
        for key in args.keys():
            if hasattr(self, key):
                setattr(self, key, args[key])
