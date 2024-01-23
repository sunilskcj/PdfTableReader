import json
from decimal import Decimal
from itertools import chain
from datetime import datetime
import re
import requests

import pdfplumber
class TransactionModel:

    TranListOfPages=[]
    with pdfplumber.open("XXXX",password= 'XXX') as f:
        for i in f.pages:
            #transaction=i.extract_table()
            TranListOfPages.append(i.extract_table())

