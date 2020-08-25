import time
import random

def type_like_a_person(sentence, input):
    for letter in sentence:
        input.send_keys(letter)
        time.sleep(random.randint(1, 5) / 30)