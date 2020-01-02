##日志分析:

###1. linux系统日志级别(7个级别):

0  EMERG : 紧急信息.

1  ALERT : 警告信息.

2  CRITICAL: 严重错误信息.

3  ERROR: 错误信息.

4  WARNING : 提醒信息.

5  NOTICE: 注意信息

6  INFO : 一般信息.

7  DEBUG: 调试信息


###2.采用python3的logging模块来查看并分析日志:
 logging模块的日志级别和linux系统日志级别一样.
 
####2.1 logging模块记录日志的方式:
-  (1) logging模块的常用函数:
   
   logging.debug(msg, *args, **kwargs)	创建一条严重级别为DEBUG的日志记录
   
   logging.info(msg, *args, **kwargs)	创建一条严重级别为INFO的日志记录

   logging.warning(msg, *args, **kwargs)	创建一条严重级别为WARNING的日志记录

   logging.error(msg, *args, **kwargs)	创建一条严重级别为ERROR的日志记录
    
   logging.critical(msg, *args, **kwargs)	创建一条严重级别为CRITICAL的日志记录
    
   logging.log(level, *args, **kwargs)	创建一条严重级别为level的日志记录

   logging.basicConfig(**kwargs)	对root logger进行一次性配置
   
   说明:
       logging.basicConfig(**kwargs) 指定记录的日志级别,格式,输出位置,打开模式等信息.
       
- (2) 四大组件:
  日志器logger : 提供应用程序代码直接使用的接口
  
  处理器handler : 用于将日志记录发送到指定的目的位置

  过滤器filter : 提供更细粒度的日志过滤功能，用于决定哪些日志记录将会被输出（其它的日志记录将会被忽略）

  格式器formatters : 用于控制日志信息的最终输出格式
  

- logging模块说明:
   
   logging模块默认提供的日志器的日志级别是WARNING. 大于它的级别才会被显示.
   
   - 输出字段含义:
      
      日志级别:日志器名称:日志内容
      
     输出的是默认的日志格式.
      
   - logging.basicConfig()函数说明:
     - 关键字参数
       
       filename 指定日志要输出的文件名
       
       filemode 日志打开模式.
       
       format 日志格式字符串.
       
       datefmt 指定日期/时间格式.
       
       style 指定format格式风格.
       
       level 日志器的日志级别.
       
       stream 日志输出目标文件要存放的位置.
       
       handlers  创建了多个Handler的可迭代对象.
     
     注意: filename、stream和handlers这三个配置项只能有一个存在.
       
   - logging模块定义的格式字符串:
      %(asctime)s 可读时间.
      %(created)f  时间戳
      %(msecs)d   毫秒.
      %(levelname)s 文字形式的日志级别
      %(levelno)s  数字形式的日志级别.
      %(name)s  日志器名称.
      %(message)s  记录信息.
      %(pathname)s  log日志文件的路径
      %(filename)s  filename名称
      %(funcName)s  函数名.
      %(process)d  进程ID
      %(processName)s  进程名称
      %(thread)d   线程ID
      %(thread)s   线程名称
      
      
      