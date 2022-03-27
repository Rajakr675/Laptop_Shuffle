import random
safal={"Room 1)":{"praveen":{14,"Thinkpad"},"sajjad":{21,"dell"},"roshan":{23,"Thinkpad"},"mahendra":{22,"dell"},"amit":{24,"Thinkpad"},"abhimannu":{25,"Thinkpad-"},"pradip":{26,"Thinkpad"},"roshan":{27,"Thinkpad"},"rajesh":{28,"Thinkpade"}},
       'Room 3)':{'akash':{5,"acer"},"raja":{10,"acer"}},
       "Room 6)":{"suryasen":{3,"Thinkpad"},"aadarsh":{4,"Thinkpad"}},
       "Room 8)":{"pawan":{30,"dell"},"aniket":{32,"acer"},"suraj":{35,"dell"},"praveen-fc":{38,"Thinkpad"},"vikky":{40,"Thinkpad"}},
       "Room 7)":{"ujjawal":{42,"Thinkpade"},"saikiran":{45,"dell"},"satish":{46,"Thinkpad"},"kumawat":{48,"Thinkpad"}},
       "Room 9)":{"anuragi":{50,"Thinkpad"},"prathmesh":{52,"Thinkpad"},"nasir":{55,"Thinkpad"},"satyam":{56,"dell"}},
      "Room 10)":{"jaypatl":{60,"Thinkpad"},"akshit":{62,"Thinkpad"},"bhopu":{65,"Thinkpad"}},
      "Room 11)":{"arif":{70,"dell"}},
      "Room 12)":{"vikash":{75,"dell"},"bhumesh":{76,"acer"},"akash-tg":{78,"dell"},"ramteke":{80,"dell"}},
      "Room-library":{"manoj":{82,"THINKPAD"},"bharat":{85,"Thinkpad"},"nikhil":{87,"Thinkpad"},"bipin":{90,""}}}
for i in safal:
    if i=="Room 9)" or i=="Room-library":
        continue
    for j in safal[i]:
        
        num=random.randint(1,100)
        safal[i][j]=num

print(safal)