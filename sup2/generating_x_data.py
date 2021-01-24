import itertools
import random


def create_all_available_hours(min_hour, max_hour, days, how_long):
    available_data = []
    for d in days:
        for h in range(min_hour, max_hour, how_long):
            available_data.append([d, h, h + how_long])
    return available_data


def create_finite_amount_of_data(min_hour, max_hour, days, how_long, max_depth = 7):
    all_data = []
    available_data = create_all_available_hours(min_hour, max_hour, days, how_long)
    max_iteration = len(available_data) - max_depth
    print("Max iteration: " + str(max_iteration))
    # big posibilities
    for i in range(len(available_data), max_iteration, -1):
        print("iteration: " + str(i))
        data_from_iteration = list(itertools.combinations(available_data, i))
        print(len(data_from_iteration))
        for tup_data in data_from_iteration:
            all_data.append(list(tup_data))
        data_from_iteration = None
    # small posibilities
    for i in range(2,max_depth):
        print("iteration: " + str(i))
        data_from_iteration = list(itertools.combinations(available_data, i))
        print(len(data_from_iteration))
        for tup_data in data_from_iteration:
            all_data.append(list(tup_data))
        data_from_iteration = None
    return all_data

def create_for_2_hour(max_depth = 7):
    av2 = create_finite_amount_of_data(8,19,[1,2,3,4,5],2, max_depth)

    with open('dataX2.txt', 'a') as the_file:
        for d in av2:
            row = str(d)
            row = row.replace("[", "").replace("]","").replace("(", "").replace(")", "")
            the_file.write(row)
            the_file.write("\n")

def create_for_1_hour(max_depth = 5):
    av1 = create_finite_amount_of_data(8,19,[1,2,3,4,5],1, max_depth)

    with open('dataX1.txt', 'a') as the_file:
        for d in av1:
            row = str(d)
            row = row.replace("[", "").replace("]","").replace("(", "").replace(")", "")
            the_file.write(row)
            the_file.write("\n")

create_for_2_hour(6)
create_for_1_hour(4)