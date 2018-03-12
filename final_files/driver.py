import contextlib as contextlib
import sys as sys
import time as time
import random as random

from pyke import knowledge_engine, krb_traceback, goal

#!!!!! USE PYTHON 3 #!!!!!

engine = knowledge_engine.engine(__file__)

fc_init = goal.compile('famous.knownFor($person, $status)')
fc_rules = goal.compile('famous.rules($person, $nation)')
fc_real = goal.compile('famous.real($person)')
fc_lighthair = goal.compile('famous.lighthair($person, $haircolor)')
fc_gender = goal.compile('famous.gender($person, $gender)')
fc_title = goal.compile('famous.title($person, $title)')
fc_dictator = goal.compile('famous.dictator($person)')
fc_allies = goal.compile('famous.friendly_with($person, $nation)')
fc_skill = goal.compile('famous.famousFor($person, $skill)')
fc_children = goal.compile('famous.children($person)')
fc_race = goal.compile('famous.race($person, $race)')
fc_disney = goal.compile('famous.disney($person)')
fc_princess = goal.compile('famous.princess($person)')
fc_comic = goal.compile('famous.comics($person)')
fc_villain = goal.compile('famous.villain($person)')
fc_lightsaber = goal.compile('famous.lightsaber($person)')

eliminated_persons = []
init_persons = []

import all_tests as all_tests
import general_tests as gen_tests
import character_tests as char_tests
import celeb_tests 
import world_leader_tests as leader_tests

def kb_init():
    curr_list = []
    engine.reset()    
    engine.activate('fc_rules')
    with fc_init.prove(engine) as gen:
        for vars, plan in gen: 
            # print(vars['person'])
            curr_list.append(vars['person'])
    global init_persons
    init_persons = curr_list
    print()
    print()
    print("The possible persons are:")
    print(init_persons)
    print()
    print()


def split():
    attrlit = [gen_tests.fc_testall(fc_init, engine), gen_tests.fc_testhair(fc_lighthair, engine), gen_tests.fc_testreal(fc_real, engine), gen_tests.fc_testgender(fc_gender, engine), 
                char_tests.fc_testdisney(fc_disney, engine), char_tests.fc_testprincess(fc_princess, engine), char_tests.fc_testvillain(fc_villain, engine), char_tests.fc_testlightsaber(fc_lightsaber, engine), 
                char_tests.fc_testcomics(fc_comic, engine), celeb_tests.fc_testskill(fc_skill, engine), celeb_tests.fc_testchildren(fc_children, engine), celeb_tests.fc_testrace(fc_race, engine), 
                leader_tests.fc_testtitle(fc_title, engine), leader_tests.fc_testdictator(fc_dictator, engine), leader_tests.fc_testnation(fc_rules, engine), leader_tests.fc_testallies(fc_allies, engine)]

    curr_best_entropy = 0
    idx = 0

    for index, item in enumerate(attrlit):
        entropy = 1 - abs(item[1]-.5)
        if entropy > curr_best_entropy:
            curr_best_entropy = entropy
            idx = index
        elif entropy == curr_best_entropy:
            if random.random() < .5:
                curr_best_entropy = entropy
                idx = index

    user_answer = input("Is this person" + attrlit[idx][0] + " ? (Yes/No) ")

    if user_answer.lower() == "yes":
        # uncomment the below to see how the system makes decesions
        # print("eliminated_persons")
        # print(attrlit[idx][3])
        # print("leftover")
        # print(attrlit[idx][2])
        eliminated_persons.extend(attrlit[idx][3])
    else:
        # uncomment the below to see how the system makes decesions
        # print("eliminated_persons")
        # print(attrlit[idx][2])
        # print("leftover")
        # print(attrlit[idx][3])
        eliminated_persons.extend(attrlit[idx][2])

    if len(init_persons) - len(eliminated_persons) == 1:
        guessed_person = list(set(init_persons) - set(eliminated_persons))
        print("The person you are thinking of is " + str(guessed_person[0]))
    else:
        split()

    
kb_init()
split()
sys.exit()
