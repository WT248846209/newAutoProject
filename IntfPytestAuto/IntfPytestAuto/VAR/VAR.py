#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    常量统一管理文件，为了方便代码中识别，目录、文件、常量名全部大写
"""
# 项目链接
PROJECT_URL = "http://shop-xo.hctestedu.com/index.php?s="
# 公共参数
PARAMS = {
    "application": "app",
    "application_client_type": "weixin"
}
# 用户名
USERNAME = "zz"
# 密码
PASSWD = "123456"
# 查询购物车报文结果
CARTCHECK = {
  "msg": "success",
  "code": 0,
  "data": {
    "data": [
      {
        "id": "13345",
        "user_id": "18446",
        "goods_id": "10",
        "title": "夏装女装古力娜扎明星同款一字领露肩蓝色蕾丝修身显瘦连衣裙礼服",
        "images": "http://shop-xo.hctestedu.com/static/upload/images/goods/2019/01/14/1547455222990904.jpg",
        "original_price": 568,
        "price": 228,
        "stock": "1",
        "spec": None, # Null要改成 None
        "add_time": "1667483086",
        "upd_time": "1667483086",
        "inventory_unit": "件",
        "is_shelves": "1",
        "is_delete_time": "0",
        "buy_min_number": "1",
        "buy_max_number": "1",
        "model": "",
        "site_type": "4",
        "is_invalid": 0,
        "inventory": "888780",
        "spec_weight": "0",
        "spec_coding": "",
        "spec_barcode": "",
        "extends": None, # Null要改成 None
        "goods_url": "http://shop-xo.hctestedu.com/index.php?s=/index/goods/index/id/10.html",
        "images_old": "/static/upload/images/goods/2019/01/14/1547455222990904.jpg",
        "total_price": 228,
        "is_error": 0,
        "error_msg": ""
      }
    ],
    "common_cart_total": 1
  }
}