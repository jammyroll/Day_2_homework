users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
twitter_name = users["Jonathan"]['twitter']
print(twitter_name)
# 2. Get Erik's hometown
home_sweet_home = users["Erik"]['home_town']
print(home_sweet_home)
# 3. Get the list of Erik's lottery numbers

Ericks_lucky_numbers = users["Erik"]['lottery_numbers']
print(Ericks_lucky_numbers)
# 4. Get the species of Avril's pet Monty
Monty_species = users["Avril"]['pets'][0]['species']
print(Monty_species)
# 5. Get the smallest of Erik's lottery numbers
lotto_num = users["Erik"]['lottery_numbers']
smallest_num = 100
for num in lotto_num:
    if num <= smallest_num:
        smallest_num = num

print(smallest_num)
# 6. Return an list of Avril's lottery numbers that are even
even_list = []

lotto_num = users["Avril"]['lottery_numbers']
for i in lotto_num:
    if i%2 == 0:
       even_list.append(i)

print(even_list)



# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
users["Erik"]['lottery_numbers'].append(7)
print(users["Erik"]['lottery_numbers'])
# 8. Change Erik's hometown to Edinburgh
users["Erik"]['home_town'] = 'Edinburgh'
print(users["Erik"]['home_town'])
# 9. Add a pet dog to Erik called "fluffy"
users['Erik']['pets'].append({'name': 'Fluffy', 'species': 'dog'})

# 10. Add another person to the users dictionary
new_user = {"Jamie" : {
    "twitter": "jammyroll",
    "lottery_numbers": [1,2,3,4,5],
    "home_town": "Belfast",
    "pets": [
    {
      "name": "Freyja",
      "species": "cat"
    }
  ]
}
}
users.update(new_user)
