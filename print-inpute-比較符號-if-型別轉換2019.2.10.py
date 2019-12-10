#print練習
price = 10
pen = 0.38
rain =True
name = 'jane'
print(price,pen,rain,name)


#inpute練習
name = input('請輸入名字:')
print('嗨', name)

x = input ('請輸入身高:')
y = input ('請輸入體重:')
print ('你的身高:',x,'你的體重:',y)


#比較符號  "問是非題答案都是true、false"變成布林值
x = 5  #定義x值
print(x == 5) #問x是不是等於5值，正確顯示true
print(x != 5) #問x是不是等於5值，顯示false
print(x > 2) #問x是不是大於2值，顯示true
print(x < 2) #問x是不是小於2值，顯示false
print(x >= 2) #問x是不是大於等於2值，顯示true
print(x <= 2) #問x是不是小於等於2值，顯示false


#if
rain = input('請問今天有沒有下雨: ')

if rain == '有':
    print('撐傘出門')
    print('買一包洋芋片')
    print('在家看電影')


#型別轉換
age = input('請輸入年齡: ')   #input會把輸入的內容都變成字串，如果下行直接輸入if age >=20: ，會跳出錯誤訊息:不可將字串與數字做比較
age = int(age) #型別轉換，將age轉成整數
if age >=20:
    print ('你可以投票')
