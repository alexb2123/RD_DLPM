#Ad Funds DP
import pandas as pd
import datetime as dt

'''data frame being used'''

df = pd.read_excel(open('/Users/alexandrubordei/Downloads/Vendor Pricing Template-20.xlsx','rb'), sheet_name='Main', usecols="B, R, S, T")
time = dt.date.today()

'''print statement'''

with open('bill_back_output.txt', 'a+') as f:
    for _, row in df.iterrows():
        item, bill_back, effective_date, end_date = row
        if pd.isnull(item) or pd.isnull(bill_back):
            break
        bill_back_syntax = ['key Tab', 'type ' + str(int(item)), 'key Tab', 'key Delete', 'key Delete', 'key delete', 'key delete', 'key delete', 'type an', 'type a', 'key Enter', 'type ' + str(dt.datetime.strftime(effective_date, '%x')), 'type ' + str(dt.datetime.strftime(end_date, '%x')),
                            'key CursorDown', 'key CursorDown', 'key CursorDown', 'key CursorDown', 'key CursorDown', 'key CursorDown', 'key CursorDown', 'key CursorDown', 'key CursorDown', 'key CursorDown', 'key CursorDown', 'key CursorDown', 'key Tab', 'type 999999', 'key tab',
                            'type ' + str(float(bill_back)), 'key Enter', 'key Enter', 'key tab', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y',
                            'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'key Enter', 'key tab', 'type y', 'type y', 'type y',
                            'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y',
                            'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'key enter', 'key tab', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y',
                            'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'key Enter', 'key tab',
                            'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y',
                            'type y', 'key Enter', 'key PF6']
        f.write(('\n'.join(bill_back_syntax) + '\n'))