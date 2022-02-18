let query_btn = document.getElementById("btn");
            let update_btn =document.getElementById("update_btn")

            let name_response = document.getElementById("name_response");
            let update_response = document.getElementById("update_response")

            query_btn.onclick = function(){
                let username = document.getElementById("username").value;
                
                fetch("/api/member?username="+username).then(function(response){
                  return response.json();
                }).then(function(result){
                    if (result["data"] === null){
                        name_response.innerHTML="查不到此使用者"
                    }else{
                        let name = result["data"]["name"];
                        let username = result["data"]["username"];
                        name_response.innerHTML=name +" ("+ username + ")";
                    }
                })
            };


            update_btn.addEventListener('click',function(){

                let name = document.getElementById('name').value;
                
                const data = {"name":name};
                console.log(data);
                fetch("/api/member",{
                    method: 'POST', 
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(data),
                    })
                    .then(response=>response.json())
                    .then(result=>{
                        if (result.hasOwnProperty('ok')){

                            update_response.innerHTML="更新成功"

                        }else{
                            update_response.innerHTML="更新失敗"
                        };
                    })


                })



