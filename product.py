import os #operating system(從標準程式庫載os模組)

#讀取檔案
products = []  #將這行放在最外面的意圖是後續用到這個空清單
if os.path.isfile('products.csv'): #os路徑裡有isfile的功能(用來檢查檔案是否在)
    print('Yes!')
    with open('products.csv','r') as f: 
            for line in f: #for loop 會一行一行讀取檔案
                if '商品,價格' in line: #用5~6可以跳過商品跟價格欄位
                    continue #continue使用時機就是要跳到下一回的意思(尤其是在for loop或while loop情境會常用到，通常會放在比較高的位置)
                name, price = line.strip().split(',') #用這行的strip去把換行去掉並用逗點的方式split做分割
                #切割完的結果會是清單
                products.append([name,price]) #產出prodicts清單
    print(products)
    
else:
    print('找不到檔案')

#讓user輸入
while True:
    name = input('請輸入商品名稱')
    if name == 'q':
        break
    price = input('請輸入商品價格')
    price = int(price) #將字串price casting 成整數
    p = [] #小清單
    p.append(name)
    p.append(price)
    #7~9可直接寫成 p = [name, price]
    products.append(p) 
print(products)
#讓products清單每個車廂裝著name和price

products[0][0] #拿products大清單第一個項目再拿p清單的第一個項目

#印出所有購買紀錄
for p in products: #for loop就是印出清單每個項目
    print(p)
    print(p[0],'的價格是',p[1])

#寫入檔案
with open('products.csv','w') as f:
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')
        #用csv要分隔要用,隔開；\n表示換行
        #f.write表示寫入
        #str(p[1])~>將整數再轉換成字串，這樣字串跟字串才可以相加!!!!(很重要)