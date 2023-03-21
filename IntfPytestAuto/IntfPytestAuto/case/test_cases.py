#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
import pytest

from IntfPytestAuto.VAR.VAR import *

@allure.feature("商品详情")
@allure.title("testDS_004验证输入的商品ID不存在提示用户")
def testDS_004(token_fix):
    # 从fix中获取预置的工具类和token
    # 所有返回都要获取，不然会报错
    ak, token = token_fix
    # 02 加入购物车
    data = {
        "goods_id":"1211"
    }

    # 添加token到公共参数
    PARAMS["token"] = token
    url = PROJECT_URL + "api/goods/detail"
    res = ak.post(url=url, params=PARAMS, json=data)
    # 输出结果
    print(res.json())
    # 结果断言
    msg = ak.get_text(res.text,"$..msg")
    assert msg == "商品不存在或已删除"

@pytest.mark.skip
@allure.feature("用户注册")
@allure.title("testDS_010用户名为不超过7位，注册成功")
def testDS_006(token_fix):
    # 从fix中获取预置的工具类和token
    # 所有返回都要获取，不然会报错
    ak, token = token_fix
    # 02 加入购物车
    data = {
        "accounts": "zz0010",
        "pwd": 123456,
        "type": "username"
    }

    url = PROJECT_URL + "api/user/reg"
    res = ak.post(url=url, params=PARAMS, json=data)
    # 输出结果
    print(res.json())
    # 结果断言
    msg = ak.get_text(res.text,"$..msg")
    assert msg == "注册成功"

@allure.feature("用户注册")
@allure.title("testDS_013验证当type输入不存在的类型提示错误信息")
def testDS_013(token_fix):
    # 从fix中获取预置的工具类和token
    # 所有返回都要获取，不然会报错
    ak, token = token_fix
    # 02 加入购物车
    data = {
        "accounts": "zz0010",
        "pwd": 123456,
        "type": "phone"
    }

    url = PROJECT_URL + "api/user/reg"
    res = ak.post(url=url, params=PARAMS, json=data)
    # 输出结果
    print(res.json())
    # 结果断言
    msg = ak.get_text(res.text,"$..msg")
    assert msg == "注册类型有误"

@allure.feature("登录")
@allure.title("testDS_022使用用户名能正确的登录用户")
def testDS_022(token_fix):
    # 从fix中获取预置的工具类和token
    # 所有返回都要获取，不然会报错
    ak, token = token_fix
    # 02 加入购物车
    data = {
        "accounts": "zz888",
        "pwd": 123456,
        "type": "username"
    }

    url = PROJECT_URL + "api/user/login"
    res = ak.post(url=url, params=PARAMS, json=data)
    # 输出结果
    print(res.json())
    # 结果断言
    msg = ak.get_text(res.text,"$..msg")
    assert msg == "登录成功"

@allure.feature("登录")
@allure.title("testDS_025验证输入错误的用户名提示用户")
def testDS_025(token_fix):
    # 从fix中获取预置的工具类和token
    # 所有返回都要获取，不然会报错
    ak, token = token_fix
    # 02 加入购物车
    data = {
        "accounts": "zz1231231231223",
        "pwd": 123456,
        "type": "username"
    }

    url = PROJECT_URL + "api/user/login"
    res = ak.post(url=url, params=PARAMS, json=data)
    # 输出结果
    print(res.json())
    # 结果断言
    msg = ak.get_text(res.text,"$..msg")
    assert msg == "登录帐号不存在"

@allure.feature("登录")
@allure.title("testDS_026验证用户名为空提示用户")
def testDS_026(token_fix):
    # 从fix中获取预置的工具类和token
    # 所有返回都要获取，不然会报错
    ak, token = token_fix
    # 02 加入购物车
    data = {
        "accounts": "",
        "pwd": 123456,
        "type": "username"
    }

    url = PROJECT_URL + "api/user/login"
    res = ak.post(url=url, params=PARAMS, json=data)
    # 输出结果
    print(res.json())
    # 结果断言
    msg = ak.get_text(res.text,"$..msg")
    assert msg == "登录账号不能为空"

