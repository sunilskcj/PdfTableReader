import json
from decimal import Decimal
from itertools import chain
from datetime import datetime
import re
import requests

import pdfplumber
class TransactionModel:
    # def __init__(self, date, name):
    #     self.date = date
    #     self.age = name
    # def custom_serializer(obj):
    #     if isinstance(obj, TransactionModel):
    #         return {"name": obj.date, "age": obj.name}
    #     raise TypeError("Object is not JSON serializable.")
    TranListOfPages=[]
    with pdfplumber.open("XXXX",password= 'XXX') as f:
        for i in f.pages:
            #transaction=i.extract_table()
            TranListOfPages.append(i.extract_table())
    TransList = list(chain.from_iterable(TranListOfPages))
    l = 0
    length = len(TransList)
    newTransList = []
    for t in TransList:
        l = l + 1
        if t[0] is not None:
            day = re.search('\d{2}/\d{2}/\d{4}', t[0])
            if day is not None:
                newTransList.append(t)
    for n in newTransList:
        if 'Cr' in n[2]:
            n[2] = n[2].replace('Cr', '')
            n[3] = '0'
        else:
            n[3] = '1'
    # print(newTransList)
        # json_string = json.dumps(newTransList, default=custom_serializer, indent=2)
        json_dict = {"transaction": [
            {"expenseDate": datetime.strptime(value[0], '%d/%m/%Y').strftime("%Y-%m-%d"), "expenses": value[1],
             "amount": value[2].replace(',', ''), "expenseType": value[3]} for value in newTransList]}
        # json_string = json.dumps(json_dict)
        transaction = json_dict["transaction"]
        print(transaction)
        api_url = "http://localhost:5244/api/Expenditure"
        for t in transaction:
            response = requests.post(api_url, json=t)
            print(response.json())
