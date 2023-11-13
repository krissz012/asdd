from netmiko import ConnectHandler
import getpass
from datetime import datetime

time_file = datetime.now().strftime("%y-%m-%d")


username = ("Enter your username: ")
password = getpass.getpass()


cisco_router = {

'device-type': 'cisco_ios',
'host': 'x.x.x.x',
'username': username,
'password': password,
#'secret': secret,
}
 
print("Running config mentese...")




net_connect = ConnectHandler(**cisco_router)
net_connect.enable()
output = net_connect.send_command('show run')
readoutput1 = (''.join(output))
saveoutput1 = open("cisco- ", + time_file, +'.txt', 'w')
saveoutput1.write(str(readoutput1))
saveoutput1.close()