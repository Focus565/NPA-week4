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
username = 'admin'
password = 'cisco'

def configInterface(device,interface,ip_address):
    device_param ={
    'device_type': 'cisco_ios',
    'host':   '',
    'username': 'admin',
    'password': 'cisco',
}
    device_param['host'] = device_ip[device]
    ssh = netmiko.ConnectHandler(**device_param)
    commands =['interface '+interface, 'ip address '+ip_address+' 255.255.255.240', 'no shut']
    ssh.send_config_set(commands)
    result = ssh.send_command('show ip int br')
    print(result)


configInterface('R1','g0/1','172.31.183.17')
configInterface('R1','g0/2','172.31.183.33')

configInterface('R2','g0/1','172.31.183.18')
configInterface('R2','g0/2','172.31.183.49')

configInterface('R3', 'g0/1', '172.31.183.34')
configInterface('R3', 'g0/2', '172.31.183.50')
configInterface('R3', 'g0/3', '172.31.183.65')

configInterface('R4', 'g0/1', '172.31.183.66')

configInterface('R5', 'g0/1', '172.31.183.67')