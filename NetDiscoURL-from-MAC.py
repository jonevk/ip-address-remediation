mac_list = '''68:05:ca:11:e0:f0
00:04:23:c7:71:16
00:0e:0c:60:18:b5
00:16:b9:c6:7b:80
00:0b:ab:c8:fb:f4
00:11:85:6c:83:49
68:05:ca:2a:67:13
40:a8:f0:cb:51:89
00:01:6c:d8:30:4e
00:1d:b3:d8:ae:20
50:65:f3:4b:1f:91
00:0d:05:06:24:6e
64:51:06:61:21:a4
90:1b:0e:6c:36:82
10:0e:7e:f7:a5:80
88:a2:5e:03:b5:c0
00:19:b9:d1:c5:32
00:17:a4:48:5f:59
00:19:bb:ea:f9:96
00:e0:81:74:42:76
00:e0:81:74:42:56
5c:f3:fc:56:e6:28
d8:9d:67:c6:4c:bd
00:d0:c9:e0:69:f5
00:0b:ab:ab:79:81
00:19:0f:12:73:1e
a0:d3:c1:29:11:1b
a0:d3:c1:2b:c2:af
c4:7d:cc:00:dc:30
00:e0:f4:2f:34:91
00:80:92:3d:f3:14
e0:9d:31:b2:80:28'''.strip().splitlines()



print(mac_list)

for mac in mac_list:
    print(f'https://netdisco.ascension.org/search?tab=node&q={mac}&stamps=on&deviceports=on&daterange=&mac_format=IEEE\t{mac}')

