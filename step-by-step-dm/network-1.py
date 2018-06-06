def GenerateConfig(context):
    resources = [
        {
            'name': 'a-new-network',
            'type': 'compute.v1.network',
            'properties': {
                'IPv4Range': '10.0.0.1/16'
            }
        }
    ]
    return { 'resources': resources }