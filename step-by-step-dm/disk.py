def GenerateConfig(context):
    resources = [{        
        "name": context.env["name"],
        "type": "compute.v1.disk",
        "properties": {
            "zone": "us-east1-b",
            "type": "projects/"+context.env["project"]+"/zones/us-east1-b/diskTypes/pd-ssd",
            "sizeGb": "10"
        }
    }]
    return { "resources": resources }