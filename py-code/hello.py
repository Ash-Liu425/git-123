#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Python演示代码
version 2.0
"""

def hello_world():
    """打印欢迎信息"""
    print("你好，世界！")

def calculate_sum(a, b):
    """计算两个数字的和"""
    return a + b

def factorial(n):
    """计算阶乘"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def greet(name):
    """个性化问候"""
    return f"你好，{name}！很高兴认识你。"

# 主程序入口
if __name__ == "__main__":
    # 演示1: 欢迎信息
    hello_world()
    
    # 演示2: 计算和
    result = calculate_sum(10, 20)
    print(f"10 + 20 = {result}")
    
    # 演示3: 阶乘
    num = 5
    fac = factorial(num)
    print(f"{num}的阶乘 = {fac}")
    
    # 演示4: 问候
    message = greet("张三")
    print(message)
    
    # 演示5: 列表操作
    fruits = ["苹果", "香蕉", "橙子", "葡萄"]
    print(f"水果列表: {fruits}")
    print(f"列表长度: {len(fruits)}")
    
    # 演示6: 字典操作
    person = {"姓名": "李四", "年龄": 28, "城市": "北京"}
    print(f"人物信息: {person}")
    print(f"名字: {person['姓名']}")
