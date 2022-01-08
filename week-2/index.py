# -*- coding: utf-8 -*-
# Python 支援的 ASCII 碼無中文 如果沒有其他編碼提示，Python將預設為ASCII作為標準編碼。
# 要定義原始碼編碼，必須在原始檔中第一行或第二行放置一個魔術註釋。

#要求一:函式與流程控制
#完成以下函式，在函式中使用迴圈計算最小值到最大值之間，所有整數的總和。

def calculate(min, max):
# 請用你的程式補完這個函式的區塊
    if min > max:  #測試輸入順序是否正
        print(0) 
        return
    
    if not (isinstance(min, int) and isinstance(max, int)): #測試輸入是否數字
        print(0)
        return
    
    if min < 0 or max < 0: #測試是否正數，此函式只支援正數
        print(0)
        return

    sum = 0  #建立一個變數用來儲存總合
    for x in range(min, max+1):
        sum+=x
    else:
        print(sum)


calculate(1, 3) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8) # 你的程式要能夠計算 4+5+6+7+8，最後印出 30


#要求二:Python 字典與列表、JavaScript 物件與陣列 
#完成以下函式，正確計算出員工的平均薪資，請考慮員工數量會變動的情況。

def avg(data):
# 請用你的程式補完這個函式的區塊 

    sum_salary = 0
#用for的方法
    #for worker in data["employees"]: #逐一取出在employees list的資料
    #    sum_salary+=worker["salary"] #取得key的值把它加到變數sum_salary
    
    #avg_salary = sum_salary/len(data["employees"]) #取得平均值，用總薪酬/員工數目
    #print(avg_salary)
    #return avg_salary

# 用while的方法
    n = 0
    while n<=len(data["employees"])-1: #找出employees list的長度
        sum_salary += data["employees"][n]["salary"]  # 逐一把員工的薪酬加進去總和
        n+=1
    avg_salary = float(sum_salary)/len(data["employees"]) # 計算員工的薪酬平均值
    print(avg_salary)
    return avg_salary


# 呼叫 avg 函式
avg({
    "count":3,
    "employees":[
        {
            "name":"John",
            "salary":30000 
        },
        {
            "name":"Bob",
            "salary":60000 
        },
        {
            "name":"Jenny",
            "salary":50000 
        }
    ]
}) 


#要求三:演算法
#找出至少包含兩筆整數的列表 (Python) 或陣列 (JavaScript) 中，兩兩數字相乘後的最大值。

def maxProduct(nums):
    # 請用你的程式補完這個函式的區塊 

    new_nums = list(nums) # 複製使用傳遞進來的列表供後續在迴圈中使用
    max = 0 #建立最大值變數
    temp = 0 #建立一個變時用來儲存兩兩數字相乘後的值

    for x in nums: #逐一取出列表中的數字
        if len(nums)<=1: #如果使用者輸入的參數只有一個,直接回傳0
            print(0)
            return 0


        if len(new_nums)<=1: #如果當新建立的列表長度＝1，強制結束函式
            print(max) 
            return max 
       
        for y in range(len(new_nums)-1): #逐一取出列表中的索引

            if len(nums) == 2: #特殊情況處理，如果使用者傳遞進來的列表長度是等於2，直接回傳最大值0
                max = x*new_nums[y+1]
                print(max)
                return max  


            temp=x*new_nums[y+1] # 計算兩兩數字相乘後的最大值
            if temp>max: # 如果有第二個相乘後的結果比前一個最大值大就取代他
                max=temp
        new_nums.remove(x) # 每當一個數字已經相乘過所有其他的數字之後就將它移除， 從而使到我們新建的列表縮小
        


maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([-1, 2]) # 得到 -2 
maxProduct([-1, 0, 2]) # 得到 0 
maxProduct([-1, -2, 0]) # 得到 2


#要求四 ( 請閱讀英文 ):演算法

#Given an array of integers, show indices of the two numbers such that they add up to a specific target. You can assume that each input would have exactly one solution, and you can not use the same element twice.

def twoSum(nums, target):
# your code here
    new_nums = list(nums)   #淺度復制一個列表
    empty_index=[]                #建立一個空白供後續在迴圈中存放索引
    temp = 0                #存放兩數雙加的總合
    temp_index = 0          #存放索引

    for x in range(len(nums)):   #先取出列表第一個數
        if len(nums)<=1:         #假如使用者輸入只有一個資料的列表就直接回傳0
            return 0
        for y in range(len(new_nums)-1):      #取出列表第一個數後面的每一個數做相加
            temp = nums[x]+new_nums[y+1]      #存放總合
            if temp==target:                  # 如果總合=target
                empty_index.append(x)               #把第一個的index放進空白列表
                temp_index=nums.index(new_nums[y+1],x+1)  #找出第二個數的index，設定一個起始位置必須是第一個數字後面的index 應對情況[2,2,3,4] target = 4
                empty_index.append(temp_index)      #把第二個index放進列表
                return empty_index              #回傳index列表
        new_nums.pop(y)                       #每次迴圈完結都把第一個數字拿走，可以使到new_nums列表的長度愈來愈短
    else:
        return 0                              #假如list中的元素沒法算出target,直接回傳0

result=twoSum([2, 11, 7, 15], 9)

print(result) # show [0, 2] because nums[0]+nums[2] is 9


# 要求五 ( Optional ):演算法
# 給定只會包含 0 或 1 兩種數字的列表 (Python) 或陣列 (JavaScript)，計算連續出現 0 的最大
# 長度。

def maxZeros(nums):
# 請用你的程式補完這個函式的區塊 

    max = 0
    temp =0
    consecutive_list =[] # 建立一個空白列表用來存放0的連續數量
    
    for x in nums:
        if 0 not in nums: # 如果列表中沒有0，就直接回傳結束函式
            print(0)
            return 0
        if x == 0:
            consecutive_list.append(x) # 列表中有0就加進去空白列表中
        else:
            temp=len(consecutive_list) # 如果列表中有一，就先把空白列表的長度記錄下來
            #print(temp)
            if temp>max: # 如果空白列表的長度是大過max
                max=temp  # max就直接等於空白列表的長度
                del consecutive_list[:] #清空列表
            
    else:
        temp=len(consecutive_list) 
        if temp>max:
            max = temp
            print(max)
            return max
        else:
            print(max)
            return(max)





maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4 
maxZeros([1, 1, 1, 1, 1]) # 得到 0 
maxZeros([0, 0, 0, 1, 1]) # 得到 3

