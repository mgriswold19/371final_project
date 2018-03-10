import contextlib
import sys
import time
import random
import leader_driver as driver

from pyke import knowledge_engine, krb_traceback, goal

def fc_testtitle(fc_prove, engine):
    engine.reset()      
    engine.activate('fc_rules') 
    num_items = len(driver.init_persons) - len(driver.eliminated_persons)
    attribute_list = []

    with fc_prove.prove(engine) as gen:
        for vars, plan in gen:
            if vars['title'] not in attribute_list:
                attribute_list.append(vars['title'])

    best_split = ""
    best_entropy = 0
    yes = []

    for attribute in attribute_list:
        observations = 0
        removed_persons = []
        with fc_prove.prove(engine, title=attribute) as gen:
            for vars, plan in gen:
                if vars['person'] not in driver.eliminated_persons:
                    observations += 1
                    removed_persons.append(vars['person'])

        if ((observations/num_items) > best_entropy):
            best_entropy = observations/num_items
            best_split = "'s offical title " + str(attribute)
            yes = removed_persons

    no = list(set(driver.init_persons) - set(yes) - set(driver.eliminated_persons))

    return([best_split,best_entropy,yes,no])

   

def fc_testdictator(fc_prove, engine):
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
            best_split = ' a dictator'
            yes = removed_persons

    no = list(set(driver.init_persons) - set(yes) - set(driver.eliminated_persons))

    return([best_split,best_entropy,yes,no])

def fc_testnation(fc_prove, engine):
    engine.reset()      
    engine.activate('fc_rules')  
    num_items = len(driver.init_persons) - len(driver.eliminated_persons)

    attribute_list = []

    with fc_prove.prove(engine) as gen:
        for vars, plan in gen:
            if vars['nation'] not in attribute_list:
                attribute_list.append(vars['nation'])

    best_split = ""
    best_entropy = 0
    yes = []

    for attribute in attribute_list:
        observations = 0
        removed_persons = []
        with fc_prove.prove(engine, nation=attribute) as gen:
            for vars, plan in gen:
                if vars['person'] not in driver.eliminated_persons:
                    observations += 1
                    removed_persons.append(vars['person'])
        if ((observations/num_items) > best_entropy):
            best_entropy = observations/num_items
            best_split = " the ruler/leader of " + str(attribute)
            yes = removed_persons

        no = list(set(driver.init_persons) - set(yes) - set(driver.eliminated_persons))

    return([best_split,best_entropy,yes,no])

def fc_testallies(fc_prove, engine):
    engine.reset()
    engine.activate('fc_rules') 
    num_items = len(driver.init_persons) - len(driver.eliminated_persons)

    attribute_list = []

    with fc_prove.prove(engine) as gen:
        for vars, plan in gen:
            if vars['nation'] not in attribute_list:
                attribute_list.append(vars['nation'])

    best_split = ""
    best_entropy = 0
    yes = []

    for attribute in attribute_list:
        observations = 0
        removed_persons = []
        with fc_prove.prove(engine, nation=attribute) as gen:
            for vars, plan in gen:
                if vars['person'] not in driver.eliminated_persons:
                    observations += 1
                    removed_persons.append(vars['person'])
        if ((observations/num_items) > best_entropy):
            best_entropy = observations/num_items
            best_split = " allies with " + str(attribute)
            yes = removed_persons

        no = list(set(driver.init_persons) - set(yes) - set(driver.eliminated_persons))

    return([best_split,best_entropy,yes,no])
