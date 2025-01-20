import_file='allow_list.txt'

remove_list=['192.168.97.225','192.168.158.180','192.168.201.40','192.168.58.57']

with open(import_file,'r') as file:
    ip_addresses=file.red()

ip_addresses=ip_addresses.split()

for ip in ip_addresses:
    if ip in remove_list:
        ip_addresses.remove(ip)

ip_addresses=' '.join(ip_addresses)

with open(import_file,'w') as file:
    file.write(ip_addresses)
