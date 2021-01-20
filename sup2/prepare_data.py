import itertools

# from testing_x_train_data import x_train2, y_train

def prepare_x_train_data(x_train):
    new_data = []
    for av_hours in x_train:
        for index in range(len(av_hours), 55):
            av_hours.append([0,0,0])
        new_data.append(av_hours)
    return new_data

def prepare_y_train_data(y_train):
    new_data = []
    for propabilities in y_train:
        for index in range(len(propabilities), 55):
            propabilities.append(0)
        new_data.append(propabilities)
    return new_data


# x_train_ready = prepare_x_train_data(x_train2)
# y_train_ready = prepare_y_train_data(y_train)

def create_all_available_hours(min_hour, max_hour, days, how_long):
    available_data = []
    for d in days:
        for h in range(min_hour, max_hour, how_long):
            available_data.append([d, h, h + how_long])
    return available_data

def create_finite_amount_of_data(min_hour, max_hour, days, how_long):
    all_data = []
    available_data = create_all_available_hours(min_hour, max_hour, days, how_long)
    for i in range(1, len(available_data) + 1):
        print("iteration: " + str(i))
        data_from_iteration = list(itertools.combinations(available_data, i))
        # print(data_from_iteration)
        all_data += data_from_iteration
    return all_data

l = create_finite_amount_of_data(8,19,[1,2,3,4,5],2)
print(len(l))
# for d in l:
#     print("zestaw")
#     print(d)

with open('dataX2.txt', 'a') as the_file:
    for d in l:
        # print("zestaw")
        # print(d)
        the_file.write(str(d))
        the_file.write("\n")