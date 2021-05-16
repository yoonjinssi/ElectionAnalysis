counties_dict = {"Arapahoe":422829, "Denver":463353, "Jefferson":432438}
for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

# Using dictionary_name[key] format to return the value of a key
for county in counties_dict:
    print(counties_dict[county])

# Using get() method to return the value of a key
for county in counties_dict:
    print(counties_dict.get(county))

# Using items() to print the key-value pair of the dictionary
for county, voters in counties_dict.items():
    print(county, voters)


#Skill Drill 3.2.10
for county,voters in counties_dict.items():
    print(county +" county has "+ str(voters) + " registered voters")

#Get each dictionary in a list of Dictionaries
voting_data=[{"county":"Arapahoe", "registered_voters":422829}, 
                {"county":"Denver","reegistered_voters":463353},
                {"counties":"Jefferson","registered_voters":432438}]
for county_dict in voting_data:
    print(county_dict)


#Get the Values from a List of Dictionaries
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)