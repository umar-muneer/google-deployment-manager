def GenerateConfig(context):
    resources = [{
        'name': context.env['name'],
        'type': 'runtimeconfig.v1beta1.waiter',
        'metadata': {
            'dependsOn': [context.properties['vmName']]
        },
        'properties': {
            'parent': '$(ref.'+context.properties['configName']+'.name)',
            'waiter': context.env['name'],
            'timeout': '300s',
            'success': {
                'cardinality': {
                    'path': '/success',
                    'number': 1
                }
            }
        }
    }]
    outputs = [{
        'name': 'configName',
        'value': context.properties['configName']
    }]
    return { 'resources': resources, 'outputs': outputs }
