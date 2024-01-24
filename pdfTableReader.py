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

