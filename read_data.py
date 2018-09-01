import pandas as pd
import json

with open('all_leads.json') as data_file:
   data = json.load(data_file)

print(data)
