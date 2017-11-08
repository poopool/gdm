"""Network template Skeleton."""


def generate_config(context):
    """Generate Network configuration."""

    name = context.env['name']
    auto_create_subnetworks = context.properties['autoCreateSubnetworks']

    resources = [
        {
            'name': name,
            'type': 'compute.v1.network',
            'properties': {
                'autoCreateSubnetworks': auto_create_subnetworks
            }
        }
    ]

    return {'resources': resources}

if __name__ == "__main__":
    from lib.testing import GenerateConfigTester
    GenerateConfigTester.print_config(generate_config)
