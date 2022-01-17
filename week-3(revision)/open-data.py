# import urllib.request as reqesut
# import json
# src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
# with reqesut.urlopen(src) as reponse:
#     data = json.load(reponse)


# landscape_list = data["result"]["results"]
# with open("data.csv", "w", encoding="utf-8") as file:
#     for data in landscape_list:
#         link=data["file"]
#         if ("jpg" in link) and ("JPG" in link):
#             if (link.index("jpg")<link.index("JPG")):
#                 lower_index = link.index("jpg")+3
#                 file.write(data["stitle"]+","+data["address"][5:8]+","+data["longitude"]+","+data["latitude"]+","+link[0:lower_index]+"\n")
#             else:
#                 upper_index = link.index("JPG")+3
#                 file.write(data["stitle"]+","+data["address"][5:8]+","+data["longitude"]+","+data["latitude"]+","+link[0:upper_index]+"\n")
#         elif "JPG" in link:
#             index = link.index("JPG")+3
#             file.write(data["stitle"]+","+data["address"][5:8]+","+data["longitude"]+","+data["latitude"]+","+link[0:index]+"\n")
#         elif "jpg" in link:
#             index = link.index("jpg")+3
#             file.write(data["stitle"]+","+data["address"][5:8]+","+data["longitude"]+","+data["latitude"]+","+link[0:index]+"\n")




#新code
import urllib.request as request
import json

src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as reponse:
    data = json.load(reponse)

attractions = data["result"]["results"]
with open("data.csv", "w", encoding="utf-8") as file:
    for one_attraction_info in attractions:
        picture_url = one_attraction_info["file"].split("https:")
        first_pic_url = "https:"+picture_url[1]
        district = one_attraction_info["address"][5:8]
        file.write(one_attraction_info["stitle"]+",+district,"+one_attraction_info["longitude"]+","+one_attraction_info["latitude"]+first_pic_url+"\n")


        


        


