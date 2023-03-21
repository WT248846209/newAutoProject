#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    这是接口关键字驱动类，用于提供自动化接口测试的关键字方法。
    主要实现常用的关键字内容，并定义好所有的参数内容即可
    接口中常用关键字无非就是：
        1.各种模拟请求方法：post/get/put/delete/header/.....
        2.集成Allure时，可添加@allure.step,这样在自动化执行的时候
        allure报告可以直接捕捉相关的执行信息，让测试报告信息更详细
        3.根据不用需求进行断言封装
"""
import json
import allure
import jsonpath
import pymysql
import requests
import hashlib
import time
from Crypto.Cipher import AES
import base64
import rsa

class ApiKey:
    # get请求的封装：因为params可能存在无值的情况，存放默认None
    @allure.step("发送get请求")
    def get(self,url,params=None,**kwargs):
        return requests.get(url=url,params=params,**kwargs)

    @allure.step("发送post请求")
    #post请求的封装：data也可能存在无值得情况，存放默认None
    def post(self,url,data=None,**kwargs):
        return requests.post(url=url,data=data,**kwargs)

    # @allure.step("获取返回结果字典值")
    # 基于jsonpath获取数据的关键字：用于提取所需要的内容
    def get_text(self,data,key):
        # jsonpath获取数据的表达式：成功则返回list，失败则返回false
        # loads是将json格式的内容转换为字典的格式
        # jsonpath接收的是dict类型的数据
        dict_data = json.loads(data)
        value = jsonpath.jsonpath(dict_data,key)
        return value[0]

    # 数据库检查
    @allure.step("数据库检查参数")
    def sqlCheck(self,sql):
        conn = pymysql.connect(
            host='shop-xo.hctestedu.com',
            port=3306,
            user='api_test',
            passwd='Aa9999!',
            database='shopxo_hctested',
            charset='utf8')
        # 创建游标
        cmd = conn.cursor()
        # 准备并执行sql语句
        cmd.execute(query=sql)
        # 获取1条查询结果
        results = cmd.fetchmany(1)[0][0]
        conn.close()
        return results

    @allure.step("获取签名")
    def getsign(self):  # 获取老签名
        dealkey = [0x07, 0xB6, 0x79, 0x56, 0x7A, 0x5C, 0x4A, 0xBE, 0x1D, 0xF1, 0xB2, 0x10, 0x3C, 0x5E, 0xDC, 0xA6,
                   0x56, 0xE7, 0x88, 0x25, 0x87, 0x95, 0xD5, 0x85, 0x76, 0x7D, 0xEA, 0x66, 0xF5, 0x0A, 0xC3, 0xA8,
                   0x55, 0x28, 0x67, 0x14, 0x06, 0xE7, 0xCB, 0x68, 0xAC, 0x2E, 0x00, 0x36, 0x57, 0x2F, 0xD2, 0xE2,
                   0x54, 0xE9, 0xC6, 0xA3, 0x03, 0xC6, 0x07, 0x33, 0xBD, 0xF1, 0x6D, 0x46, 0x62, 0xFD, 0x82, 0xCF,
                   0xA3, 0x50, 0x15, 0xB2, 0x53, 0xA4, 0x9C, 0x93, 0x98, 0x55, 0x8E, 0xF8, 0xC1, 0x0C, 0x15, 0x71,
                   0x42, 0x6A, 0xA4, 0xF1, 0x5D, 0x72, 0xB1, 0xC4, 0xF6, 0xF0, 0x56, 0xAE, 0xCA, 0x77, 0x44, 0x45,
                   0x21, 0x1B, 0x93, 0x40, 0x49, 0x89, 0x52, 0x76, 0x2C, 0x64, 0xB8, 0x3B, 0xF9, 0x8D, 0x51, 0xA5,
                   0x80, 0x2C, 0x92, 0x39, 0xF7, 0xAD, 0xAF, 0x59, 0x1F, 0x06, 0xDE, 0x5A, 0x1D, 0x91, 0x1C, 0xDB,
                   0x6F, 0xAD, 0xC1, 0xE8, 0xE5, 0xD4, 0xB4, 0x7C, 0x3E, 0x61, 0x73, 0x2D, 0xCE, 0xCD, 0x01, 0xDF,
                   0x5E, 0xCE, 0x60, 0xB7, 0x83, 0xD1, 0x39, 0xA9, 0xF3, 0x35, 0x05, 0xBA, 0x88, 0x78, 0x97, 0xFC,
                   0x3D, 0x2F, 0xF9, 0x36, 0x2A, 0x38, 0xB0, 0x25, 0x16, 0xA7, 0x08, 0x8C, 0xF6, 0x21, 0xC8, 0x22,
                   0xBC, 0x90, 0x48, 0x35, 0x9A, 0x0D, 0x1A, 0xD9, 0xFA, 0xCC, 0x70, 0xAA, 0x42, 0x3F, 0xB6, 0xE1,
                   0xBB, 0x41, 0x17, 0x74, 0xC2, 0x48, 0x7E, 0x80, 0xD6, 0x09, 0xC5, 0x24, 0x60, 0x30, 0x0E, 0xE3,
                   0xFA, 0x92, 0x66, 0x43, 0xE1, 0x8A, 0x4D, 0xD7, 0x1B, 0x6B, 0x23, 0x65, 0xA0, 0x12, 0x9D, 0x9B,
                   0xE0, 0x93, 0xE5, 0xD2, 0xE3, 0xF4, 0xDC, 0x41, 0xA4, 0x3A, 0x10, 0x2B, 0x96, 0xED, 0x1B, 0x1E,
                   0xA9, 0xB4, 0x34, 0x11, 0x94, 0xA6, 0x75, 0x34, 0xD8, 0x89, 0xFC, 0x4F, 0x3B, 0x22, 0xB1, 0xA7]
        # 生成13位整数时间戳
        timestamp = int(time.time() * 1000)
        str1 = str(timestamp) + str('_') + str(dealkey[timestamp % len(dealkey)])
        sign = hashlib.md5(str1.encode('utf-8')).hexdigest()
        return sign, timestamp

    @allure.step("Md5加密")
    def enMd5(self,text):
        return hashlib.md5(text.encode('utf-8')).hexdigest()

    # AES加密填充使用
    def pad(self, text):
        """
        #填充函数，使被加密数据的字节码长度是block_size的整数倍
        """
        length = AES.block_size  # 初始化数据块大小
        count = len(text.encode('utf-8'))
        add = length - (count % length)
        entext = text + (chr(add) * add)
        return entext

    @allure.step("AES加密")
    def enAES(self,key, text):
        global aes
        key = key.encode("utf-8")  # 初始化密钥
        aes = AES.new(key, AES.MODE_ECB)  # 初始化AES,ECB模式的实例,可以选择其他模式
        res = aes.encrypt(self.pad(text).encode("utf8"))
        # Base64是网络上最常见的用于传输8Bit字节码的编码方式之一
        msg = str(base64.b64encode(res), encoding="utf8")
        return msg

    @allure.step("AES解密")
    def deAES(self, text):
        # 截断函数，去除填充的字符
        unpad = lambda date: date[0:-ord(date[-1])]
        res = base64.decodebytes(text.encode("utf8"))
        msg = aes.decrypt(res).decode("utf8")
        return unpad(msg)

    # 秘钥的位数, 可以自定义指定, 例如: 128、256、512、1024、2048等
    @allure.step("生成RSA公钥和私钥")
    def keyRSA(self, num):
        (pubkey, privkey) = rsa.newkeys(num)
        # 生成公钥
        pub = pubkey.save_pkcs1()
        with open('public.pem', 'wb') as f:
            f.write(pub)

        # 生成私钥
        pri = privkey.save_pkcs1()
        with open('private.pem', 'wb') as f:
            f.write(pri)

    @allure.step("RSA加密")
    def enRSA(self, text):
        # 以 utf-8 的编码格式打开指定文件
        f = open("public.pem", encoding="utf-8")
        # 输出读取到的数据
        pub_str = f.read()
        # 关闭文件
        f.close()
        pub_key = rsa.PublicKey.load_pkcs1(pub_str)
        # rsa加密 最后把加密字符串转为base64
        text = text.encode("utf-8")
        cryto_info = rsa.encrypt(text, pub_key)
        cipher_base64 = base64.b64encode(cryto_info)
        cipher_base64 = cipher_base64.decode()
        return cipher_base64

    @allure.step("RSA解密")
    def deRSA(self, text):
        # 以 utf-8 的编码格式打开指定文件
        f = open("private.pem", encoding="utf-8")
        # 输出读取到的数据
        priv_str = f.read()
        # 关闭文件
        f.close()
        priv_key = rsa.PrivateKey.load_pkcs1(priv_str)
        # rsa解密 返回解密结果
        cryto_info = base64.b64decode(text)
        talk_real = rsa.decrypt(cryto_info, priv_key)
        res = talk_real.decode("utf-8")
        return res

if __name__ == '__main__':
    ak = ApiKey()
    # print(ak.getsign())
    # print(ak.enMd5("展昭"))
    # print(ak.enAES("1234567812345678","展昭"))
    # print(ak.deAES("BaycijcwjugCYXnlSXT4NQ=="))
    # ak.keyRSA(512)
    # print(ak.enRSA("展昭"))
    print(ak.deRSA("fWlu5HU+flfIaK18IQKpwE7wgQOuPtKKaSB1qWcU8MNqg90T3hWpAmi/o4B+1dYAsz0qJML9fgKOZ+DOkGkSVA=="))