@allure.feature("加入购物车")
@allure.title("testDS_033验证无规格值可以加入到对应商品")
def testDS_033(token_fix):
    # 从fix中获取预置的工具类和token
    # 所有返回都要获取，不然会报错
    ak, token = token_fix
    # 02 加入购物车
    data ={
        "goods_id": "10",
        "spec": "",
        "stock": 1
    }

    # 添加token到公共参数
    PARAMS["token"] = token
    url = PROJECT_URL + "api/cart/save"
    res = ak.post(url=url, params=PARAMS, json=data)
    # 输出结果
    print(res.json())
    # 结果断言
    msg = ak.get_text(res.text,"$..msg")
    assert msg == "加入成功"

@allure.feature("删除购物车")
@allure.title("testDS_055能删除当前用户对应的购物车")
def testDS_055(token_fix):
    # 从fix中获取预置的工具类和token
    # 所有返回都要获取，不然会报错
    ak, token = token_fix
    # 01 加入购物车
    data ={
        "goods_id": "10",
        "spec": "",
        "stock": 1
    }

    # 添加token到公共参数
    PARAMS["token"] = token
    url = PROJECT_URL + "api/cart/save"
    res = ak.post(url=url, params=PARAMS, json=data)
    # 输出结果
    print(res.json())
    # 结果断言
    msg = ak.get_text(res.text,"$..msg")
    assert msg == "加入成功"

    # 02 查询购物车
    # 添加token到公共参数
    PARAMS["token"] = token
    url = PROJECT_URL + "api/cart/index"
    res = ak.post(url=url, params=PARAMS, json=data)
    # 输出结果
    print(res.json())
    # 返回购物车id
    cartid = ak.get_text(res.text,"$..id")

    # 03 删除购物车
    data ={
        "id": cartid
    }

    # 添加token到公共参数
    PARAMS["token"] = token
    url = PROJECT_URL + "api/cart/delete"
    res = ak.post(url=url, params=PARAMS, json=data)
    # 输出结果
    print(res.json())
    # 结果断言
    msg = ak.get_text(res.text,"$..msg")
    assert msg == "删除成功"

@allure.feature("提交订单")
@allure.title("testDS_094验证能正确的下单")
def testDS_094(token_fix):
    # 从fix中获取预置的工具类和token
    # 所有返回都要获取，不然会报错
    ak, token = token_fix
    # 01 加入购物车
    data ={
        "goods_id": "10",
        "spec": "",
        "stock": 1
    }

    # 添加token到公共参数
    PARAMS["token"] = token
    url = PROJECT_URL + "api/cart/save"
    res = ak.post(url=url, params=PARAMS, json=data)
    # 输出结果
    print(res.json())
    # 结果断言
    msg = ak.get_text(res.text,"$..msg")
    assert msg == "加入成功"

    # 02 查询购物车
    # 添加token到公共参数
    PARAMS["token"] = token
    url = PROJECT_URL + "api/cart/index"
    res = ak.post(url=url, params=PARAMS, json=data)
    # 输出结果
    print(res.json())
    # 返回购物车id
    cartid = ak.get_text(res.text,"$..id")

    # 03 提交订单
    data ={
        "goods_id": 10,
        "buy_type": "cart",
        "stock": 1,
        "spec": "",
        "ids": cartid,
        "address_id": 921,
        "payment_id": 4,
        "user_note": "",
        "site_model": 0
    }
    # 添加token到公共参数
    PARAMS["token"] = token
    url = PROJECT_URL + "api/buy/add"
    res = ak.post(url=url, params=PARAMS, json=data)
    # 输出结果
    print(res.json())
    # 结果断言
    msg = ak.get_text(res.text,"$..msg")
    assert msg == "提交成功"

