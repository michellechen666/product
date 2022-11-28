products = []
while True:
    name = input('請輸入商品名稱')
    if name == 'q':
        break
    price = input('請輸入商品價格')
    p = [] #小清單
    p.append(name)
    p.append(price)
    #7~9可直接寫成 p = [name, price]
    products.append(p) #讓products清單每個車廂裝著name和price
print(products)

products[0][0] #拿products大清單第一個項目再拿p清單的第一個項目

for p in products: #for loop就是印出清單每個項目
    print(p)
    print(p[0],'的價格是',p[1])

with open('product.csv','w') as f:
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n') #用csv要分隔要用,隔開；\n表示換行