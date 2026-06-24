"""

Exercises for day 5:
https://github.com/Asabeneh/30-Days-Of-Python/blob/master/05_Day_Lists/05_lists.md

"""

# 1

empty_list = []

# 2

list = [1, 2, 3, 4, 5]

# 3 

print(len(list)) # 5

# 4
first_item = list[0]
middle_item = list[2]
last_item = list[len(list) - 1]

# 5

mixed_data_types = ["Leillo", 21, 1.91, "Single", "Av. Parkinson #133A"]

# 6

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7

print(it_companies)

# 8
print(len(it_companies))

# 9
print(it_companies[0], it_companies[3], it_companies[len(it_companies) - 1])

# 10
it_companies[3] = "Nvidia"
print(it_companies)

# 11
it_companies.append("Mediatek")

# 12
it_companies.insert(4, "TSMC")

# 13
it_companies[0] = it_companies[0].upper()
print(it_companies)

# 14

print(("#; ").join(it_companies))

# 15
does_exist = "IBM" in it_companies
print("Does IBM belongs to IT companies?",does_exist) # True

# 16

it_companies.sort()

# 17

it_companies.reverse()

# 18

it_companies = it_companies[3:]

print(it_companies)

# 19

it_companies = it_companies[:-3]
print(it_companies)

# 20
it_companies = it_companies[::2]
print(it_companies)

# 21 
it_companies.remove("Microsoft")

# 22
it_companies.remove("IBM")

# 23 and 24
it_companies.clear()

# 25
del it_companies

# 26

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)

# 27

full_stack = front_end.copy()
full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")

print(full_stack)

# 28 - Level 2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()

min_age = ages[0]
max_age = ages[len(ages) - 1]

median_age = (ages[4] + ages[5]) / 2
average_age = sum(ages) / len(ages)
print(median_age)
print(average_age)

range_ages = max_age - min_age

abs_min_avg = abs(min_age - average_age)
abs_max_avg = abs(max_age - average_age)


countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]

half_countries = round((len(countries) - 1) / 2)

print(countries[half_countries])

half_1_countries = countries[:half_countries + 1]
half_2_countries = countries[half_countries + 1:]
print(len(half_1_countries))
print(len(half_2_countries))

less_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_country, second_country, third_country, *scandic_countries = less_countries

print(scandic_countries)