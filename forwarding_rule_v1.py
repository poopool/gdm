"""Forwarding Rule Basic template Skeleton."""


def generate_config(context):
    """Forwarding Rule Generate configuration."""

    name = context.env['name']
    region = context.properties['region']
    ip_protocol = context.properties['IPProtocol']
    port_range = context.properties['portRange']
    ip_address = context.properties['IPAddress']
    network = context.properties['network']
    target = context.properties['target']

    resources = [
        {
            'name': name,
            'type': 'compute.v1.forwardingRules',
            'properties': {
                'region': region,
                'IPProtocol': ip_protocol,
                'portRange': port_range,
                'IPAddress': ip_address,
                'network': network,
                'target': target
            }
        }
    ]

    return {'resources': resources}

if __name__ == "__main__":
    from lib.testing import GenerateConfigTester
    GenerateConfigTester.print_config(generate_config)
