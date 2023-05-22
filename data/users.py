import dataclasses
from datetime import date


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile: str
    year: date
    month: str
    day: date
    subjects: str
    hobbies: str
    picture: str
    address: str
    state: str
    city: str


student = User(
     first_name='Olga',
     last_name='YA',
     email='name@example.com',
     gender='Female',
     mobile='8922569476',
     year='1999',
     month='May',
     day='11',
     subjects='Computer Science',
     hobbies='Reading',
     picture='tests.jpg',
     address='Moscowskaya Street 18',
     state='Haryana',
     city='Karnal'
)