@allure.feature("订单列表")
@allure.title("testDS_124能查看当前用户所有的订单信息")
def testDS_124(token_fix):
    # 从fix中获取预置的工具类和token
    # 所有返回都要获取，不然会报错
    ak, token = token_fix
    # 01 加入购物车
    data ={
        "goods_id": "10",
        "spec": "",
        "stock": 1
    }

    # 添加token到公共参数
    PARAMS["token"] = token
    url = PROJECT_URL + "api/cart/save"
    res = ak.post(url=url, params=PARAMS, json=data)
    # 输出结果
    print(res.json())
    # 结果断言
    msg = ak.get_text(res.text,"$..msg")
    assert msg == "加入成功"

    # 02 查询购物车
    # 添加token到公共参数
    PARAMS["token"] = token
    url = PROJECT_URL + "api/cart/index"
    res = ak.post(url=url, params=PARAMS, json=data)
    # 输出结果
    print(res.json())
    # 返回购物车id
    cartid = ak.get_text(res.text,"$..id")

    # 03 提交订单
    data ={
        "goods_id": 10,
        "buy_type": "cart",
        "stock": 1,
        "spec": "",
        "ids": cartid,
        "address_id": 921,
        "payment_id": 4,
        "user_note": "",
        "site_model": 0
    }
    # 添加token到公共参数
    PARAMS["token"] = token
    url = PROJECT_URL + "api/buy/add"
    res = ak.post(url=url, params=PARAMS, json=data)
    # 输出结果
    print(res.json())
    # 结果断言
    msg = ak.get_text(res.text,"$..msg")
    assert msg == "提交成功"

    # 04 显示当用户的所有订单
    # 添加token到公共参数
    PARAMS["token"] = token
    url = PROJECT_URL + "api/order/index"
    res = ak.post(url=url, params=PARAMS)
    # 输出结果
    print(res.json())
    # 结果断言
    msg = ak.get_text(res.text, "$..msg")
    assert msg == "success"

@allure.feature("订单详情")
@allure.title("testDS_135验证可以查看对应订单的详细信息")
def testDS_135(token_fix):
    # 从fix中获取预置的工具类和token
    # 所有返回都要获取，不然会报错
    ak, token = token_fix
    # 01 加入购物车
    data ={
        "goods_id": "10",
        "spec": "",
        "stock": 1
    }

    # 添加token到公共参数
    PARAMS["token"] = token
    url = PROJECT_URL + "api/cart/save"
    res = ak.post(url=url, params=PARAMS, json=data)
    # 输出结果
    print(res.json())
    # 结果断言
    msg = ak.get_text(res.text,"$..msg")
    assert msg == "加入成功"

    # 02 查询购物车
    # 添加token到公共参数
    PARAMS["token"] = token
    url = PROJECT_URL + "api/cart/index"
    res = ak.post(url=url, params=PARAMS, json=data)
    # 输出结果
    print(res.json())
    # 返回购物车id
    cartid = ak.get_text(res.text,"$..id")

    # 03 提交订单
    data ={
        "goods_id": 10,
        "buy_type": "cart",
        "stock": 1,
        "spec": "",
        "ids": cartid,
        "address_id": 921,
        "payment_id": 4,
        "user_note": "",
        "site_model": 0
    }
    # 添加token到公共参数
    PARAMS["token"] = token
    url = PROJECT_URL + "api/buy/add"
    res = ak.post(url=url, params=PARAMS, json=data)
    # 输出结果
    print(res.json())
    # 结果断言
    msg = ak.get_text(res.text,"$..msg")
    assert msg == "提交成功"
    # 返回订单id
    orderId = ak.get_text(res.text,"$..order_ids[0]")

    # 04 验证可以查看对应订单的详细信息
    data = {
        "id": orderId
    }

    # 添加token到公共参数
    PARAMS["token"] = token
    url = PROJECT_URL + "api/order/detail"
    res = ak.post(url=url, params=PARAMS, json=data)
    # 输出结果
    print(res.json())
    # 结果断言
    msg = ak.get_text(res.text, "$..msg")
    assert msg == "success"

