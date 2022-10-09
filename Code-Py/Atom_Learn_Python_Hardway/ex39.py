states = {
    'Tamil Nadu': "TN",
    'Andhra Pradesh': "AP",
    'Uttar Pradesh': "UP",
    'West Bengal': "WB",
    'Madhya Pradesh': "MP"
}

cities = {
    'TN': "Chennai",
    'AP': "Hyderabad",
    'WB': "Kolkatta"
}

cities['UP'] = "Varanasi"
cities['MP'] = "MPcity"

print("-" * 15)

print("TN State has: ", cities["TN"])
print("AP State has: ", cities["AP"])

print("-" * 15)
print("Uttar Pradesh's abbreviation is", states["Uttar Pradesh"])
print("Mathya Pradesh's abbreviation is", states["Madhya Pradesh"])

print("-" * 15)

print("Tamil Nadu has: ", cities[states["Tamil Nadu"]])
print("West Bengal has: ", cities[states["West Bengal"]])

print("-" * 15)
for state, abbreviation in list(states.items()):
    print(f"{state} is abbreviated {abbreviation}")

print("-" * 15)
for abbreviation, city in list(cities.items()):
    print(f"{abbreviation} has the city {city}")

print("-" * 15)
state = states.get("Kashmir")

if not state:
    print("Sorry, no Kashmir")

city = cities.get("KS", "Does not exist")
print(f"The city for the state 'KS' is: {city}")
