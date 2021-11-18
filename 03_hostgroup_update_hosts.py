from zabbix_api import ZabbixAPI
from zabbix_api import ZabbixAPIException
from zabbix_api import Already_Exists

"""
Inserir um hostgroup em hosts já cadastrados
"""


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

novo_hostgroupid = 115

def get_hosts_from_groupids(groupid):
    hosts = zapi.host.get({
        "output": ["host","name","status"],
        "groupids": groupid
    })
    return hosts

def massadd_hostgroup(hostsids):
    hostgroup_add = zapi.hostgroup.massadd({
        "groups": [
            {
                "groupid": novo_hostgroupid
            }
        ],
        "hosts": hostsids
    })
    print(hostgroup_add)

hostsids = []
for host in get_hosts_from_groupids(113):
    host_name = host['name']
    host_id = host['hostid']
    print(host_name, host_id)
    temp_dict = {}
    temp_dict['hostid'] = host_id
    hostsids.append(temp_dict)

massadd_hostgroup(hostsids=hostsids)
print(massadd_hostgroup)
    
