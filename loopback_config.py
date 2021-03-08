import netmiko

device_ip = '172.31.183.'
loopback = '172.20.183.'
username = 'admin'
password = 'cisco'
device_params ={
    'device_type': 'cisco_ios',
    'host':   '',
    'username': 'admin',
    'password': 'cisco',
}

for i in range(1,10):
    device_params['host'] = device_ip +str(i)
    ssh = netmiko.ConnectHandler(**device_params)
    commands =['interface lo0', 'ip address '+loopback+str(i)+' 255.255.255.255']
    ssh.send_config_set(commands)
    result = ssh.send_command('show ip int br')
    print(result)
