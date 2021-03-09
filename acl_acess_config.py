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


def configACL(device,interface):
    device_param ={
    'device_type': 'cisco_ios',
    'host':   '',
    'username': 'admin',
    'password': 'cisco',
}
    device_param['host'] = device_ip[device]
    ssh = netmiko.ConnectHandler(**device_param)
    commands =["ip access-list extended mgnAccess","10 deny ip any 172.31.183.0 0.0.0.15","20 permit ip any any", "interface "+interface,"ip access-group mgnAccess in"]
    result = ssh.send_config_set(commands)
    print(result)


configACL('R1','g0/1')
configACL('R1','g0/2')

configACL('R2','g0/1')
configACL('R2','g0/2')

configACL('R3', 'g0/1')
configACL('R3', 'g0/2')
configACL('R3', 'g0/3')

configACL('R4', 'g0/1')

configACL('R5', 'g0/1')