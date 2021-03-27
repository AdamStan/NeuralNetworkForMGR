from generating_x_data import prepare_data
import itertools

days = [1,2,3,4,5]
days_combinations = itertools.combinations(days, 3)
all_data = []
for comb in list(days_combinations):
    all_data += prepare_data(max_hour=16, days=list(comb))
    all_data += prepare_data(min_hour=11, days=list(comb))
    break

print(len(all_data))

# TODO: Remove duplicates
