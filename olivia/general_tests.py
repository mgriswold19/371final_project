import contextlib
import sys
import time
import random
import leader_driver as driver

from pyke import knowledge_engine, krb_traceback, goal


def fc_testall(fc_prove, engine):
    engine.reset()      
    engine.activate('fc_rules') 
    num_items = len(driver.init_persons) - len(driver.eliminated_persons)

    attribute_list = []

    with fc_prove.prove(engine) as gen:
        for vars, plan in gen:
            if vars['status'] not in attribute_list:
                attribute_list.append(vars['status'])

    best_split = ""
    best_entropy = 0
    yes = []

    for attribute in attribute_list:
        observations = 0
        removed_persons = []
        with fc_prove.prove(engine, status=attribute) as gen:
            for vars, plan in gen:
                if vars['person'] not in driver.eliminated_persons:
                    observations += 1
                    removed_persons.append(vars['person'])
        if ((observations/num_items) > best_entropy):
            best_entropy = observations/num_items
            best_split = " a " + str(attribute)
            yes = removed_persons

        no = list(set(driver.init_persons) - set(yes) - set(driver.eliminated_persons))

    return([best_split,best_entropy,yes,no])

def fc_testhair(fc_prove, engine):
    engine.reset()     
    engine.activate('fc_rules')
    num_items = len(driver.init_persons) - len(driver.eliminated_persons)

    best_split = ""
    best_entropy = 0
    yes = []

    observations = 0
    removed_persons = []
    with fc_prove.prove(engine) as gen:
        for vars, plan in gen:
            if vars['person'] not in driver.eliminated_persons:
                observations += 1
                removed_persons.append(vars['person'])

    if ((observations/num_items) > best_entropy):
            best_entropy = (observations/num_items)
            best_split = ' light-haired (grey,white, or blonde)'
            yes = removed_persons

    no = list(set(driver.init_persons) - set(yes) - set(driver.eliminated_persons))

    return([best_split,best_entropy,yes,no])

def fc_testreal(fc_prove, engine):
    engine.reset() 
    engine.activate('fc_rules') 
    num_items = len(driver.init_persons) - len(driver.eliminated_persons)

    best_split = ""
    best_entropy = 0
    yes = []

    observations = 0
    removed_persons = []
    with fc_prove.prove(engine) as gen:
        for vars, plan in gen:
            if vars['person'] not in driver.eliminated_persons:
                observations += 1
                removed_persons.append(vars['person'])

    if ((observations/num_items) > best_entropy):
            best_entropy = (observations/num_items)
            best_split = ' a real person(not a character)'
            yes = removed_persons

    no = list(set(driver.init_persons) - set(yes) - set(driver.eliminated_persons))

    return([best_split,best_entropy,yes,no])

def fc_testgender(fc_prove, engine, gender = 'male'):
    engine.reset()
    engine.activate('fc_rules') 
    num_items = len(driver.init_persons) - len(driver.eliminated_persons)

    attribute_list = []

    with fc_prove.prove(engine) as gen:
        for vars, plan in gen:
            if vars['gender'] not in attribute_list:
                attribute_list.append(vars['gender'])

    best_split = ""
    best_entropy = 0
    yes = []

    for attribute in attribute_list:
        observations = 0
        removed_persons = []
        with fc_prove.prove(engine, gender=attribute) as gen:
            for vars, plan in gen:
                if vars['person'] not in driver.eliminated_persons:
                    observations += 1
                    removed_persons.append(vars['person'])
        if ((observations/num_items) > best_entropy):
            best_entropy = observations/num_items
            best_split = " " + attribute
            yes = removed_persons

        no = list(set(driver.init_persons) - set(yes) - set(driver.eliminated_persons))

    return([best_split,best_entropy,yes,no])

