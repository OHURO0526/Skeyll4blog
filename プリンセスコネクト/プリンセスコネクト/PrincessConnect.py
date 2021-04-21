import discord


TOKEN = 'NjQ5NTYxMTE2NDg1MDkxMzI4.Xd-k7g.fpd8KrciNTDFlqgRyHr0BMWglVI' #TOKENIDの部分を自分のIDに変える


client = discord.Client()


BossNum = ["1","2","3","4","5"]
# If someone reserve an attack, add to this list.
Booking1 = [1ボス]
Booking2 = [2ボス]
Booking3 = [3ボス]
Booking4 = [4ボス]
Booking5 = [5ボス]


@client.event
async def on_message(message):
    listFlag = 0
    bookFlag = 0
    endFlag = 0
    displayFlag = 0

    
    if message.content.startswith("凸"):
       if "list" in message.content: # Call a list
           listFlag = 1
       elif "消" in message.content: # Initialize all lists
           endFlag = 1
       elif "リスト" in message.content: # Call all arrays
           displayFlag = 1
       else: # Book
           bookFlag = 1


       if listFlag == 1:
           for Boss in BossNum:
               tmpList = []
               if Boss in message.content:
                  BookList = "Booking" + Boss
                  tmpList = [x[0] for x in eval(BookList)]
                  member = ""
                  for one in tmpList:
                      member += one + " "
                  await message.channel.send("Boss" + Boss + ":" + member)
           listFlag =  0


       elif endFlag == 1:
           for Boss in BossNum:
                  BookList = "Booking" + Boss
                  eval(BookList).clear()
           reply = "予約を全削除"
           await message.channel.send(reply)
           endFlag = 0


       elif bookFlag == 1:
           bossCount = 0
           for Boss in BossNum:
               if Boss in message.content:
                  BookList = "Booking" + Boss
                  eval(BookList).append([message.author.display_name, str(message.author.mention)])
                  bossCount += 1
           if bossCount >= 1:
               reply = str(bossCount) + "件の予約 >" + message.author.display_name
               await message.channel.send(reply)
           bookFlag = 0


       elif displayFlag == 1: # Display all book list
           for Boss in BossNum:
               tmpList = []
               BookList = "Booking" + Boss
               tmpList= [x[0] for x in eval(BookList)]
               member = ""
               for one in tmpList:
                   member += one + " "
               await message.channel.send("Boss" + Boss + ":" + member)
           displayFlag = 0


    elif message.content.startswith("f"):
        for Boss in BossNum:
               if Boss in message.content:
                   BookList = "Booking" + Boss
                   eval(BookList).remove([message.author.display_name,str(message.author.mention)]) 
        reply = "削除完了 >" + message.author.display_name
        await message.channel.send(reply)


   
    elif message.content.startswith("コマンド"):
        reply = "凸:凸 1-5 / 予約表示:rsv list 1-5 / 予約全表示:凸リスト / 予約削除:f 1-5 / 予約全削除:凸消"
        await message.channel.send(reply)
         

client.run(TOKEN)

