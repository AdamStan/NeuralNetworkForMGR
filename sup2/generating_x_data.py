import itertools
import random


def create_all_available_hours(min_hour, max_hour, days, how_long):
    available_data = []
    for d in days:
        for h in range(min_hour, max_hour, how_long):
            available_data.append([d, h, h + how_long])
    return available_data


def create_finite_amount_of_data(min_hour, max_hour, days, how_long, max_depth=7):
    all_data = []
    available_data = create_all_available_hours(min_hour, max_hour, days, how_long)
    max_iteration = len(available_data) - max_depth
    print("Max iteration: " + str(max_iteration))
    # big possibilities
    for i in range(len(available_data), max_iteration, -1):
        print("iteration:" + str(i))
        data_from_iteration = list(itertools.combinations(available_data, i))
        print(len(data_from_iteration))
        for tup_data in data_from_iteration:
            all_data.append(list(tup_data))

    # small possibilities
    for i in range(2, max_depth):
        print("iteration: " + str(i))
        data_from_iteration = list(itertools.combinations(available_data, i))
        print(len(data_from_iteration))
        for tup_data in data_from_iteration:
            all_data.append(list(tup_data))

    return all_data


def create_finite_amount_from_mid(min_hour, max_hour, days, how_long, it):
    all_data = []
    available_data = create_all_available_hours(min_hour, max_hour, days, how_long)
    print("iteration: " + str(it))
    data_from_iteration = list(itertools.combinations(available_data, it))
    print(len(data_from_iteration))
    for tup_data in data_from_iteration:
        all_data.append(list(tup_data))
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


def get_available_hours(av_hours):
    av_hours_number = 0
    for index in range(0, len(av_hours)):
        if av_hours[index][0] != 0:
            av_hours_number += 1
    return av_hours_number


def prepare_data(the_same_start=20, min_hour=8, max_hour=19, how_long=2, days=[1,2,3,4,5]):
    all_data = []
    available_data = create_all_available_hours(min_hour, max_hour, days, how_long)
    for iteration in range(1, len(available_data) + 1):
        print("iteration: " + str(iteration))
        starts_dict = dict()
        data_from_iteration = list(itertools.combinations(available_data, iteration))
        print("data length: " + str(len(data_from_iteration)))
        for iteration_data in data_from_iteration:
            if str(iteration_data[0]) not in starts_dict.keys():
                starts_dict[str(iteration_data[0])] = 0
            starts_dict[str(iteration_data[0])] += 1
            if starts_dict[str(iteration_data[0])] > the_same_start:
                continue
            new_sample = []
            for three in list(iteration_data):
                new_sample.append(list(three))
            all_data.append(new_sample)
        print("All data size:")
        print(len(all_data))
    return all_data
