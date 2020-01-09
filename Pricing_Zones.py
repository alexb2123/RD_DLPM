zone_dictionary = {


'NE': [150, 160, 171, 810, 811, 814, 815, 820, 822, 834, 882],


'NYC': [110, 112, 121, 163, 167, 818],


'NY': [144, 161, 801, 802, 803, 806, 819],


'NJ': [111, 173, 194, 807, 832, 874, 895],


'SJP': [804, 808, 812, 816, 852],


'WPA': [816, 823],


'VM': [125, 185, 805, 809, 817, 855]
}

#print(zone_dictionary.keys())

#print(type(zone_dictionary))

for store in zone_dictionary['NE']:
    print(store)