## shortuuid笔记

`shortuuid` 是一个简单的python 库,它生成一个简洁明确和URL安全 uuid的生成器.

`shortuuid` 使用python的内置 `uuid` 模块生成 uuid.

### 安装

要安装shortuuid,安装方法有:

- 使用pip安装: `pip install shortuuid`
- 使用setuptools,做:`easy_install shortuuid`
- 安装源代码: https://github.com/stochastic-technologies/shortuuid,进行`python setup.py install`

### 用法

- 导入模块:`import shortuuid`

- 生成短UUID:`shortuuid.uuid()`

- 将URL生成UUID:

  ```python
  shortuuid.uuid(name="baidu.com")
  shortuuid.uuid(name="http://www.baidu.com")
  ```

- 生成带密码的安全随机字符串`( 内部使用 os.urandom(), )`

  ```python
  shortuuid.ShortUUID().random(length=16)
  ```

- 查看用于生成新uuid的字母表

  ```python
  shortuuid.get_alphabet()
  ```

- 使用自己的字母表生成 uuid

  ```python
  shortuuid.set_alphabet("012~`!@#$%^&*()_+{}|:<>?")
  print(shortuuid.uuid())
  ```

- `shortuuid` 将自动排序和删除字母表中的重复项以确保一致性

  ```python
  print(shortuuid.get_alphabet())
  ```

- 基于类的用法

  - 如果需要每个线程有多个字母，则可以使用ShortUUID类

  ```python
  su = shortuuid.ShortUUID(alphabet="01234567890-=")
  print(su.uuid())
  print(su.get_alphabet())
  print(su.set_alphabet("-=;']qwertyuiop"))
  print(su.get_alphabet())
  ```


参考博客: <https://xin053.github.io/2016/07/07/shortuuid%E5%BA%93%E4%BD%BF%E7%94%A8%E8%AF%A6%E8%A7%A3/>