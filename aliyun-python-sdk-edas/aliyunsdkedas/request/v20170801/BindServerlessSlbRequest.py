# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RoaRequest
class BindServerlessSlbRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Edas', '2017-08-01', 'BindServerlessSlb')
		self.set_uri_pattern('/pop/v5/k8s/acs/serverless_slb_binding')
		self.set_method('POST')

	def get_Intranet(self):
		return self.get_query_params().get('Intranet')

	def set_Intranet(self,Intranet):
		self.add_query_param('Intranet',Intranet)

	def get_AppId(self):
		return self.get_query_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_query_param('AppId',AppId)

	def get_Internet(self):
		return self.get_query_params().get('Internet')

	def set_Internet(self,Internet):
		self.add_query_param('Internet',Internet)