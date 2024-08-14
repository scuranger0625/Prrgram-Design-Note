# 1. 函數定義與返回值
# 函數是一組相關語句的集合，用來執行特定任務。

def greet(name):
    """這是文檔字串，用來說明這個函數的功能"""
    return f"Hello, {name}!"

# 呼叫函數
print(greet("Alice"))  # 輸出: Hello, Alice!

# 注意事項：
# 1. 使用 def 關鍵字來定義函數。
# 2. 函數可以有可選的參數和返回值。
# 3. 使用文檔字串 (docstring) 來說明函數的用途和功能。

# 2. 遞迴函數
# 遞迴是一種在函數中調用自身的編程技術，適合解決分治類問題。

def factorial(n):
    """計算 n 的階乘"""
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# 測試遞迴函數
print("5! =", factorial(5))  # 輸出: 5! = 120

# 注意事項：
# 1. 遞迴函數必須有一個終止條件（基礎情況），以防止無限遞迴。
# 2. 遞迴適合解決需要重複解同類問題的場景，但在處理深度遞迴時需謹慎，避免超出記憶體限制。

# 3. 匿名函數（Lambda 函數）
# 匿名函數是一種沒有名稱的簡短函數，適合用於簡單的計算或作為高階函數的參數。

# 使用 lambda 函數定義一個平方計算函數
square = lambda x: x * 2
print("平方計算:", square(5))  # 輸出: 平方計算: 10

# 注意事項：
# 1. Lambda 函數僅能包含一個表達式，並且沒有名稱。
# 2. Lambda 函數常用於簡短且臨時的計算中，或作為高階函數（如 filter, map）的參數。

# 4. 全域與區域變數
# 函數內部的變數默認為區域變數，除非使用 global 關鍵字聲明為全域變數。

x = 10  # 全域變數

def modify_global():
    global x  # 聲明 x 為全域變數
    x = x + 5  # 修改全域變數
    print("函數內 x 的值:", x)

modify_global()  # 呼叫函數
print("函數外 x 的值:", x)  # 輸出: 函數外 x 的值: 15

# 注意事項：
# 1. 使用 global 關鍵字可以在函數內修改全域變數。
# 2. 函數內未聲明為 global 的變數為區域變數，僅在函數內有效。
# 3. 謹慎使用全域變數，以避免程式結構混亂和難以維護。

# 5. 模組與包的使用
# Python 的模組是包含 Python 定義和語句的文件，而包是有層次結構的模組集合。

import math  # 導入標準模組

def calculate_circle_area(radius):
    """計算圓的面積"""
    return math.pi * radius ** 2

# 呼叫函數
print("半徑為 5 的圓面積:", calculate_circle_area(5))  # 輸出: 半徑為 5 的圓面積: 78.53981633974483

# 注意事項：
# 1. 使用 import 關鍵字可以導入模組或包中的功能。
# 2. 模組化有助於程式碼的重用和組織，提升可維護性。
