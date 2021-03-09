from netmiko import ConnectHandler

cisco_881 = {
    'device_type': 'cisco_ios',
    'host':   '172.31.183.1',
    'username': 'admin',
    'password': 'cisco',
}
with ConnectHandler(**cisco_881) as ssh:
    result = ssh.send_command('sh ip int br')
    print(result)