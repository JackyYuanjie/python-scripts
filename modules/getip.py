# -*- coding:utf-8 -*-

import ifcfg
import json
  
for name, interface in ifcfg.interfaces().items():
    # do something with interface
    print(interface['device'])