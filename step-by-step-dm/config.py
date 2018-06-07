NETWORK_NAME = 'a-new-name-of-network-3'
DISK_NAME = 'disk-vmgr-3'
VM_NAME = 'vm-3'
CONFIG_NAME = 'config-vmgr-3'
WAITER_NAME = 'waiter-vmgr-3'
ZONE = 'us-east1-b'
REGION = 'us-east1'
def GenerateConfig(context):
    resources = [{
        'name': VM_NAME,
        'type': 'vm.py',
        'properties': {
            'machineType': 'g1-small',
            'zone': ZONE,
            'region': REGION,
            'network': NETWORK_NAME,
            'disk': DISK_NAME,
            'configName': CONFIG_NAME,
            'vmIP': context.properties['vmIP']
        }
    }, {
        'name': NETWORK_NAME,
        'type': 'network-1.py'
    }, {
        'name': NETWORK_NAME + '-firewall',
        'type': 'firewall-1.py',
        'properties': {
            'network': NETWORK_NAME
        }
    }, {
        'name': DISK_NAME,
        'type': 'disk.py',
        'properties': {
            'zone': ZONE
        }
    }, {
        'name': CONFIG_NAME,
        'type': 'resource-config.py'
    }, {
        'name': WAITER_NAME,
        'type': 'waiter.py',
        'properties': {
            'vmName': VM_NAME,
            'configName': CONFIG_NAME
        }
    }]
    return { 'resources': resources }