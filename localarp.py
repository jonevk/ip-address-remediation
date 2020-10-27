from arpcleantools import add_vlan_to_list, vlans, vlans_used, devices_used, sites, unneeded_items, sanitize, get_switch
arplist = '''0000.a102.ab83
0000.a104.2ba5
0000.a102.7849
0040.9716.56bd
f4cf.e209.fa8d
0040.9716.56be
0000.a103.40bf
0000.a103.96f4
0040.970c.bb7b
3333.0000.0016
0000.a104.0c2d
0000.a103.b4fc
0040.9716.56bb
0040.970c.bbbe
0040.970c.bc13
00d0.c99e.a01d
0040.970c.bbbd
000b.ab0c.639c
0000.a103.b4f7
0000.a104.19d1
0040.9716.f7c8
0000.a104.1a25
0000.a103.b358
0016.e09e.b3e0
0000.a103.bbf6
0000.a103.b5b9
000e.0cb3.68c9
0000.a104.0c7d
0000.a104.2d85
3333.0000.0001
000b.ab0b.5ed8
0000.a104.1314
0040.970c.bb6a
101f.742c.2cbc
0040.9716.59f1
0000.a105.984c
0040.9716.56ed
74fe.4811.6cc0
0040.9716.56ee
0016.e09c.1e40
0000.a104.0bdc
0040.9716.5972
0000.a104.0bdd
3333.0000.000d
0040.970c.bbed
00d0.c99e.9ea6
0000.a103.5747
000e.0cb3.6a1b
0000.a103.9813
74fe.4800.6eae
0040.970c.b516
0000.a105.92a7
0016.e09c.3140
0000.a104.1a0f
0000.a103.961c
000e.0cb3.6006
0040.9716.f722
0040.9716.f928
0016.e07f.8280
0000.a104.3167
000a.0412.e840
0040.970c.bc34
0016.e0a7.7a80
0040.970c.bb9a
00d0.c99e.a03a
0000.a106.7770
0000.a103.b37b
0000.a104.0c8e
0000.a103.bc66
0016.e09c.4e40
0000.a104.0c90
0000.a104.1a5f
0000.a104.1c6e
74fe.4811.6ce4
0000.a103.f6a6
0000.a103.a179
0000.a102.e253
000b.ab0c.644e
0000.a103.988f
0015.176d.2eb4
0040.9716.f7f2
0000.a104.19a1
0010.f305.7324
000b.ac09.3bc0
0000.a104.19e4
0040.970c.b5c2
0010.f305.7325
0040.9716.fa44
0000.a103.991a
0016.e083.52c0
0040.9716.f6ee
0000.a103.eff1
000b.ab0c.6464
0040.9716.f3c2
0040.970c.bb99
0000.a103.f0d1
00d0.c99e.7c27
0000.a103.bbed
00d0.c99e.7c26
0040.970c.c047
0000.a104.0c8a
0000.a103.96db
0000.a103.96da
0000.a104.2d7a
0000.a103.b43c
0000.a105.9778
0016.e09e.9d20
00d0.c99e.a01c
000b.ac08.e7c0
0000.a104.19df
0000.a10e.7b0d
00d0.c99e.a273
0000.a103.964d
0000.a103.56d7
0000.a103.96d7
0000.a103.b4a4
0000.a103.effd
00d0.c9d8.2a69
74fe.4800.6ead
0000.a104.0b9d
0040.970c.bc11
00d0.c9d8.2a6a
000b.ab0c.2170
00d0.c9d8.2c5f
0000.a103.9910
0000.a10f.c1c7
0000.a105.9259
0000.a103.f6ef
000b.ab08.d49f
0000.a10c.0c37
0000.a104.9ae7
101f.7430.3060
0000.a104.0d72
0000.a103.97ba
101f.7430.3062
0040.9716.fa12
0016.e09e.b360
0000.a104.1968
0040.9716.5753
0040.970c.bbf2
0000.a104.1d2e
0040.9716.59f2
0040.970c.bbf4
0040.9716.f7ea
0040.970c.bbba
0040.9716.68bf
0016.e09c.7440
0000.a104.0cae
0000.a10e.b113
00d0.c9d8.2c60
000b.ab0c.e320
0000.a103.4c75
0016.e09e.e7a0
0040.9716.56bc
00d0.c99e.603c
0000.a103.cb55
0040.970c.bc36
000a.041c.cf40
000e.0cab.86e6
0016.e09c.2780
000e.0cab.8893
0040.970c.bbe4
0040.970c.bbe5
0040.970c.bbeb
0010.f302.0c7b
0010.f302.0c7a
000e.0cb3.67c2
0040.9716.5971
0000.a103.9896
74fe.4811.6cba
0000.a104.1d30
3333.0000.0016
3333.0000.0001
3333.0000.000d
001b.1700.0116'''.strip().splitlines()

ge_list = '''10:1f:74:30:30:60
10:1f:74:2c:2c:bc
00:d0:c9:d8:2c:5f
00:d0:c9:d8:2a:69
74:fe:48:00:6e:ad
00:40:97:16:56:be
00:40:97:16:56:bc
00:40:97:16:59:f2
00:40:97:16:59:72
00:40:97:16:56:ee
'''.strip().splitlines()

for mac in ge_list:
    print(f'{mac} \t {sanitize(mac)[2]}')