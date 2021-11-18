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

templates = zapi.template.get({
    "output": ['host']
})
for template in templates:
    print(template)
    templateid = template['templateid']
    template_name = template['host']
    templateids = []
    templateids.append(templateid)
    export_xml = zapi.configuration.export({
        "format": "xml",
        "options": {
            "templates": templateids
        }
    })   
    conf = open(f'{template_name}.xml',"w")
    conf.write(export_xml)
    print(f'{template_name} - Configuração exportada com sucesso')

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