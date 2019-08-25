# coding:utf-8
from enum import Enum, unique


@unique
class Error(Enum):
    ALBUM_ERROR = [100, '专辑错误']
    XIMALAYA_ERROR = [101, '喜马拉雅错误']
    TRACK_ERROR = [102, '单曲错误']
