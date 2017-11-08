"""VPN Tunnel Basic template Skeleton."""


def generate_config(context):
    """VPN Tunnel Generate configuration."""

    name = context.env['name']
    region = context.properties['region']
    forwarding_rule = context.properties['forwardingRule']
    ike_version = context.properties['ikeVersion']
    peer_ip = context.properties['peerIp']
    shared_secret = context.properties['sharedSecret']
    target_vpn_gateway = context.properties['targetVpnGateway']

    resources = [
        {
            'name': name,
            'type': 'compute.v1.vpnTunnel',
            'properties': {
                'region': region,
                'forwardingRule': forwarding_rule,
                'ikeVersion': ike_version,
                'peerIp': peer_ip,
                'sharedSecret': shared_secret,
                'targetVpnGateway': target_vpn_gateway,
                'localTrafficSelector': [
                    '0.0.0.0/0',
                ],
                'remoteTrafficSelector': [
                    '0.0.0.0/0',
                ]
            }
        }
    ]

    return {'resources': resources}

if __name__ == "__main__":
    from lib.testing import GenerateConfigTester
    GenerateConfigTester.print_config(generate_config)
