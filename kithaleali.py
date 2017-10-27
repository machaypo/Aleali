__author__ = 'MP'
from faker import Faker
from random import getrandbits
import requests
import time
import random
fake = Faker()

def cook(amt):
     for i in range(1, amt + 1):
        url = 'https://docs.google.com/forms/d/e/1FAIpQLScHyNZjs1yI61FpRSzjfAyZ3jYe4P39qShWRNRM0zz2i99Ulw/formResponse';
        s = requests.session()
        email = 'r23kick+{}@gmail.com'.format(getrandbits(40)); #Edit Your Email Here
        name = fake.name() #Lucy Cechtelar
        phone = fake.phone_number() #XXXXXXXXXX
        stores = "Kith Lafayette" , "Kith Brooklyn"
        store = random.choice(stores) 
        sizes = "Women's 4","Women's 4.5","Women's 5","Women's 5.5","Women's 6","Women's 6.5","Women's 7","7.5","8","8.5","9","9.5","10","10.5",'11','11.5','12','12.5','13'
        size = random.choice(sizes) 
        print size
        print name
        print store
        
        payload = {
            'entry_2111423237': name, #RandomName
            'entry_2648839': email, #Email
            'entry_1712332735': store, #Stores
            'entry_473600588': size, #RandomSize

        }
 
        
        s.post(url, data=payload,);
        print('Created {}/{} Entries'.format(i,amt))
        time.sleep(0)


amt = input('How many entries?  ')
cook(int(amt))
