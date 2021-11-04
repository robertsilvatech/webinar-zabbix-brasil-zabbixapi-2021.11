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