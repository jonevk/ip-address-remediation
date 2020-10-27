class Device:
    '''Class for network devices including cisco routers and switches'''
    def __init__(self, name, ip, mac, type = 'default'):
        self.name = name
        self.ip = ip
        self.mac = mac
        self.type = type


    def oui(self):
        if len(self.mac) == 14:
            return self.mac[:7]


    def macfix(self):
        if '.' in self.mac:
            fixmac = str(self.mac)
            fixmac = fixmac.split()
            print(fixmac)
            print(type(fixmac))
            return fixmac
        return self


    def raw(self):
        pass


    @classmethod
    def from_cisco(cls,line):
        pass

class PA(Device):
    pass

class Cisco(Device):
    pass

class Fortigate(Device):
    pass

test_device = Device('smc-core-c65-1', '172.16.128.144', '0000.0c07.acfc')


if __name__ == '__main__':
    print(f'The device name is: {test_device.name}')
    print(f'The device IP Address is: {test_device.ip}')
    print(f'The device MAC Address is: {test_device.mac}')
    print(f'The device OUI is: {test_device.oui()}')
    test_device.macfix()
    print(f'The post fixed device MAC is: {test_device.mac}')
    print(type(test_device))
    print(dir(test_device))
    print('-'*80)