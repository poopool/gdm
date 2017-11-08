"""Network route Basic template Skeleton."""


def generate_config(context):
    """Network route Generate configuration."""

    name = context.env['name']
    network = context.properties['network']
    next_hop_vpn_tunnel = context.properties['nextHopVpnTunnel']
    priority = context.properties['priority']
    dest_range = context.properties['destRange']

    resources = [
        {
            'name': name,
            'type': 'compute.v1.route',
            'properties': {
                'network': network,
                'nextHopVpnTunnel': next_hop_vpn_tunnel,
                'priority': priority,
                'destRange': dest_range,
            }
        }
    ]

    return {'resources': resources}

if __name__ == "__main__":
    from lib.testing import GenerateConfigTester
    GenerateConfigTester.print_config(generate_config)
