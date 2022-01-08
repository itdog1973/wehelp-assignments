//要求一:函式與流程控制
//完成以下函式，在函式中使用迴圈計算最小值到最大值之間，所有整數的總和。
function calculate(min, max){
    // 請用你的程式補完這個函式的區塊 
    if (min>max){
  
        console.log(0);
        return;
    };

    if(isNaN(min) || isNaN(max)){
        console.log(0);
        return;
    }

    if (min <0 || max <0){
        console.log(0);
        return;
    }

    let sum = 0;
    for (let i=min; i<=max; i++){
        sum+=i;
    }
    console.log(sum);

}
    calculate(1, 3); // 你的程式要能夠計算 1+2+3，最後印出 6 
    calculate(4, 8); // 你的程式要能夠計算 4+5+6+7+8，最後印出30






//要求二:Python 字典與列表、JavaScript 物件與陣列 
//完成以下函式，正確計算出員工的平均薪資，請考慮員工數量會變動的情況。


function avg(data){
    // 請用你的程式補完這個函式的區塊 
    // 使用for方法
    let sum_salary = 0; //宣告總薪酬
    let avg_salary=0;  // 宣告平均薪酬
    let length = data.employees.length; // 宣告員工人數
    let info = data.employees; // 宣告一個區域變數用來存放員工陣列
    //for(let i = 0; i<=length-1;i++){  
    //    sum_salary+=info[i].salary; // 逐一加入每個員工的薪酬
    //}
    
        // 使用while方法
    let n = 0;
    while (n<=length-1){
        sum_salary+=info[n].salary
        n++;
    }

    avg_salary=sum_salary/length; // 取得平均員工薪酬
    console.log(avg_salary);

}

    // 呼叫 avg 函式
    avg({
        "count":3,
        "employees":[ 
            {
                "name":"John",
                "salary":30000 
            },
            {
                "name":"Bob",
                "salary":60000 },
            {
                "name":"Jenny",
                "salary":50000 
             }
        ]
    }); 






//要求三:演算法
//找出至少包含兩筆整數的列表 (Python) 或陣列 (JavaScript) 中，兩兩數字相乘後的最大值。

function maxProduct(nums){
    // 請用你的程式補完這個函式的區塊 

    const new_nums = nums.slice(0);

    let max =0;
    let temp=0;
    for(let i = 0; i<nums.length; i++){
        if(new_nums.length<=1){
            console.log(max);
            return max;
        }
    
        for(let j=0; j<new_nums.length-1; j++){
            if(nums.length==2){
                max=nums[i]*new_nums[j+1];
                console.log(max);
                return max;
            }
            temp = nums[i]*new_nums[j+1];
            if (temp>max){
                max=temp;
            }
        }
        new_nums.shift();
    };


}

maxProduct([5, 20, 2, 6]) //得到 120 
maxProduct([10, -20, 0, 3]) // 得到 30 
maxProduct([-1, 2]) // 得到 -2 
maxProduct([-1, 0, 2]) // 得到 0 
maxProduct([-1, -2, 0]) // 得到 2







//要求四 ( 請閱讀英文 ):演算法
function twoSum(nums, target){
    // your code here
    let array_length = nums.length; 
    let i = 0;
    let j = 0;
    let temp = 0;
    const empty_index = [];
    while (i<array_length){ 
        while(j<array_length-1){
            temp=nums[i]+nums[j+1]; // 把第一個數字和第二個數字相加
            if (temp == target){   // 如果相加是等於target. 回傳這兩個數字的index
                empty_index.push(i);
                empty_index.push(j+1);
                return(empty_index)
            }
            j++;
        }
        i++;
    }



    }
let result=twoSum([2, 11, 7, 15], 9);
console.log(result); // show [0, 2] because nums[0]+nums[2] is 9




//要求五 ( Optional ):演算法
//給定只會包含 0 或 1 兩種數字的列表 (Python) 或陣列 (JavaScript)，計算連續出現 0 的最大
//長度。

function maxZeros(nums){
// 請用你的程式補完這個函式的區塊 
    let temp = 0;
    let max = 0;
    let remain = true;
    let consecutive_array = [];
    
    for(let i =0; i<nums.length; i++){ 

        if (!(nums.includes(0))){ // 如果陣列中 沒有0就直接結束函式 回傳0
            console.log(0);
            return 0;
        }

        if(nums[i]==0){
            consecutive_array.push(nums[i]); // 如果有0就將它加進去空白的陣列
        }else{

            temp=consecutive_array.length; // 如果有1就直接記錄空白列表的長度
            if (temp>max){       // 看看空白列表的長度是否大過max, 是的話就max 就等於空白列表的長度
                max=temp;
               
            };
            consecutive_array=[]; // 清空陣列

        };
        if (i+1 == nums.length){    //做一個類似Python else的效果
            temp=consecutive_array.length;
            if (temp>max){
                max=temp;
            }
            console.log(max);
            return max;
        }
        
    }
    






}
maxZeros([0, 1, 0, 0]); // 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]); // 得到 4 
maxZeros([1, 1, 1, 1, 1]); // 得到 0 
maxZeros([0, 0, 0, 1, 1]) // 得到 3