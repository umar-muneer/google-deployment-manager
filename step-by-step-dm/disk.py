COMPUTE_URL_BASE = 'https://www.googleapis.com/compute/v1/'
def GenerateConfig(context):
    resources = [{        
        "name": context.env["name"],
        "type": "compute.v1.disk",
        "properties": {
            "zone": "us-east1-b",
            "type": "projects/"+context.env["project"]+"/zones/us-east1-b/diskTypes/pd-ssd",
            "sizeGb": "10",
            'sourceImage': ''.join([COMPUTE_URL_BASE, 'projects/',
                                        'debian-cloud/global',
                                        '/images/family/debian-8'])
        }
    }]
    return { "resources": resources }