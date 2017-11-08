"""VPN Gateway Basic template Skeleton."""


def generate_config(context):
    """VPN Gateway Generate configuration."""

    name = context.env['name']
    region = context.properties['region']
    network = context.properties['network']

    resources = [
        {
            'name': name,
            'type': 'compute.v1.targetVpnGateway',
            'properties': {
                'region': region,
                'network': network
            }
        }
    ]

    return {'resources': resources}

if __name__ == "__main__":
    from lib.testing import GenerateConfigTester
    GenerateConfigTester.print_config(generate_config)
