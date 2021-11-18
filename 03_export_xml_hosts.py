from zabbix_api import ZabbixAPI
from zabbix_api import ZabbixAPIException
from zabbix_api import Already_Exists

URL = 'http://10.0.0.56/zabbix'
USERNAME = 'Admin'
PASSWORD = 'zabbix'

try:
    zapi = ZabbixAPI(URL, timeout=180, validate_certs=False)
    zapi.login(USERNAME, PASSWORD)
    print(f'Conectado na API do Zabbix: {zapi.api_version()}')
except Exception as err:
    print(f'Falha para se conectar na API do Zabbix ({err}')
    exit(1)

def get_hosts_from_groupids(groupid):
    hosts = zapi.host.get({
        "output": ["host","name","status"],
        "groupids": groupid
    })
    return hosts

for host in get_hosts_from_groupids(115):
    hostid = host['hostid']
    hostname = host['name']
    print(hostid, hostname) 
    hosts = []
    hosts.append(hostid)
    export_xml = zapi.configuration.export({
        "format": "xml",
        "options": {
            "hosts": hosts
        }
    })   
    conf = open(f'{hostname}.xml',"w")
    conf.write(export_xml)
    print(f'{hostname} - Configuração exportada com sucesso')

"""
    "params": {
        "options": {
            "hosts": [
                "10161"
            ]
        },
        "format": "xml"
    },
"""