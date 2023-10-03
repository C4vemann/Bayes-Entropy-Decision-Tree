import pandas as pd;
import numpy as np;
import itertools
from itertools import permutations
import math;



# #comb_array = list(itertools.product(*options));
# comb_array = list(itertools.product(options[0],options[1],options[3]));

# print(tree_data[["Overall Type","Arrangement","Margin sub-category"]].isin(options[0],options[1],options[3]));

# #outputs the set from a given tree_data attribute from the options dictionary
# for column in range(1,len(tree_data.columns)-1):
#     #print(options.get(tree_data.columns[column]));
#     print();

# array = ["Overall Type", "Arrangement", "Margin"];
# winner = ["Margin sub-category"];

# for i in array:
#     for j in options.get(i):
#         print(j);

# for i in range(1,len(tree_data.columns)-1):
#     print(i);
#print(tree_data[options[array[0]]]);

tree_data = pd.read_csv("./input.csv", header=[0]);
sampleSize = tree_data[tree_data.columns[len(tree_data.columns)-1]].sum();
options = {};

for i in range(1,len(tree_data.columns)-1):
    options[tree_data.columns[i]] = list(pd.unique(tree_data[tree_data.columns[i]]));

def my_function(data,size,options,winner = {}):

    if not options:
        return winner;

    winnerValue = float('inf');

    entropy = 0;

    # for column in range(1,len(data.columns)-1):
    #     temp = [options.get(data.columns[column]),*winner.values()];
    #     print(temp);

    for option in options:
        temp = [options[option],*winner.values()];
        combinations = list(itertools.product(*temp));
        print(len(combinations));

        for combination in combinations:
            condition = pd.Series(True, index=data.index);
            print("option:", data[option]);
            print("combination:", combination[0]);
            condition &= data[option] == combination[0];
            temp2 = [*winner];
            
            for combo in range(1,len(combination)-1):
                print("combo:", combo);
                print("jello", temp2[combo]);
                print(data[temp2[combo]], combination[combo]);
                # condition &= data[temp2[combo]] == combination[combo];
            # print(data[condition]);


            


        # print(temp);

    winner['Margin'] = options['Margin'];
    winner['Overall Type'] = options['Overall Type'];
    options.pop('Margin');
    options.pop('Overall Type');

    my_function(data,size,options,winner);
    # for option in options:
    #     temp = [option, *winner];
    #     for property in temp:
    #     print(temp);

        #for property in option['columnSet']:

            #print(property);



    # for column in range(1,len(data.columns)-1):
    #     e = 0;
    #     for option in options[column-1]:
    #         condition = data[data.columns[column]] == option;
    #         selectedRows = data[condition];
    #         optionTotal = selectedRows[selectedRows.columns[len(selectedRows.columns)-1]].sum();
    #         v = 0;
    #         for row in selectedRows.index:
    #             temp = selectedRows[selectedRows.columns[len(selectedRows.columns)-1]][row];
    #             x = (temp/optionTotal)*(math.log2(optionTotal/temp));
    #             v+=x;
    #         v = v * (optionTotal/size);
    #         e += v;
    #     if e < winnerValue:
    #         #winner.append(options.pop(column-1));
    #         winnerValue = e;
    #         #winner = data.columns[column];

    # print(winner);
    # print(winnerValue);


    
    #winner.append(options.popitem());

    # print(winner);
    # print(options);
    # print("\n");

    #my_function(data,options);

my_function(tree_data,sampleSize,options);