import pandas as pd
import datetime as dt
#import Pricing_Zones as zone_dictionary

'''data frame being used'''

df = pd.read_excel(open('/Users/alexandrubordei/Downloads/Vendor Pricing Template-39.xlsx','rb'), sheet_name='Main', usecols="B, F, K, L, M")
time = dt.date.today()

#zone_dictionary = {'NE': [150, 160, 171, 810, 811, 814, 815, 820, 822, 834, 882],
#                   'NYC': [110, 112, 121, 163, 167, 818],
#                   'NY': [144, 161, 801, 802, 803, 806, 819],
#                   'NJ': [111, 173, 194, 807, 832, 874, 895],
#                   'SJP': [804, 808, 812, 816, 852],
#                   'WPA': [816, 823],
#                   'VM': [125, 185, 805, 809, 817, 855]}

zone_dictionary = {'NE': [150],
                   'NYC': [110],
                   'NY': [144],
                   'NJ': [111],
                   'SJP': [804],
                   'WPA': [816],
                   'VM': [125],
                   'test': [895, 163]}

'''print statement'''

def DLPM_local(df):
    with open('zones_output_local.txt', 'a+') as f:
        for _, row in df.iterrows():
            item, zone, last_price, DLPM_cost, effective_date = row
            if pd.isnull(item) or pd.isnull(DLPM_cost):
                break
            for store in zone_dictionary.get(zone):
# Future price change
                if DLPM_cost > last_price or DLPM_cost < last_price and effective_date.floor('D') > time:
                    DLPM_syntax = ['key tab', 'type ' + str(int(store)) + '-' + f"{int(item):0>7}", 'key tab',
                                   'key delete', 'key delete', 'type h',
                                   'key enter', 'type ' + str(dt.datetime.strftime(effective_date, '%x')),
                                   'key CursorDown', 'key CursorDown', 'key CursorDown',
                                   'key CursorDown', 'key CursorDown', 'key CursorDown', 'key CursorDown',
                                   'key CursorDown',
                                   'key CursorDown', 'type ' + str(float(DLPM_cost)), 'key enter', 'type y',
                                   'key enter',
                                   'type ' + str(dt.datetime.strftime(effective_date, '%m%d%y')), 'key enter',
                                   'key enter', 'key enter', 'key pf1', 'key enter', 'key enter', 'key enter']
                    f.write(('\n'.join(DLPM_syntax) + '\n'))
# immediate price increase
                if DLPM_cost < last_price and (
                        (effective_date.floor('D') == time) or (effective_date.floor('D') <= time)):
                    DLPM_syntax = ['key Tab',  'type ' + str(int(store)) + '-' + f"{int(item):0>7}", 'key Tab',
                                   'key Delete', 'key Delete', 'type h',
                                   'key Enter', 'type ' + str(dt.datetime.strftime(effective_date, '%x')),
                                   'key CursorDown', 'key CursorDown', 'key CursorDown',
                                   'key CursorDown', 'key CursorDown', 'key CursorDown', 'key CursorDown',
                                   'key CursorDown',
                                   'key CursorDown', 'type ' + str(float(DLPM_cost)), 'key Enter', 'key PF1',
                                   'key Enter',
                                   'key Enter', 'key Enter']
                    f.write(('\n'.join(DLPM_syntax) + '\n'))
# Immediate price decrease
                if DLPM_cost > last_price and (
                        (effective_date.floor('D') == time) or (effective_date.floor('D') <= time)):
                    DLPM_syntax = ['key Tab',  'type ' + str(int(store)) + '-' + f"{int(item):0>7}", 'key Tab',
                                   'key Delete', 'key Delete', 'type h',
                                   'key Enter', 'type ' + str(dt.datetime.strftime(effective_date, '%x')),
                                   'key CursorDown', 'key CursorDown',
                                   'key CursorDown', 'key CursorDown', 'key CursorDown', 'key CursorDown',
                                   'key CursorDown', 'key CursorDown', 'key CursorDown',
                                   'type ' + str(float(DLPM_cost)),
                                   'key Enter', 'type n', 'key Enter', 'key Enter', 'key PF1', 'key Enter', 'key Enter', 'key Enter']
                    f.write(('\n'.join(DLPM_syntax) + '\n'))
if __name__ == '__main__':
    DLPM_local(df)