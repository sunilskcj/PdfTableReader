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
        
