NETWORK_NAME = 'a-new-name-of-network'
DISK_NAME = 'disk-vmgr-1'
def GenerateConfig(context):
    resources = [{
        'name': 'vm-1',
        'type': 'vm.py',
        'properties': {
            'machineType': 'g1-small',
            'zone': 'us-east1-b',
            'network': NETWORK_NAME,
            'disk': DISK_NAME
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
        'type': 'disk.py'
    }]
    return { 'resources': resources }