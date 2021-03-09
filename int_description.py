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


def configInterface(device):
    num = 0
    device_param ={
    'device_type': 'cisco_ios',
    'host':   '',
    'username': 'admin',
    'password': 'cisco',
}
    device_param['host'] = device_ip[device]
    ssh = netmiko.ConnectHandler(**device_param)
    result = ssh.send_command('sh cdp neigh det | i ^Device|^Interface')
    # commands =["cdp run","lldp run"]
    # ssh.send_config_set(commands)
    # result = ssh.send_command("show lldp")
    local_interface = re.findall("Interface: (\w+\/\d)",result)
    out_interface = re.findall("Port ID \(outgoing port\): (\w+\/\d)",result)
    name = re.findall("Device ID: (\w+)",result)
    for i in local_interface:
        commands =["interface "+i,"description connect to "+out_interface[num]+" of "+name[num]]
        ssh.send_config_set(commands)
        num +=1
    print(ssh.send_command("sh interface description"))

for i in device_ip:
    configInterface(i)