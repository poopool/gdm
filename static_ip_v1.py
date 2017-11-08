"""Static IP Basic template Skeleton."""


def generate_config(context):
    """Static IP Generate configuration."""

    name = context.env['name']
    region = context.properties['region']

    resources = [
        {
            'name': name,
            'type': 'compute.v1.address',
            'properties': {
                'region': region,
            }
        }
    ]

    return {'resources': resources}

if __name__ == "__main__":
    from lib.testing import GenerateConfigTester
    GenerateConfigTester.print_config(generate_config)
