/* 



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
    item_txt.appendChild(text_node); 
    

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


 */

/////////////////////////////////////////////////////////////////////////新code//////////////////////////////////////////////////////////////////
let attractionNameArray =[];
let attractionLinkArray=[];
let wrapTag;
let picPositionCounter = 0;
let numOfPicInTwoRowsCounter =0

//
document.addEventListener("DOMContentLoaded", function(){  //建立完DOM後馬上取得body，建立container容器和wrap容器

let containerTag = document.createElement('div');
containerTag.className="container";
document.body.appendChild(containerTag);

wrapTag = document.createElement('div');
wrapTag.className="wrap";
containerTag.appendChild(wrapTag)

let buttonContainer = document.createElement("div"); //建立按鈕
buttonContainer.className="btnContainer";
document.body.appendChild(buttonContainer);
buttonTag = document.createElement("button");
buttonTag.className="btn";
buttonTag.textContent="Load More";
buttonContainer.appendChild(buttonTag);


buttonTag.addEventListener("click",function(){ //幫按鈕加上click event,
    if (numOfPicInTwoRowsCounter+2 == 58){
        insertPicAndText(2,2);
    }else if(numOfPicInTwoRowsCounter == 58 ){
        alert("沒有景點啦");
        buttonTag.disabled;
    }else{
        insertPicAndText(8,8); //呼叫函式，每次帶入8筆資料到畫面中
    };
 
})
});


function getData(){ //做ajax連線，使用promise的方法做接收伺服器的response
    return new Promise(function(resolve, reject){
        let req = new XMLHttpRequest();
        req.open("get", "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json");
        req.onload=function(){

            resolve(this.responseText);
 
        };

        req.onerror=function(){

            reject("error");
        }
        req.send();
    });
}

   
let promiseResponse = getData(); //呼叫getData函式，取得連線結果
promiseResponse.then(function(response){
    let json_data = JSON.parse(response);
    const attractionName = json_data["result"]["results"]
    for(let i =0; i<attractionName.length; i++){
        attractionNameArray.push(attractionName[i]["stitle"]);
        let picLink = attractionName[i]["file"].split("https://");
        let firstPicLink = "https://"+picLink[1];
        attractionLinkArray.push(firstPicLink);
    };

    insertPicAndText(0,8);//呼叫函式取圖片和網址

}).catch(function(err){
    alert(err);
});



   



function insertPicAndText(picPosition,numOfPicInTwoRows){ //把新增圖片和文字包裝成一個函式

    picPositionCounter = picPositionCounter + picPosition; //計算圖片在array的位置
    numOfPicInTwoRowsCounter = numOfPicInTwoRowsCounter+ numOfPicInTwoRows; //計算目前有多少張圖片在畫面上
    
    for(let i=picPositionCounter; i<numOfPicInTwoRowsCounter; i++){

        let item = document.createElement('div'); //建立項目item
        item.className="item";
        wrapTag.appendChild(item);  
    
        let picTag = document.createElement("div"); //建立項目子層 picture
        picTag.className="pic"
        item.appendChild(picTag)

        let img=document.createElement('img'); // 把圖片加入picture
        img.src = attractionLinkArray[i];
        picTag.appendChild(img);

    
        let textTag = document.createElement('div'); //建立項目子層 text
        textTag.className="txt"
        textTag.textContent=attractionNameArray[i] // 把景點名稱加入text
        item.appendChild(textTag);

        
    };
  
}











//});






