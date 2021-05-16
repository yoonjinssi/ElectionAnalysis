# counties_dict={"Arapahoe":422829, "Denver":463353, "Jefferson":432438}
# for county, voters in counties_dict.items():
#     print(f'{county} county has {voters:,} voters.')




# for popcorn in counties_dict.items():
#     print(f'{popcorn}')

voting_data=[{"county":"Arapahoe", "registered_voters":422829},
             {"county":"Denver","registered_voters":463353},
             {"county":"Jefferson", "registered_voters":432438}]
for i in voting_data:
    for keys, values in i.items():
        print(keys, values)

# for county, voters in voting_data:
#     print(f'{county} has {voters:,} voters')