def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    quantity_dict=dict(zip(reqd_gems,reqd_quantity))
    price_dict=dict(zip(gems_list,price_list))
    if(set(reqd_gems).issubset(set(gems_list))):
     for (k,v) in quantity_dict.items():
        print(k,v,price_dict[k],price_dict[k]*v)
     bill_amount= (sum([price_dict[k] * v for k, v in quantity_dict.items()]))
    else:
        bill_amount=-1
    return(bill_amount)
gems_list=["Emerald","Ivory","Jasper","Ruby","Garnet"]
price_list=[1760,2119,1599,3920,3999]
reqd_gems=["Ivory","Emerald","Garnet"]
reqd_quantity=[3,10,12]
bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)