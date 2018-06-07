# Copyright 2016 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Creates the virtual machine."""

COMPUTE_URL_BASE = 'https://www.googleapis.com/compute/v1/'
BRANCH_NAME = 'master'

def GenerateConfig(context):
  """Creates the second virtual machine."""
  resources = [{
      'name': context.env['name'],
      'type': 'compute.v1.instance',
      'properties': {
          'zone': context.properties['zone'],
          'machineType': ''.join([COMPUTE_URL_BASE, 
                                  'projects/',
                                  context.env['project'],
                                  '/zones/',
                                  context.properties['zone'],
                                  '/machineTypes/',
                                  context.properties['machineType']]),
          'disks': [{
            "kind": "compute#attachedDisk",
            "type": "PERSISTENT",
            "boot": True,
            "mode": "READ_WRITE",
            "autoDelete": False,
            "deviceName": context.properties['disk'],
            "source": '$(ref.'+context.properties['disk']+'.selfLink)'
          }],
          'networkInterfaces': [{
            'kind': 'compute#networkInterface',
            'subnetwork': 'projects/'+context.env['project']+'/regions/'+context.properties['region']+'/subnetworks/default',
            'accessConfigs': [
                {
                    'kind': 'compute#accessConfig',
                    'name': 'External NAT',
                    'type': 'ONE_TO_ONE_NAT',
                    'networkTier': 'PREMIUM',
                    'natIP': context.properties['vmIP']
                }],
            "aliasIpRanges": []
          }],
          'metadata': {
              'items': [{
                  'key': 'startup-script',
                  'value': ''.join(['#!/bin/bash\n',
                                    'gcloud beta runtime-config configs variables set success/my-instance success --config-name ' +context.properties['configName']])
              }]
          },
          "serviceAccounts": [
            {
                "email": "815435412714-compute@developer.gserviceaccount.com",
                "scopes": ["https://www.googleapis.com/auth/cloud-platform"]
            }
        ]
      }
  }]
  return {'resources': resources}