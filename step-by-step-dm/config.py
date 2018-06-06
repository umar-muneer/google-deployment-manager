NETWORK_NAME = 'a-new-name-of-network'
def GenerateConfig(context):
    resources = [{
        'name': 'vm-1',
        'type': 'vm.py',
        'properties': {
            'machineType': 'g1-small',
            'zone': 'us-east1-b',
            'network': NETWORK_NAME
        }
    }, {
        'name': 'vm-2',
        'type': 'vm.py',
        'properties': {
            'machineType': 'f1-micro',
            'zone': 'us-east1-b',
            'network': NETWORK_NAME
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
    }]
    return { 'resources': resources }