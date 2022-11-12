# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import csv
from csv import DictReader
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    filename = "state_market_tracker.csv"
    with open(filename,'r') as data:
        dict_reader = DictReader(data)
        list_of_dict = list(dict_reader)
        dict1 = {}
        property_type = 'All Residential'
        statelist = ["AK", "AL", "AR", "AZ", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "IA", "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MD", "ME", "MI", "MN", "MO", "MS", "NC", "NE", "NH", "NJ", "NM", "NV", "NY", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VA", "VT", "WA", "WI", "WV"]
        for j in range(len(statelist)) :
            state = statelist[j]
            print(state+ '\t', end =" ")
            for i in range(len(list_of_dict)):
                if(list_of_dict[i].get('state_code') == state and list_of_dict[i].get('property_type') == property_type):
                    tempdict = {list_of_dict[i].get('period_begin') : list_of_dict[i].get('median_sale_price')}
                    dict1.update(tempdict)
            # for x in sorted(dict1.keys(), reverse=True):
            #     print(x+ '\t', end =" ")
            # print(" ")
            for x in sorted(dict1.keys(), reverse=True):
                print(dict1.get(x)+ '\t', end =" ")
            print(" ")
