import netmiko

device_ip = {
    "R0":"172.31.183.1",
    "R1":"172.31.183.4",
    "R2":"172.31.183.5",
    "R3":"172.31.183.6",
    "R4":"172.31.183.7",
    "R5":"172.31.183.9",
    "S0":"172.31.183.2",
    "S1":"172.31.183.3",
    "S2":"172.31.183.8"
}


def configInterface(device):
    device_param ={
    'device_type': 'cisco_ios',
    'host':   '',
    'username': 'admin',
    'password': 'cisco',
}
    device_param['host'] = device_ip[device]
    ssh = netmiko.ConnectHandler(**device_param)
    commands =["ip access-list standard  ssh","10 permit 172.31.183.0 0.0.0.15","20 permit 10.253.190.0 0.0.0.255", "line vty 0 15","transport input telnet ssh","access-class ssh in"]
    result = ssh.send_config_set(commands)
    print(result)


for i in device_ip:
    configInterface(i)