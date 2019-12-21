import pandas as pd
import datetime as dt

'''data frame being used'''

df = pd.read_excel(open('/Users/alexandrubordei/Downloads/try6.xlsx','rb'), sheet_name='Sheet1', usecols="C, D, F, H")
time = dt.date.today()

'''print statement'''

with open('outputs.txt', 'a+') as f:
    for _, row in df.iterrows():
        last_price, DLPM_cost, item, effective_date = row
        if pd.isnull(item) or pd.isnull(DLPM_cost):
            break
#Future price increase
        if DLPM_cost > last_price and effective_date.floor('D') > time:
            DLPM_syntax = ['key PA2', 'type DLPM#', 'key Enter', 'key tab', 'type ' + str(int(item)), 'key tab', 'key delete', 'key delete', 'type h',
                           'key enter', 'type ' + str(dt.datetime.strftime(effective_date, '%x')), 'key CursorDown', 'key CursorDown', 'key CursorDown',
                           'key CursorDown', 'key CursorDown', 'key CursorDown', 'key CursorDown', 'key CursorDown',
                           'key CursorDown', 'type '+ str(float(DLPM_cost)), 'key enter', 'type y', 'key enter',
                           'type ' + str(dt.datetime.strftime(effective_date, '%m%d%y')), 'key enter', 'key enter', 'key enter', 'key pf1', 'key Enter', 'key Enter', 'key Enter', 'key Enter',
                           'key tab', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y',
                           'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'key Enter', 'key tab', 'type y', 'type y', 'type y',
                           'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y',
                           'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'key enter', 'key tab', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y',
                           'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'key Enter', 'key tab',
                           'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y',
                           'type y', 'key Enter', 'key PF6']
            f.write(('\n'.join(DLPM_syntax) + '\n'))
#future price drop
        if DLPM_cost < last_price and effective_date.floor('D') > time:
            DLPM_syntax = ['key PA2', 'type DLPM#', 'key Enter', 'key tab', 'type ' + str(int(item)), 'key tab', 'key delete', 'key delete', 'type h',
                           'key enter', 'type ' + str(dt.datetime.strftime(effective_date, '%x')), 'key CursorDown', 'key CursorDown', 'key CursorDown',
                           'key CursorDown', 'key CursorDown', 'key CursorDown', 'key CursorDown', 'key CursorDown',
                           'key CursorDown', 'type '+ str(float(DLPM_cost)), 'key enter', 'type y', 'key enter',
                           'type ' + str(dt.datetime.strftime(effective_date, '%m%d%y')), 'key enter', 'key enter', 'key enter', 'key pf1', 'key Enter', 'key Enter', 'key Enter', 'key Enter',
                           'key tab', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y',
                           'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'key Enter', 'key tab', 'type y', 'type y', 'type y',
                           'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y',
                           'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'key enter', 'key tab', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y',
                           'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'key Enter', 'key tab',
                           'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y',
                           'type y', 'key Enter', 'key PF6']
            f.write(('\n'.join(DLPM_syntax) + '\n'))
#immediate price decrease
        if DLPM_cost < last_price and ((effective_date.floor('D') == time) or (effective_date.floor('D') <= time)):
            DLPM_syntax = ['key PA2', 'type DLPM#', 'key Enter','key Tab', 'type ' + str(int(item)), 'key Tab', 'key Delete', 'key Delete', 'type h',
                           'key Enter', 'type ' + str(dt.datetime.strftime(effective_date, '%x')), 'key CursorDown', 'key CursorDown',
                           'key CursorDown', 'key CursorDown', 'key CursorDown', 'key CursorDown', 'key CursorDown', 'key CursorDown',
                           'key CursorDown', 'type ' + str(float(DLPM_cost)), 'key Enter', 'type n', 'key enter', 'key enter', 'key PF1', 'key Enter', 'key enter', 'key Enter', 'key Enter', 'key Enter',
                           'key tab', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y',
                           'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'key Enter', 'key tab', 'type y', 'type y', 'type y',
                           'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y',
                           'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'key enter', 'key tab', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y',
                           'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'key Enter', 'key tab',
                           'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y',
                           'type y', 'key Enter', 'key PF6']
            f.write(('\n'.join(DLPM_syntax) + '\n'))
#Immediate price increase
        if DLPM_cost > last_price and ((effective_date.floor('D') == time) or (effective_date.floor('D') <= time)):
            DLPM_syntax = ['key PA2', 'type DLPM#', 'Key Enter', 'key Tab', 'type ' + str(int(item)), 'key Tab', 'key Delete', 'key Delete', 'type h',
                           'key Enter', 'type ' + str(dt.datetime.strftime(effective_date, '%x')), 'key CursorDown', 'key CursorDown',
                           'key CursorDown', 'key CursorDown', 'key CursorDown', 'key CursorDown',
                           'key CursorDown', 'key CursorDown', 'key CursorDown', 'type ' + str(float(DLPM_cost)),
                           'key Enter', 'key PF1', 'key Enter', 'key Enter', 'key Enter', 'key Enter',
                           'key tab', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y',
                           'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'key Enter', 'key tab', 'type y', 'type y', 'type y',
                           'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y',
                           'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'key enter', 'key tab', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y',
                           'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'key Enter',
                           'key tab', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y', 'type y',
                           'type y', 'key Enter', 'key PF6']
            f.write(('\n'.join(DLPM_syntax) + '\n'))