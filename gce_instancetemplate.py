"""Creates the virtual machine."""

GCE_URL_BASE = 'https://www.googleapis.com/compute/v1/'


def generate_config(context):
    """ Iterates through the resource provided by context """

    resources = []
    project = context.env['project']
    name = context.env['name']
    machine_type = context.properties['machineType']
    zone = context.properties['zone']
    count = context.properties['count']
    image_project = context.properties['image_project']
    image_name = context.properties['image_name']

    for count in xrange(count):
        instance_resources = {
            'name': (name + '-' + str(count + 1)),
            'type': 'compute.v1.instance',
            'properties': {
                'zone': zone,
                'machineType': ''.join([GCE_URL_BASE, 'projects/',
                                        project,
                                        '/zones/', zone,
                                        '/machineTypes/', machine_type]),
                'disks': [{
                    'deviceName': 'boot',
                    'type': 'PERSISTENT',
                    'boot': True,
                    'autoDelete': True,
                    'initializeParams': {
                        'sourceImage': ''.join([GCE_URL_BASE, 'projects/',
                                                image_project,
                                                '/global/images/family/',
                                                image_name])
                        }
                    }],
                'networkInterfaces': [{
                    'network': ''.join([GCE_URL_BASE, 'projects/',
                                        project,
                                        '/global/networks/default']),
                    'accessConfigs': [{
                        'name': 'External NAT',
                        'type': 'ONE_TO_ONE_NAT'}],
                }]
            }
        }

        # Add labels if they exist
        try:
            instance_resources['properties']['labels'] = \
                context.properties['labels']
        except KeyError:
            pass

        # Add metadata items if they exist
        try:
            instance_resources['properties']['metadata'] = {
                'items': context.properties['metadata_items']
            }
        except KeyError:
            pass

        # Add tags if they exist
        try:
            instance_resources['properties']['tags'] = \
                context.properties['tags']
        except KeyError:
            pass

        resources.append(instance_resources)

    return {'resources': resources}


if __name__ == "__main__":
    from lib.testing import GenerateConfigTester

    EXTRA_PROPERTIES = {
        'machineType': 'f1-micro',
        'zone': 'us-central1-a',
        'count': 1,
        'image_project': 'debian-cloud',
        'image_name': 'debian-9'
    }

    GenerateConfigTester.print_config(generate_config, EXTRA_PROPERTIES)
