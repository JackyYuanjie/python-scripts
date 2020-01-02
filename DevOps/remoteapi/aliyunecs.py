#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 调用阿里云Python SDK管理ECS云服务器
## 发起调用
### 以ECS为例,使用Python SDK发起请求
#1. 导入ECS的SDK
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
from aliyunsdkecs.request.v20140526 import StopInstanceRequest

# 2. 新建一个AcsClient
# 注意这里的client的access-key-id和access-key-secret是你自己阿里云账户创建的.
# region-id 是地域ID。 例如:华北2的id: cn-beijing
'''
client = AcsClient(
   "<your-access-key-id>", 
   "<your-access-key-secret>",
   "<your-region-id>"
)
'''

# 3.创建Request对象
request = DescribeInstancesRequest.DescribeInstancesRequest()
request.set_PageSize(10)

# 4. 发起调用并处理返回
try:
    response = client.do_action_with_exception(request)
    print(response)
except ServerException as e:
  print(e)
except ClientException as C:
  print(C)