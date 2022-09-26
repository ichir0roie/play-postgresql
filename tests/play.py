from scripts.play_manager import *


engine = create_engine("postgresql://user:password@localhost:15432/postgres")

session = Session(engine)

import string
import random


def get_random_char():
    return random.choice(string.ascii_letters)


for i in range(1000):
    print("loop {}".format(str(i)))
    data_1 = []
    data_2 = []
    for j in range(1000):
        data_1.append(Table1(column1=get_random_char(), column2=get_random_char(), column3=get_random_char()))
        data_2.append(Table2(column1=get_random_char(), column2=get_random_char(), column3=get_random_char()))
    session.add_all(data_1)
    session.add_all(data_2)
    session.commit()

res = session.query(Table1)
print(res)
