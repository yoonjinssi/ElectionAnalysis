counties=["Arapahoe", "Denver", "Jefferson"]
if counties[1]== 'Denver':
    print(counties[1])

temperature = int(input("What is the temperature outside?"))

if temperature>80:
    print("Turn on the AC")
else:
    print("Open the windows")


counties = ["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties")
else:
    print("El Paso is not the list of counties")

for county in counties:
    print(county)
