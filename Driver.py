import pandas as pd;
import numpy as np;
import itertools
from itertools import permutations
import math;

tree_data = pd.read_csv("./input.csv", header=[0]);
sampleSize = tree_data[tree_data.columns[len(tree_data.columns)-1]].sum();
options = {};

for i in range(1,len(tree_data.columns)-1):
    options[tree_data.columns[i]] = list(pd.unique(tree_data[tree_data.columns[i]]));

def my_function(data,size,options,winner = {}):

    if not options:
        return winner;

    winnerValue = float('inf');
    winnerOption = 0;

    for option in options:
        temp = [options[option],*winner.values()];
        combinations = list(itertools.product(*temp));
        entropy = 0;


        for combination in combinations:
            v = 0;

            condition = pd.Series(True, index=data.index);
            condition &= data[option] == combination[0];
            temp2 = [*winner];
            
            for combo in range(1,len(combination)):
                condition &= data[temp2[combo-1]] == combination[combo];

            if len(data[condition]) == 0:
                continue;

            if len(data[condition]) == 1:
                continue;

            tempTable = data[condition];
            conditionSum = tempTable[tempTable.columns[len(tempTable.columns)-1]].sum();

            v += np.sum(
                (tempTable[tempTable.columns[len(tempTable.columns)-1]] / conditionSum) *
                (np.log2(conditionSum / tempTable[tempTable.columns[len(tempTable.columns)-1]]))
            );

            v *= conditionSum/size;
            entropy += v;


        if entropy < winnerValue:
            winnerValue = entropy;
            winnerOption = option;

    winner[winnerOption] = options[winnerOption];
    options.pop(winnerOption);

    return my_function(data,size,options,winner);


decisionTree = my_function(tree_data,sampleSize,options);

for key in decisionTree.keys():
    print(key + " -> ");