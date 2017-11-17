"""Creates a CloudSQL instance using beta endpoint."""


def generate_config(context):
    """ Generates a CloudSQL instance and database """

    resources = [{
        'name': context.properties['name'],
        'type': 'sqladmin.v1beta4.instance',
        'properties': {
            'name': context.properties['name'],
            'region': context.properties['region'],
            'databaseVersion': context.properties['db_version'],
            'backendType': context.properties['backend_type'],
            'instanceType': context.properties['instance_type'],
            'failoverReplica': context.properties['failover_replica'],
            'settings': {
                'tier': context.properties['db_machine_type'],
                'backupConfiguration': context.properties['backup_configuration'],
                'locationPreference': context.properties['location_preference'],
                'ipConfiguration': context.properties['ip-configuration'],
                'dataDiskType': context.properties['data_disk_type'],
                'dataDiskSizeGb': context.properties['data_disk_size']
                }
            }
        }]

    return {'resources': resources}
