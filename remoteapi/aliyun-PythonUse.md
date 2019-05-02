# 使用python管理阿里云server
### 1.开始

阿里云Python SDK网址: https://help.aliyun.com/document_detail/53090.html

使用阿里云Python SDK访问云服务器、云数据库RDS、云监控等多个阿里云服务。

### 2.环境准备
- 使用阿里云Python SDK，您需要一个RAM账号以及一对AccessKey ID和AccessKey Secret. 使用aliyun账号创建AccessKey.

### 3. 安装阿里云Python SDK
1. 安装SDK核心库
  - Python2安装阿里云SDK核心库:
    ```
    pip install aliyun-python-sdk-core
    ```
  - Python3安装阿里云SDK核心库:
    ```
    pip install aliyun-python-sdk-core-v3
    ```
2. 安装云产品的SDK
   - 安装云服务器ECS的SDK:
    ```
    pip install aliyun-python-sdk-ecs
    ```

### 4.使用Python SDK
**调用Python SDK的3个主要步骤:**
  1. 创建Client实例。在创建Client实例时，您需要获取Region ID、AccessKey ID和AccessKey Secret。
  2. 创建API请求并设置参数。
  3. 发起请求并处理应答或异常。

- 代码参考:aliyunecs.py

地域(Region-id)参考: https://help.aliyun.com/document_detail/40654.html?spm=a2c4e.11153987.0.0.6d85366adl5pC1

### 5.使用Python SDK手册
手册参考网址: https://help.aliyun.com/document_detail/67117.html?spm=a2c4g.11186623.2.15.647051c1xjmT4m

1. 安装
  ```
  pip install aliyun-python-sdk-core-v3 # 安装Python3的阿里云SDK核心库
  pip install aliyun-python-sdk-ecs # 安装管理ECS的库
  ```
2. 设置身份验证凭据
  - 支持身份验证方式
  
  | 验证方式 |	说明 |
  | ---: | ----: |
  | AccessKey	| 使用AccessKey ID和AccessKey Secret访问 |
  | StsToken |	使用STS Token访问 |
  | RamRoleArn |	使用RAM子账号的AssumeRole方式访问 |
  | EcsRamRole |	在ECS实例上通过EcsRamRole实现免密验证 |

建议您使用RAM账号来访问阿里云服务。阿里云账号的AccessKey对拥有的资源有完全的权限。RAM账号由阿里云账号授权创建，仅有对特定资源限定的操作权限.
