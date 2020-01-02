# -*- coding:utf-8 -*-
import shortuuid

# 生成短UUID
print(shortuuid.uuid())

# 将URL生成UUID
print(shortuuid.uuid(name="baidu.com"))
print(shortuuid.uuid(name="http://www.baidu.com"))

print(shortuuid.uuid(name="测试用法"))

# 生成带密码的安全随机字符串( 内部使用 os.urandom(), )
# 默认生成22位数uuid。
print(shortuuid.ShortUUID().random(length=16))

# 查看用于生成新uuid的字母表
print(shortuuid.get_alphabet())

# 使用自己的字母表生成uuid
shortuuid.set_alphabet("012~`!@#$%^&*()_+{}|:<>?")
print(shortuuid.uuid())

# shortuuid 将自动排序和删除字母表中的重复项以确保一致性
print(shortuuid.get_alphabet())

# 序列化现有的uuid,请使用encode()和decode()
import uuid
u = uuid.uuid4()
print(u)
s = shortuuid.encode(u)
print(s)
print(shortuuid.decode(s) == u)

short = s[:7]
print(short)
h = shortuuid.decode(short)
print(shortuuid.decode(shortuuid.encode(h)) == h)


# 基于类的用法
# 如果需要每个线程有多个字母，则可以使用ShortUUID类
su = shortuuid.ShortUUID(alphabet="01234567890-=")
print(su.uuid())
print(su.get_alphabet())
print(su.set_alphabet("-=;']qwertyuiop"))
print(su.get_alphabet())