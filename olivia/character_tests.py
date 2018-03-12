import contextlib
import sys
import time
import random
import leader_driver as driver

from pyke import knowledge_engine, krb_traceback, goal

def fc_testdisney(fc_prove, engine):
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
            best_split = ' a disney character'
            yes = removed_persons

    no = list(set(driver.init_persons) - set(yes) - set(driver.eliminated_persons))

    return([best_split,best_entropy,yes,no])

def fc_testprincess(fc_prove, engine):
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
            best_split = ' a princess'
            yes = removed_persons

    no = list(set(driver.init_persons) - set(yes) - set(driver.eliminated_persons))

    return([best_split,best_entropy,yes,no])

def fc_testvillain(fc_prove, engine):
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
            best_split = ' a villain'
            yes = removed_persons

    no = list(set(driver.init_persons) - set(yes) - set(driver.eliminated_persons))

    return([best_split,best_entropy,yes,no])

def fc_testcomics(fc_prove, engine):
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
            best_split = ' originally a comic book character'
            yes = removed_persons

    no = list(set(driver.init_persons) - set(yes) - set(driver.eliminated_persons))

    return([best_split,best_entropy,yes,no])

def fc_testlightsaber(fc_prove, engine):
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
            best_split = ' someone who carries a lightsaber'
            yes = removed_persons

    no = list(set(driver.init_persons) - set(yes) - set(driver.eliminated_persons))

    return([best_split,best_entropy,yes,no])
