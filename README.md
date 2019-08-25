# 喜马拉雅专辑音频downloader

> 喜马拉雅网址 https://www.ximalaya.com/

## python虚拟环境

```bash
➜  ximalaya-downloader git:(develop) python3.6 -m venv venv
```

## 运行  

> 支持"命令行传入专辑id" 和 "写专辑id到程序中" 两种方式

### 命令行

需要修改ximalaya.py，去掉注释即可。

`python -m ximalaya.py 7785486`

### 专辑id写程序中

保留ximalaya.py的注释，`album_id = '7785486'`修改成其他即可。

### 运行结果

```bash
/Users/xxx/Projects/ximalaya-downloader/venv/bin/python /Users/xxx/Projects/ximalaya-downloader/downloader/ximalaya.py
正在下载专辑 7785486
[Errno 17] File exists: '【原创】佛门史话'
正在下载Track 36107141, 下载地址 http://audio.xmcdn.com/group27/M09/29/B3/wKgJW1j7wiPCFIl4ACL33w8P1HY290.m4a
正在下载Track 36167419, 下载地址 http://audio.xmcdn.com/group26/M02/3A/D2/wKgJRlj8oJyz32R6AJutm8zODBQ316.m4a
正在下载Track 36292511, 下载地址 http://audio.xmcdn.com/group27/M00/54/BC/wKgJW1j-q2fja4lEAKEQd8kK44w217.m4a
正在下载Track 36551100, 下载地址 http://audio.xmcdn.com/group27/M03/8B/97/wKgJW1kCXSrx6OMmAI1KxFidoh8038.m4a
正在下载Track 36663488, 下载地址 http://audio.xmcdn.com/group27/M02/A4/6D/wKgJR1kEcSPytXdHAJHFnSBNYHc889.m4a
正在下载Track 36808247, 下载地址 http://aod.tx.xmcdn.com/group27/M03/C4/31/wKgJW1kHH6qwhKtuAI5WCTELNOs365.m4a
正在下载Track 36923114, 下载地址 http://audio.xmcdn.com/group26/M07/E2/3B/wKgJWFkI5qqAISEPAKYlga9h9bU202.m4a
正在下载Track 37106403, 下载地址 http://audio.xmcdn.com/group27/M02/04/95/wKgJR1kLqzPzJSj2AKBwaLoCtqg831.m4a
正在下载Track 37264700, 下载地址 http://aod.tx.xmcdn.com/group26/M08/2B/20/wKgJRlkOVH3hE9oiAI5qlo4vyeo228.m4a
正在下载Track 37445495, 下载地址 http://audio.xmcdn.com/group26/M0B/52/62/wKgJWFkQ6B3ScTaeAI99MKenOhY136.m4a
正在下载Track 37627167, 下载地址 http://audio.xmcdn.com/group26/M00/76/73/wKgJRlkThAGjbGIMAJSuHXEhSmM731.m4a
正在下载Track 37888085, 下载地址 http://audio.xmcdn.com/group27/M02/A7/AB/wKgJW1kXMm2h2frsAJKKZEo3Kno688.m4a
正在下载Track 38164759, 下载地址 http://audio.xmcdn.com/group27/M0A/DF/F2/wKgJR1kbb6Gj-YrXAJ0fpa9d3sk730.m4a
正在下载Track 38422487, 下载地址 http://audio.xmcdn.com/group29/M06/61/6D/wKgJXVkfZ2ehSak6AJU5n2m7CZw729.m4a
正在下载Track 38878819, 下载地址 http://audio.xmcdn.com/group29/M06/F5/73/wKgJWVkl9urSERnDAKHbHRqpInc163.m4a
正在下载Track 39357430, 下载地址 http://audio.xmcdn.com/group28/M03/F4/FF/wKgJSFkt7tij7Q3bAJbTUR9Ohwk943.m4a
正在下载Track 39826306, 下载地址 http://audio.xmcdn.com/group29/M07/63/B3/wKgJXVk0njORErBTALQkfHCklFA920.m4a
正在下载Track 40235425, 下载地址 http://audio.xmcdn.com/group28/M09/BB/44/wKgJSFk51K2ydDoFALI3FnKP6Zc279.m4a
正在下载Track 40627408, 下载地址 http://aod.tx.xmcdn.com/group29/M01/00/C7/wKgJWVk_GVTScm4HAIrk-aQVVo8124.m4a
正在下载Track 40937861, 下载地址 http://audio.xmcdn.com/group29/M07/40/1B/wKgJWVlDEMLBOA_dAKKJ3NR3BbU362.m4a

Process finished with exit code 0
```