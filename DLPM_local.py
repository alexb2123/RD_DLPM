import pandas as pd
import datetime as dt
import Pricing_Zones


#print(Pricing_Zones.NE)
'''data frame being used'''

df = pd.read_excel(open('/Users/alexandrubordei/Downloads/Vendor Pricing Template-36.xlsx','rb'), sheet_name='Main', usecols="B, K, L, M")
time = dt.date.today()



'''print statement'''

def DLPM_local(df):
    with open('output_local.txt', 'a+') as f:
        for _, row in df.iterrows():
            item, last_price, DLPM_cost, effective_date = row
            if pd.isnull(item) or pd.isnull(DLPM_cost):
                break
#Future price change
            if DLPM_cost > last_price or DLPM_cost < last_price and effective_date.floor('D') > time:
                DLPM_syntax = ['key tab', 'type ' + str(int(item)), 'key tab', 'key delete', 'key delete', 'type h',
                               'key enter', 'type ' + str(dt.datetime.strftime(effective_date, '%x')), 'key CursorDown', 'key CursorDown', 'key CursorDown',
                               'key CursorDown', 'key CursorDown', 'key CursorDown', 'key CursorDown', 'key CursorDown',
                               'key CursorDown', 'type '+ str(float(DLPM_cost)), 'key enter', 'type y', 'key enter',
                               'type ' + str(dt.datetime.strftime(effective_date, '%m%d%y')), 'key enter', 'key enter', 'key enter', 'key pf1', 'key enter', 'key enter', 'key enter']
                f.write(('\n'.join(DLPM_syntax) + '\n'))
#immediate price decrease
            if DLPM_cost < last_price and ((effective_date.floor('D') == time) or (effective_date.floor('D') <= time)):
                DLPM_syntax = ['key Tab', 'type ' + str(int(item)), 'key Tab', 'key Delete', 'key Delete', 'type h',
                               'key Enter', 'type ' + str(dt.datetime.strftime(effective_date, '%x')), 'key CursorDown', 'key CursorDown', 'key CursorDown',
                               'key CursorDown', 'key CursorDown', 'key CursorDown', 'key CursorDown', 'key CursorDown',
                               'key CursorDown', 'type ' + str(float(DLPM_cost)), 'key Enter', 'key PF1', 'key Enter',
                               'key Enter', 'key Enter']
                f.write(('\n'.join(DLPM_syntax) + '\n'))
#Immediate price increase
            if DLPM_cost > last_price and ((effective_date.floor('D') == time) or (effective_date.floor('D') <= time)):
                DLPM_syntax = ['key Tab', 'type ' + str(int(item)), 'key Tab', 'key Delete', 'key Delete', 'type h',
                               'key Enter', 'type ' + str(dt.datetime.strftime(effective_date, '%x')), 'key CursorDown', 'key CursorDown',
                               'key CursorDown', 'key CursorDown', 'key CursorDown', 'key CursorDown',
                               'key CursorDown', 'key CursorDown', 'key CursorDown', 'type ' + str(float(DLPM_cost)),
                               'key Enter', 'key PF1', 'key Enter', 'key Enter', 'key Enter']
                f.write(('\n'.join(DLPM_syntax) + '\n'))
if __name__ == '__main__':
    DLPM_local(df)