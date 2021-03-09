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


def configOSPF(device,network,wildcard):
    device_param ={
    'device_type': 'cisco_ios',
    'host':   '',
    'username': 'admin',
    'password': 'cisco',
}
    device_param['host'] = device_ip[device]
    ssh = netmiko.ConnectHandler(**device_param)
    commands =["router ospf 1", "network "+network+" "+wildcard+" area 0"]
    result = ssh.send_config_set(commands)
    print(result)


configOSPF('R1', '172.31.183.16','0.0.0.15')
configOSPF('R1', '172.31.183.32','0.0.0.15')
configOSPF('R1', '172.20.183.4', '0.0.0.0')

configOSPF('R2', '172.31.183.16','0.0.0.15')
configOSPF('R2', '172.31.183.48','0.0.0.15')
configOSPF('R2', '172.20.183.5', '0.0.0.0')

configOSPF('R3', '172.31.183.32','0.0.0.15')
configOSPF('R3', '172.31.183.48','0.0.0.15')
configOSPF('R3', '172.31.183.64','0.0.0.15')
configOSPF('R3', '172.20.183.6', '0.0.0.0')

configOSPF('R4', '172.31.183.64','0.0.0.15')
configOSPF('R4', '172.20.183.7', '0.0.0.0')

configOSPF('R5', '172.31.183.64','0.0.0.15')
configOSPF('R5', '172.20.183.9', '0.0.0.0')
