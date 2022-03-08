def dis(price,discount):
    ds=price*(discount/100)
    sp=price-ds
    return sp
ori_price=int(input("Enter original price:"))
dis_per=int(input("Enter discount percentage:"))
print(dis(ori_price,dis_per))


##original_price=160
##discount_price=5
##def dis(160,5):
##    ds=160*(5/100)=8
##    sp=160-8=152
