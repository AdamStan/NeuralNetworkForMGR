import random
import itertools

def create_all_available_hours(min_hour, max_hour, days, how_long):
    available_data = []
    for d in days:
        for h in range(min_hour, max_hour):
            available_data.append([d, h, h + how_long])
    return available_data

def create_finite_amount_of_data(min_hour, max_hour, days, how_long, max_depth = 5):
    all_data = []
    available_data = create_all_available_hours(min_hour, max_hour, days, how_long)
    max_iteration = len(available_data) - max_depth
    print("Max iteration: " + str(max_iteration))
    # big possibilities
    for i in range(2, max_depth):
        print("iteration: " + str(i))
        data_from_iteration = list(itertools.combinations(available_data, i))
        print(len(data_from_iteration))
        for tup_data in data_from_iteration:
            all_data.append([])
            for three in tup_data:
                for num in three:
                    all_data[-1].append(num)
        data_from_iteration = None
    return all_data

def create_finite_amount_from_mid(min_hour, max_hour, days, how_long, it):
    all_data = []
    available_data = create_all_available_hours(min_hour, max_hour, days, how_long)
    print("iteration: " + str(it))
    data_from_iteration = list(itertools.combinations(available_data, it))
    print(len(data_from_iteration))
    for tup_data in data_from_iteration:
        all_data.append(tup_data[0])
        all_data.append(tup_data[1])
        all_data.append(tup_data[2])
    return all_data

def create_for_2_hour(max_depth = 5):
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

def create_3input_available_hours(av_hours_from_plan, plan_to_manipulate, hours_to_delete=3):
    """
    It will randomly remove some hours, without hour which should be taken
    :param plan_hours:
    :param hours_to_delete:
    :return:
    """
    if len(av_hours_from_plan) != 165:
        raise Exception("av_hours_from_plan should be flat and have 165 length");

    new_plan_to_manipulate = repair_plan_to_manipulate(av_hours_from_plan, plan_to_manipulate)
    teachers_hours = new_plan_to_manipulate
    room_hours = new_plan_to_manipulate.copy()

    # wylosuj hours_to_delete razy godzinki do usuniecia, ale tak zeby zostala godzina do wybrania

    # zwrocenie 3 list
    return av_hours_from_plan.copy(), teachers_hours, room_hours

def get_available_hours(av_hours):
    av_hours_number = 0
    for index in range(0, len(av_hours), 3):
        if av_hours[index] != 0:
            av_hours_number += 1
    return av_hours_number

def remove_data(hours_data, hours_to_delete, av_hours_in_plan):
    hours_deleted = []
    av_indexes = [i for i in range(0, av_hours_in_plan)]
    for _ in range(hours_to_delete):
        remove_index = -1
        while (av_hours_in_plan - len(hours_deleted)) > 2:
            remove_index = random.choice(av_indexes)
            if remove_index not in hours_deleted:
                break

        if remove_index == -1:
            break
        hours_data[remove_index * 3] = 0
        hours_data[remove_index * 3 + 1] = 0
        hours_data[remove_index * 3 + 2] = 0
        hours_deleted.append(remove_index)

def repair_plan_to_manipulate(all_possibilities, plan_to_manipulate):
    # av_hours_from_plan - contains all 55 possibilities:
    # [ 1, 8, 10, 1, 9, 11, ... , 5, 18, 20 ]
    # plan_to_manipulate contains not ordered:\
    # [ 1, 9, 11, 4, 8, 10, ... ]
    # get plan_to_manipulate in form:
    # [ 0, 0, 0, 1, 9, 11, 0, 0, 0, ..., 4, 8, 10, ... ]
    ptm_index = 0
    new_plan_to_manipulate = []
    for i in range(0, len(all_possibilities), 3):
        if all_possibilities[i] == plan_to_manipulate[ptm_index] and \
                all_possibilities[i + 1] == plan_to_manipulate[ptm_index + 1] and \
                all_possibilities[i + 2] == plan_to_manipulate[ptm_index + 2]:
            new_plan_to_manipulate.append(plan_to_manipulate[ptm_index])
            new_plan_to_manipulate.append(plan_to_manipulate[ptm_index + 1])
            new_plan_to_manipulate.append(plan_to_manipulate[ptm_index + 2])
            ptm_index += 3
            if ptm_index >= len(plan_to_manipulate):
                break
        else:
            new_plan_to_manipulate.append(0)
            new_plan_to_manipulate.append(0)
            new_plan_to_manipulate.append(0)
    # print("data to manipulate")
    # print(len(new_plan_to_manipulate))
    # print(new_plan_to_manipulate)
    return new_plan_to_manipulate
