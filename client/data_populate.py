import requests
import random
from time import sleep

endpoint = 'http://127.0.0.1:8000/api/users/create/'

# test user
data = {
        'phone_number': '+91-9999999999',
        'name': 'Test User',
        'email': 'test@user.com',
        'password': 'Testuser@1'
}
res = requests.post(endpoint,json=data)
print('Test user created')

# Client users
country_code = '+91'
phone_numbers = []
names = []
passwords = []
total = 80

for i in range(total):
    names.append(f'Client user: {i+1}')
    passwords.append(f'Clientuser@{i+1}')
    num = country_code + '-' + str(random.randrange(7000000000,9999999999)) + '\n'
    phone_numbers.append(num)
    
for i in range(total):
    data = {
        'phone_number': phone_numbers[i],
        'name': names[i],
        'email': '',
        'password': passwords[i]
    }
    res = requests.post(endpoint,json=data)
    sleep(1)

print('Database Populated')