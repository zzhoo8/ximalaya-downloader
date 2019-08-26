# 喜马拉雅专辑音频downloader

> 喜马拉雅网址 https://www.ximalaya.com/

* 20190826 支持声音数30以上的专辑

## python虚拟环境

```bash
➜  ximalaya-downloader git:(develop) python3.6 -m venv venv
```

## 运行  

> 支持"命令行传入专辑url" 和 "写专辑url到程序变量中" 两种方式

### 命令行

需要修改ximalaya.py，去掉注释即可。

`python -m ximalaya.py https://www.ximalaya.com/lishi/6703398/`

### 专辑id写程序中

保留ximalaya.py的注释，`album = Album(url='https://www.ximalaya.com/lishi/6703398/')`修改成其他即可。

### 运行结果

```bash
专辑 6703398 共有 46 声音
专辑 6703398 第 1 页的声音列表
专辑 6703398 第 2 页的声音列表
正在下载专辑 6703398
[Errno 17] File exists: '【原创】美国史话'
正在下载Track 30343127 【原创】美国史话（1）香料的故事, 下载地址 http://audio.xmcdn.com/group25/M0B/7B/5E/wKgJNlifOY-RkWysAHYCYxXeyO8150.m4a
正在下载Track 30343281 【原创】美国史话（2）大航海时代, 下载地址 http://audio.xmcdn.com/group24/M08/7A/1E/wKgJMFifOvnT-I05AHdbe_FzGOU522.m4a
正在下载Track 30343314 【原创】美国史话（3）登上新大陆, 下载地址 http://aod.tx.xmcdn.com/group25/M05/7B/68/wKgJMVifO3fgP8VVALXwGkFRR8I519.m4a
正在下载Track 30347530 【原创】美国史话（4）土著的命运, 下载地址 http://aod.tx.xmcdn.com/group21/M00/79/EF/wKgJKFifq3ORCzMOAKTVO5aFI4E370.m4a
正在下载Track 30347560 【原创】美国史话（5）罪恶的开始, 下载地址 http://audio.xmcdn.com/group23/M07/7C/9E/wKgJL1ifq93z9k6iAIc2OlA4z30549.m4a
正在下载Track 30357253 【原创】美国史话（6）英国人来了, 下载地址 http://audio.xmcdn.com/group24/M02/7B/30/wKgJMFif3GXQWeqnAIWg8pFj1Yo568.m4a
正在下载Track 30357309 【原创】美国史话（7）五月花传奇, 下载地址 http://audio.xmcdn.com/group22/M03/7C/A3/wKgJM1if3MaAHw9TAMOhQoT7U6E529.m4a
正在下载Track 30412821 【原创】美国史话（8）日子还不错, 下载地址 http://aod.tx.xmcdn.com/group23/M0A/80/DE/wKgJNFihG_fDs0z9AJ608UqC56I660.m4a
正在下载Track 30471269 【原创】美国史话（9）我不想缴税, 下载地址 http://audio.xmcdn.com/group22/M0A/84/3E/wKgJLliiOi6DnhEbAJ1tfCRQ_3I757.m4a
正在下载Track 30541025 【原创】美国史话（10）打响第一枪, 下载地址 http://audio.xmcdn.com/group21/M04/85/EC/wKgJLVijgDbA87mDAI3O7eqMVWY930.m4a
正在下载Track 30611543 【原创】美国史话（11）枪口的方向, 下载地址 http://aod.tx.xmcdn.com/group21/M0A/8A/36/wKgJKFiky_7DUfX4ALN4rSaK_AY817.m4a
正在下载Track 30681827 【原创】美国史话（12）我们胜利了, 下载地址 http://audio.xmcdn.com/group23/M07/91/7E/wKgJL1imI0bhxPAjAJxHzG0cWEI601.m4a
正在下载Track 30749910 【原创】美国史话（13）终知柴米贵, 下载地址 http://aod.tx.xmcdn.com/group22/M01/95/1C/wKgJLlincSag1IOtAKM7iTThC8w656.m4a
正在下载Track 30815220 感激，承诺和其他, 下载地址 http://aod.tx.xmcdn.com/group23/M08/99/60/wKgJNFiolZfhpjjlAAtV7MI-3t8551.m4a
正在下载Track 30815641 【原创】美国史话（14）闭门造宪法, 下载地址 http://audio.xmcdn.com/group25/M00/98/D5/wKgJNliot92Tt07aANRlfVTXdLY594.m4a
正在下载Track 30879364 【原创】美国史话（15）中国皇后号, 下载地址 http://audio.xmcdn.com/group25/M01/9C/94/wKgJMVipsZmTCkiYAKZIvvCDq6Q832.m4a
正在下载Track 30952895 【原创】美国史话（16）投奔党组织, 下载地址 http://audio.xmcdn.com/group22/M05/A1/42/wKgJM1irBzjjQdiYALB4sJ0EVjY949.m4a
正在下载Track 31035634 【原创】美国史话（17）神奇的法官, 下载地址 http://aod.tx.xmcdn.com/group21/M09/A4/32/wKgJKFisvHiDjKvNAKval7Q-8O0925.m4a
正在下载Track 31193810 【原创】美国史话（18）战争与银行, 下载地址 http://audio.xmcdn.com/group22/M03/B0/33/wKgJM1ivWZ_jPUbaAMdbvjlhKdQ706.m4a
正在下载Track 31325421 【原创】美国史话（19）猛人安德鲁, 下载地址 http://audio.xmcdn.com/group24/M06/B7/0A/wKgJNVixklqjuzF1ALyBc7GHMxM525.m4a
正在下载Track 31485085 【原创】美国史话（20）血泪满西路, 下载地址 http://audio.xmcdn.com/group25/M07/C2/16/wKgJNli0mJTT7gA4AKNNKHUZ8Ho557.m4a
正在下载Track 31635266 【原创】美国史话（21）孤星共和国, 下载地址 http://audio.xmcdn.com/group22/M06/CB/8F/wKgJM1i3SNPRVTgDALZJrIrO4Po542.m4a
正在下载Track 31787398 【原创】美国史话（22）西进与奴隶, 下载地址 http://audio.xmcdn.com/group22/M08/D1/94/wKgJLli57p2jBXRmAKkkBoFQtbk250.m4a
正在下载Track 31907327 【原创】美国史话（23）林肯的轨迹, 下载地址 http://audio.xmcdn.com/group18/M09/B4/42/wKgJJVi752yha_UhAKaZgx8tmAk624.m4a
正在下载Track 32024103 【原创】美国史话（24）挥刀向弟兄, 下载地址 http://audio.xmcdn.com/group23/M08/DA/CA/wKgJL1i97GvRM0fXAMRkjnjykDw246.m4a
正在下载Track 32178156 【原创】美国史话（25）弹劾约翰逊, 下载地址 http://audio.xmcdn.com/group18/M04/BD/B9/wKgJJVjAjHLDKkwMAMDI6Zzr6n4022.m4a
正在下载Track 32255846 【原创】美国史话（26）埋骨枕木下, 下载地址 http://audio.xmcdn.com/group21/M06/DF/41/wKgJLVjB2a-T74HwAMcpzm2JXVQ748.m4a
正在下载Track 32403251 【原创】美国史话（27）最好的时代, 下载地址 http://aod.tx.xmcdn.com/group17/M09/C6/76/wKgJJFjEHCuAEAKZAL1AWRwj0wg009.m4a
正在下载Track 32536184 【原创】美国史话（28）最坏的时代, 下载地址 http://aod.tx.xmcdn.com/group23/M06/E7/E6/wKgJL1jGeufTKzXOALluYUzrs44420.m4a
正在下载Track 32661142 【原创】美国史话（29）进步的时代, 下载地址 http://aod.tx.xmcdn.com/group27/M08/05/32/wKgJR1jIXLOgw2QFALCe2-Pq1JA367.m4a
正在下载Track 30343127 【原创】美国史话（1）香料的故事, 下载地址 http://aod.tx.xmcdn.com/group25/M0B/7B/5E/wKgJNlifOY-RkWysAHYCYxXeyO8150.m4a
正在下载Track 30343281 【原创】美国史话（2）大航海时代, 下载地址 http://audio.xmcdn.com/group24/M08/7A/1E/wKgJMFifOvnT-I05AHdbe_FzGOU522.m4a
正在下载Track 30343314 【原创】美国史话（3）登上新大陆, 下载地址 http://audio.xmcdn.com/group25/M05/7B/68/wKgJMVifO3fgP8VVALXwGkFRR8I519.m4a
正在下载Track 30347530 【原创】美国史话（4）土著的命运, 下载地址 http://audio.xmcdn.com/group21/M00/79/EF/wKgJKFifq3ORCzMOAKTVO5aFI4E370.m4a
正在下载Track 30347560 【原创】美国史话（5）罪恶的开始, 下载地址 http://audio.xmcdn.com/group23/M07/7C/9E/wKgJL1ifq93z9k6iAIc2OlA4z30549.m4a
正在下载Track 30357253 【原创】美国史话（6）英国人来了, 下载地址 http://aod.tx.xmcdn.com/group24/M02/7B/30/wKgJMFif3GXQWeqnAIWg8pFj1Yo568.m4a
正在下载Track 30357309 【原创】美国史话（7）五月花传奇, 下载地址 http://audio.xmcdn.com/group22/M03/7C/A3/wKgJM1if3MaAHw9TAMOhQoT7U6E529.m4a
正在下载Track 30412821 【原创】美国史话（8）日子还不错, 下载地址 http://audio.xmcdn.com/group23/M0A/80/DE/wKgJNFihG_fDs0z9AJ608UqC56I660.m4a
正在下载Track 30471269 【原创】美国史话（9）我不想缴税, 下载地址 http://audio.xmcdn.com/group22/M0A/84/3E/wKgJLliiOi6DnhEbAJ1tfCRQ_3I757.m4a
正在下载Track 30541025 【原创】美国史话（10）打响第一枪, 下载地址 http://aod.tx.xmcdn.com/group21/M04/85/EC/wKgJLVijgDbA87mDAI3O7eqMVWY930.m4a
正在下载Track 30611543 【原创】美国史话（11）枪口的方向, 下载地址 http://audio.xmcdn.com/group21/M0A/8A/36/wKgJKFiky_7DUfX4ALN4rSaK_AY817.m4a
正在下载Track 30681827 【原创】美国史话（12）我们胜利了, 下载地址 http://audio.xmcdn.com/group23/M07/91/7E/wKgJL1imI0bhxPAjAJxHzG0cWEI601.m4a
正在下载Track 30749910 【原创】美国史话（13）终知柴米贵, 下载地址 http://audio.xmcdn.com/group22/M01/95/1C/wKgJLlincSag1IOtAKM7iTThC8w656.m4a
正在下载Track 30815220 感激，承诺和其他, 下载地址 http://audio.xmcdn.com/group23/M08/99/60/wKgJNFiolZfhpjjlAAtV7MI-3t8551.m4a
正在下载Track 30815641 【原创】美国史话（14）闭门造宪法, 下载地址 http://audio.xmcdn.com/group25/M00/98/D5/wKgJNliot92Tt07aANRlfVTXdLY594.m4a
正在下载Track 30879364 【原创】美国史话（15）中国皇后号, 下载地址 http://audio.xmcdn.com/group25/M01/9C/94/wKgJMVipsZmTCkiYAKZIvvCDq6Q832.m4a
正在下载Track 30952895 【原创】美国史话（16）投奔党组织, 下载地址 http://audio.xmcdn.com/group22/M05/A1/42/wKgJM1irBzjjQdiYALB4sJ0EVjY949.m4a
正在下载Track 31035634 【原创】美国史话（17）神奇的法官, 下载地址 http://audio.xmcdn.com/group21/M09/A4/32/wKgJKFisvHiDjKvNAKval7Q-8O0925.m4a
正在下载Track 31193810 【原创】美国史话（18）战争与银行, 下载地址 http://audio.xmcdn.com/group22/M03/B0/33/wKgJM1ivWZ_jPUbaAMdbvjlhKdQ706.m4a
正在下载Track 31325421 【原创】美国史话（19）猛人安德鲁, 下载地址 http://audio.xmcdn.com/group24/M06/B7/0A/wKgJNVixklqjuzF1ALyBc7GHMxM525.m4a
正在下载Track 31485085 【原创】美国史话（20）血泪满西路, 下载地址 http://audio.xmcdn.com/group25/M07/C2/16/wKgJNli0mJTT7gA4AKNNKHUZ8Ho557.m4a
正在下载Track 31635266 【原创】美国史话（21）孤星共和国, 下载地址 http://aod.tx.xmcdn.com/group22/M06/CB/8F/wKgJM1i3SNPRVTgDALZJrIrO4Po542.m4a
正在下载Track 31787398 【原创】美国史话（22）西进与奴隶, 下载地址 http://aod.tx.xmcdn.com/group22/M08/D1/94/wKgJLli57p2jBXRmAKkkBoFQtbk250.m4a
正在下载Track 31907327 【原创】美国史话（23）林肯的轨迹, 下载地址 http://audio.xmcdn.com/group18/M09/B4/42/wKgJJVi752yha_UhAKaZgx8tmAk624.m4a
正在下载Track 32024103 【原创】美国史话（24）挥刀向弟兄, 下载地址 http://aod.tx.xmcdn.com/group23/M08/DA/CA/wKgJL1i97GvRM0fXAMRkjnjykDw246.m4a
正在下载Track 32178156 【原创】美国史话（25）弹劾约翰逊, 下载地址 http://audio.xmcdn.com/group18/M04/BD/B9/wKgJJVjAjHLDKkwMAMDI6Zzr6n4022.m4a
正在下载Track 32255846 【原创】美国史话（26）埋骨枕木下, 下载地址 http://audio.xmcdn.com/group21/M06/DF/41/wKgJLVjB2a-T74HwAMcpzm2JXVQ748.m4a
正在下载Track 32403251 【原创】美国史话（27）最好的时代, 下载地址 http://audio.xmcdn.com/group17/M09/C6/76/wKgJJFjEHCuAEAKZAL1AWRwj0wg009.m4a
正在下载Track 32536184 【原创】美国史话（28）最坏的时代, 下载地址 http://audio.xmcdn.com/group23/M06/E7/E6/wKgJL1jGeufTKzXOALluYUzrs44420.m4a
正在下载Track 32661142 【原创】美国史话（29）进步的时代, 下载地址 http://audio.xmcdn.com/group27/M08/05/32/wKgJR1jIXLOgw2QFALCe2-Pq1JA367.m4a
```