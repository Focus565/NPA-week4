import netmiko
import re

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


def configNAT(device):
    device_param ={
    'device_type': 'cisco_ios',
    'host':   '',
    'username': 'admin',
    'password': 'cisco',
}
    device_param['host'] = device_ip[device]
    ssh = netmiko.ConnectHandler(**device_param)
    commands =["interface g0/1","ip nat inside","interface g0/2","ip nat outside","exit","ip access-list standard nat","10 permit 172.31.183.0 0.0.0.255","exit","ip nat inside source list nat interface g0/2 overload"]
    result = ssh.send_config_set(commands)
    # result = ssh.send_command("show lldp")
    print(result)


configNAT("R5")