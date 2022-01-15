



const title_array = []; //建立陣列放景點名稱
const link_array = []; // 建立變數放圖片網址
let last_id = undefined; //建立一個變數用
let stop_id = undefined; //建立一個變數用停止使用載入更多



let src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
fetch(src).then(function(response){ //使用ajax連線
    return response.json();         

}).then(function(result){
   
    let attraction = result["result"]["results"] //解析得到的json資料
    for(let i= 0; i<attraction.length; i++){   
        let view = attraction[i]["stitle"];
        let link = attraction[i]["file"];
        link2 = link.toLowerCase();
        index = link2.indexOf("jpg")+3
        first_jpg=link2.slice(0,index);
        title_array.push(view);
        link_array.push(first_jpg);
    }
    let container = document.createElement('div'); //在html建立容器
    container.className="container";
    container.id="container";
    document.body.appendChild(container);
    const container_id = document.getElementById("container");
    let wrap = document.createElement('div');
    wrap.className="wrap";
    wrap.id="wrap"
    container_id.appendChild(wrap);
    const wrap_id = document.getElementById("wrap")
    





for (let i=0; i<8; i++){  //在html建立容器 放進圖片和景點名稱 8個為一組
  
    let item = document.createElement('div');
    item.className="item";
    item.id="item"+i;
    wrap_id.appendChild(item);
    let item_class = document.getElementById("item"+i);
    
    let item_pic = document.createElement('div');
    item_pic.className="pic";
    item_class.appendChild(item_pic); 

    let item_txt = document.createElement('div');
    item_txt.className="txt";
    item_class.appendChild(item_txt); 
    
    let img = document.createElement('img');
    img.src=link_array[i];
    item_pic.appendChild(img);

    let text_node = document.createTextNode(title_array[i]);
    item_txt.appendC
    

    last_id=i; //這個是用來計算前8張圖片已經用過了



};



let button_div =document.createElement('div'); //在html建立按鈕
button_div.className="button_div";
document.body.appendChild(button_div);
let button = document.createElement('button');
let txt = document.createTextNode("Load More");
button.className="button";
button.id="button";
button.appendChild(txt);
button_div.appendChild(button);




let btn = document.getElementById("button"); //得到按鈕物件
let handler = function(){ //建立一個函式，每當要按按鈕的時候就跑以下程式 

   if (stop_id!=undefined){ //檢查是不是最後一個景點
       alert("No more landscape XDD!");
        return;
   };

    for (let i=last_id+1; i<=last_id+8; i++){  //根據一開始載入得到的last_id用來做後續判斷


        if(i==title_array.length){ //檢查是不是最後一個景點，是的話把按鈕改名字
            button.textContent="No More";
            stop_id =i
            return;
        };

        let item = document.createElement('div');
        item.className="item";
        item.id="item"+i;
        wrap_id.appendChild(item);
        let item_class = document.getElementById("item"+i);
        
        let item_pic = document.createElement('div');
        item_pic.className="pic";
        item_class.appendChild(item_pic); 
    
        let item_txt = document.createElement('div');
        item_txt.className="txt";
        item_class.appendChild(item_txt); 
        
        let img = document.createElement('img');
        img.src=link_array[i];
        item_pic.appendChild(img);
    
        let text_node = document.createTextNode(title_array[i]);
        item_txt.appendChild(text_node); 
    
     
        

};

last_id+=8; //load完8張圖片，加8



    

};


btn.addEventListener("click",handler);







});






