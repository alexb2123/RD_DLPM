import pandas as pd
import datetime as dt
import Pricing_Zones



'''data frame being used'''

df = pd.read_excel(open('/Users/alexandrubordei/Downloads/Vendor Pricing Template-24.xlsx','rb'), sheet_name='Main', usecols="B, F, K, L, M")
#zones = pd.read_excel(open('/Users/alexandrubordei/Downloads/Vendor Pricing Template-24.xlsx','rb'), sheet_name='Pricing Zones', usecols="D, E", index_col=1)


time = dt.date.today()

#result = pd.merge(df, zones, left_on='Zone', right_index=True, how='left', sort=False)
#stores = result.Stores[2]
#store_ids = [str(i).strip() for i in stores.replace('\n', '').split(',')]



#print(zones.head())
#print(stores)




'''print statement'''

def DLPM_local(df, result):
    with open('output_local.txt', 'a+') as f:
        for _, row in df.iterrows():
            item, store_ids, last_price, DLPM_cost, effective_date = row
            if pd.isnull(item) or pd.isnull(DLPM_cost):
                break
    #Future price change
            if DLPM_cost > last_price or DLPM_cost < last_price and effective_date.floor('D') > time:
                DLPM_syntax = ['key tab', 'type ' + str(int(store_ids)) + '-' + str(int(item)), 'key tab', 'key delete', 'key delete', 'type h',
                               'key enter', 'type ' + str(dt.datetime.strftime(effective_date, '%x')), 'key CursorDown', 'key CursorDown', 'key CursorDown',
                               'key CursorDown', 'key CursorDown', 'key CursorDown', 'key CursorDown', 'key CursorDown',
                               'key CursorDown', 'type ' + str(float(DLPM_cost)), 'key enter', 'type y', 'key enter',
                               'type ' + str(dt.datetime.strftime(effective_date, '%m%d%y')), 'key enter', 'key enter', 'key enter', 'key pf1', 'key enter', 'key enter', 'key enter']
                f.write(('\n'.join(DLPM_syntax) + '\n'))
    #immediate price decrease
            if DLPM_cost < last_price and ((effective_date.floor('D') == time) or (effective_date.floor('D') <= time)):
                DLPM_syntax = ['key Tab', 'type ' + str(int(zones)) + '-' + str(int(item)), 'key Tab', 'key Delete', 'key Delete', 'type h',
                               'key Enter', 'type ' + str(dt.datetime.strftime(effective_date, '%x')), 'key CursorDown', 'key CursorDown', 'key CursorDown',
                               'key CursorDown', 'key CursorDown', 'key CursorDown', 'key CursorDown', 'key CursorDown',
                               'key CursorDown', 'type ' + str(float(DLPM_cost)), 'key Enter', 'key PF1', 'key Enter',
                               'key Enter', 'key Enter']
                f.write(('\n'.join(DLPM_syntax) + '\n'))
    #Immediate price increase
            if DLPM_cost > last_price and ((effective_date.floor('D') == time) or (effective_date.floor('D') <= time)):
                DLPM_syntax = ['key Tab', 'type ' + str(int(zones)) + '-' + str(int(item)), 'key Tab', 'key Delete', 'key Delete', 'type h',
                               'key Enter', 'type ' + str(dt.datetime.strftime(effective_date, '%x')), 'key CursorDown', 'key CursorDown',
                               'key CursorDown', 'key CursorDown', 'key CursorDown', 'key CursorDown',
                               'key CursorDown', 'key CursorDown', 'key CursorDown', 'type ' + str(float(DLPM_cost)),
                               'key Enter', 'key PF1', 'key Enter', 'key Enter', 'key Enter']
                f.write(('\n'.join(DLPM_syntax) + '\n'))
if __name__ == '__main__':
    DLPM_local(df, zones)