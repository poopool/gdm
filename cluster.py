# Copyright 2016 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
'''''''Create configuration to deploy GKE cluster.'''

def GenerateConfig(context):
  '''''''Generate YAML resource configuration.'''

  cluster_name = context.env['name']

  resources = [
      {
          'name': cluster_name,
          'type': 'container.v1.cluster',
          'properties': {
              'zone': context.properties['zone'],
              'cluster': {
                  'name': cluster_name,
                  'nodePools': [{
                        'name': 'default-pool',
                        ##Per zone
                        'initialNodeCount': 1,
                        'config': {
                            'machineType': 'n1-standard-1',
                            'imageType': 'COS',
                            'diskSizeGb': 10,
                            'preemptible': False,
                            'oauthScopes': [
                                'https://www.googleapis.com/auth/' + s
                                for s in context.properties['oauthScopes']
                            ]
                        },
                        'autoscaling': {
                            'enabled': True,
                            ##This is Min and Max nodes per zone
                            'minNodeCount': 1,
                            'maxNodeCount': 2
                        },
                        'management': {
                            'autoUpgrade': False,
                            'autoRepair': False,
                            'upgradeOptions': {}
                        }
                    }],
                  'locations': [
                      'us-central1-a',
                      'us-central1-b',
                      'us-central1-c'
                  ]
              }
          }
      }
  ]

  return {'resources': resources}
