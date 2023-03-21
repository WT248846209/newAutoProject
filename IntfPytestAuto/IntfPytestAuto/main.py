#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import pytest

if __name__ == '__main__':
    # pytest.main(['-v','--alluredir', './result','--clean-alluredir','./case/test_cases.py::testDS_999'])
    pytest.main(['-v','--alluredir', './result','--clean-alluredir'])
    os.system('allure generate ./result/ -o ./report_allure/ --clean')