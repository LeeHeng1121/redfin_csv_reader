# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import csv
import json
from csv import DictReader
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    f = open('counties_list.json')
    y = json.load(f)
    dict_county = {}
    output = open('all_counties.txt', 'w')
    for i in y:
        state = i['State']
        county = i['County']
        if(dict_county.__contains__(state)) :
            dict_county[state].add(county)
        else :
            dict_county[state] = {county}
    # print(dict_county['Texas'])
    # for i in dict_county['Texas']:
    #     print(i)
    for i in dict_county:
        dict_county[i] = sorted(dict_county[i])
    statelist = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "District of Columbia", "Florida", "Georgia", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin"]
    for j in range(len(statelist)) :
            state = statelist[j]
            filename = "county_market_tracker.csv"
            with open(filename,'r') as data:
                dict_reader = DictReader(data)
                list_of_dict = list(dict_reader)
                dict1 = {}
                property_type = 'All Residential'
                countyList = dict_county[state]
                for c in countyList :
                    county = c
                    print(state + '\t' + county)
                    output.write(state)
                    output.write('\t')
                    output.write(county)
                    output.write('\t')
                    for i in range(len(list_of_dict)):
                        if(list_of_dict[i].get('region') == county and list_of_dict[i].get('property_type_id') == property_type):
                            tempdict = {list_of_dict[i].get('period_begin') : list_of_dict[i].get('median_sale_price_mom')}
                            dict1.update(tempdict)
                    # for x in sorted(dict1.keys(), reverse=True):
                    #     print(x+ '\t', end =" ")
                    # print(" ")
                    for x in sorted(dict1.keys(), reverse=True):
                        # print(dict1.get(x)+ '\t', end =" ")
                        output.write(dict1.get(x))
                        output.write('\t')
                    # print(" ")
                    output.write('\n')
