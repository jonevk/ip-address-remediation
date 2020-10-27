import yaml
import time
my_username = 'jvankle'
my_password = 'passwd'
host_list = []

cisco_hosts = 'cisco_hosts.yml'

with open (cisco_hosts) as f:
    hosts = yaml.safe_load(f)
print(hosts)
for d in hosts:
    print(type(d))
    d.update(username = my_username)
    for k, v in d.items():
        print(v)
