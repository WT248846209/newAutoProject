#!/usr/bin/env python
# -*- coding: utf-8 -*-
from IntfPytestAuto.data_driver import yaml_driver

content = yaml_driver.load_yaml('../data/userData.yaml')
print(content)