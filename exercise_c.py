united_kingdom = [
  {
    "name": "Scotland",
    "population": 5295000,
    "capital": "Edinburgh"
  },
  {
    "name": "Wales",
    "population": 3063000,
    "capital": "Swansea"
  },
  {
    "name": "England",
    "population": 5301000,
    "capital": "London"
  }
]

# 1. Change the capital of Wales from `"Swansea"` to `"Cardiff"`.
united_kingdom[1]['capital'] = 'Cardiff'
print(united_kingdom[1])
# 2. Create a dictionary for Northern Ireland and add it to the 
# `united_kingdom` list (The capital is Belfast, and the population 
# is 1,811,000).
NI={
    "name": "Northern Ireland",
    "population": 1811000,
    "capital": "Belfast"
  }
united_kingdom.append(NI)
print(united_kingdom)
print(len(united_kingdom))

# 3. Use a loop to print the names of all the countries in the UK.
N_countries = list(range(0,len(united_kingdom)))
print(N_countries)
for country in N_countries:
    print(united_kingdom[country-1]['name'])
# 4. Use a loop to find the total population of the UK.
counter = 0
for country in N_countries:
    counter = counter + int(united_kingdom[country]['population'])
print(counter)