@allure.feature("取消订单")
@allure.title("testDS_143验证待支付的状态能正确取消")
def testDS_143(token_fix):
    # 从fix中获取预置的工具类和token
    # 所有返回都要获取，不然会报错
    ak, token = token_fix
    # 02 加入购物车
    data = {
        "goods_id": "10",
        "spec": "",
        "stock": 1
    }

    # 添加token到公共参数
    PARAMS["token"] = token
    url = PROJECT_URL + "api/cart/save"
    res = ak.post(url=url, params=PARAMS, json=data)
    # 输出结果
    print(res.json())
    # 结果断言
    msg = ak.get_text(res.text, "$..msg")
    assert msg == "加入成功"

    # 02 查询购物车
    # 添加token到公共参数
    PARAMS["token"] = token
    url = PROJECT_URL + "api/cart/index"
    res = ak.post(url=url, params=PARAMS, json=data)
    # 输出结果
    print(res.json())
    # 返回购物车id
    cartid = ak.get_text(res.text,"$..id")

    # 03 提交订单
    data ={
        "goods_id": 10,
        "buy_type": "cart",
        "stock": 1,
        "spec": "",
        "ids": cartid,
        "address_id": 921,
        "payment_id": 4,
        "user_note": "",
        "site_model": 0
    }
    # 添加token到公共参数
    PARAMS["token"] = token
    url = PROJECT_URL + "api/buy/add"
    res = ak.post(url=url, params=PARAMS, json=data)
    # 输出结果
    print(res.json())
    # 结果断言
    msg = ak.get_text(res.text,"$..msg")
    assert msg == "提交成功"
    # 返回订单id
    orderId = ak.get_text(res.text,"$..order_ids[0]")
    print("订单ID")
    print(orderId)

    # 04 取消订单
    data = {
        "id": orderId
    }

    # 添加token到公共参数
    PARAMS["token"] = token
    url = PROJECT_URL + "api/order/cancel"
    res = ak.post(url=url, params=PARAMS, json=data)
    # 输出结果
    print(res.json())
    # 结果断言
    msg = ak.get_text(res.text, "$..msg")
    assert msg == "取消成功"

@allure.feature("订单支付")
@allure.title("testDS_999完成订单支付")
def testDS_999(token_fix):
    # 从fix中获取预置的工具类和token
    # 所有返回都要获取，不然会报错
    ak, token = token_fix
    # 01 加入购物车
    data ={
        "goods_id": "10",
        "spec": "",
        "stock": 1
    }

    # 添加token到公共参数
    PARAMS["token"] = token
    url = PROJECT_URL + "api/cart/save"
    res = ak.post(url=url, params=PARAMS, json=data)
    # 输出结果
    print(res.json())
    # 结果断言
    msg = ak.get_text(res.text,"$..msg")
    assert msg == "加入成功"

    # 02 查询购物车
    # 添加token到公共参数
    PARAMS["token"] = token
    url = PROJECT_URL + "api/cart/index"
    res = ak.post(url=url, params=PARAMS, json=data)
    # 输出结果
    print(res.json())
    # 返回购物车id
    cartid = ak.get_text(res.text,"$..id")

    # 03 提交订单
    data ={
        "goods_id": 10,
        "buy_type": "cart",
        "stock": 1,
        "spec": "",
        "ids": cartid,
        "address_id": 921,
        "payment_id": 4,
        "user_note": "",
        "site_model": 0
    }
    # 添加token到公共参数
    PARAMS["token"] = token
    url = PROJECT_URL + "api/buy/add"
    res = ak.post(url=url, params=PARAMS, json=data)
    # 输出结果
    print(res.json())
    # 结果断言
    msg = ak.get_text(res.text,"$..msg")
    assert msg == "提交成功"
    # 返回订单id
    orderId = ak.get_text(res.text,"$..order_ids[0]")

    # 04 订单支付
    data = {
        "ids": orderId,
        "payment_id": 4
    }

    # 添加token到公共参数
    PARAMS["token"] = token
    url = PROJECT_URL + "api/order/pay"
    res = ak.post(url=url, params=PARAMS, json=data)
    # 输出结果
    print(res.json())
    # 结果断言
    msg = ak.get_text(res.text, "$..msg")
    assert msg == "处理成功"
