# coding:utf-8
from downloader.common.enums.error import Error


class BusinessException(RuntimeError):
    error_code = -1
    error_msg = ''

    def __init__(self, error: Error):
        self.error_code = error.value[0]
        self.error_msg = error.value[1]
