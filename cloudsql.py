"""Creates a CloudSQL instance using beta endpoint."""


def generate_config(context):
    """ Generates a CloudSQL instance and database """

    name = context.env['name']

    resources = [{
        'name': name,
        'type': 'sqladmin.v1beta4.instance',
        'properties': {
            'region': context.properties['region'],
            'databaseVersion': context.properties['db_version'],
            'backendType': context.properties['backend_type'],
            'failoverReplica': context.properties['failover_replica'],
            'settings': {
                'tier': context.properties['db_machine_type'],
                'databaseReplicationEnabled': context.properties['database_replication_enabled'],
                'locationPreference': context.properties['location_preference'],
                'ipConfiguration': context.properties['ip-configuration'],
                'dataDiskType': context.properties['data_disk_type'],
                'dataDiskSizeGb': context.properties['data_disk_size']
                }
            }
        }]

    if 'backupConfiguration' in context.properties:
        resources['properties']['backupConfiguration'] = context.properties['backup_configuration']
    return {'resources': resources}
