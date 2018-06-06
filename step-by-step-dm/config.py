def GenerateConfig(context):
    resources = [{
        'name': 'vm-1',
        'type': 'vm.py',
        'properties': {
            'machineType': 'g1-small',
            'zone': 'us-east1-b',
            'network': 'a-new-network'
        }
    }, {
        'name': 'vm-2',
        'type': 'vm.py',
        'properties': {
            'machineType': 'f1-micro',
            'zone': 'us-east1-b',
            'network': 'a-new-network'
        }
    }, {
        'name': 'network-1',
        'type': 'network-1.py'
    }, {
        'name': 'firewall-1',
        'type': 'firewall-1.py'
    }]
    return { 'resources': resources }