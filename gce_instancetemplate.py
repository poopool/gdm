"""Basic InstanceTemplate template Skeleton."""

GCE_BASE_URL = 'https://www.googleapis.com/compute/v1/'
SCOPE_BASE_URL = 'https://www.googleapis.com/auth/'

def generate_config(context):
    """Generate InstanceTemplate configuration."""
    name = context.env['name']
    project = context.env['project']
    machine_type = context.properties['machineType']

    # Disk array variables
    disks_dev_name = context.properties['disks'][0]['deviceName']
    disks_boot = context.properties['disks'][0]['boot']
    disks_auto_delete = context.properties['disks'][0]['autoDelete']
    image_url = context.properties['image_url']

    # Network Interface configuration variables
    default_network = ''.join([GCE_BASE_URL, 'projects/', project, '/global/networks/default'])
    net_access_cfg_name = context.properties['networkInterfaces'][0]['accessConfigs'][0]['name']
    net_access_cfg_type = context.properties['networkInterfaces'][0]['accessConfigs'][0]['type']

    instance_template = {
        'name': name,
        'type': 'compute.v1.instanceTemplate',
        'properties': {
            'project': project,
            'properties': {
                'machineType': machine_type,
                'networkInterfaces': [{
                    'network': default_network,
                    'accessConfigs': [{
                        'name': net_access_cfg_name,
                        'type': net_access_cfg_type
                    }]
                }],
                'disks': [{
                    'deviceName': disks_dev_name,
                    'boot': disks_boot,
                    'autoDelete': disks_auto_delete,
                    'initializeParams': {'sourceImage': image_url}
                }],
                'serviceAccounts': [{
                    'scopes': [
                        SCOPE_BASE_URL + s
                        for s in context.properties['serviceAccounts'][0]['scopes']
                    ],
                }]
            }
        }
    }

    # Add tags if they exist
    try:
        instance_template['properties']['properties']['tags'] = \
            context.properties['tags']
    except KeyError:
        pass

    return {'resources': [instance_template]}

if __name__ == "__main__":
    from lib.testing import GenerateConfigTester
    GenerateConfigTester.print_config(generate_config)
