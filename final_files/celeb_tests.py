import contextlib
import sys
import time
import random
import driver as driver

from pyke import knowledge_engine, krb_traceback, goal

def fc_testskill(fc_prove, engine):
    engine.reset()
    engine.activate('fc_rules')
    num_items = len(driver.init_persons) - len(driver.eliminated_persons)

    attribute_list = []

    with fc_prove.prove(engine) as gen:
        for vars, plan in gen:
            if vars['skill'] not in attribute_list:
                attribute_list.append(vars['skill'])

    best_split = ""
    best_entropy = 0
    yes = []

    for attribute in attribute_list:
        observations = 0
        removed_persons = []
        with fc_prove.prove(engine, skill=attribute) as gen:
            for vars, plan in gen:
                if vars['person'] not in driver.eliminated_persons:
                    observations += 1
                    removed_persons.append(vars['person'])
        if ((observations/num_items) > best_entropy):
            best_entropy = observations/num_items
            best_split = " famous for " + str(attribute)
            yes = removed_persons

        no = list(set(driver.init_persons) - set(yes) - set(driver.eliminated_persons))

    return([best_split,best_entropy,yes,no])

def fc_testchildren(fc_prove, engine):
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
            best_split = ' a parent'
            yes = removed_persons

    no = list(set(driver.init_persons) - set(yes) - set(driver.eliminated_persons))

    return([best_split,best_entropy,yes,no])


def fc_testrace(fc_prove, engine):
    engine.reset()
    engine.activate('fc_rules')
    num_items = len(driver.init_persons) - len(driver.eliminated_persons)

    attribute_list = []

    with fc_prove.prove(engine) as gen:
        for vars, plan in gen:
            if vars['race'] not in attribute_list:
                attribute_list.append(vars['race'])

    best_split = ""
    best_entropy = 0
    yes = []

    for attribute in attribute_list:
        observations = 0
        removed_persons = []
        with fc_prove.prove(engine, race=attribute) as gen:
            for vars, plan in gen:
                if vars['person'] not in driver.eliminated_persons:
                    observations += 1
                    removed_persons.append(vars['person'])
        if ((observations/num_items) > best_entropy):
            best_entropy = observations/num_items
            best_split = " (at least in part) " + str(attribute)
            yes = removed_persons

        no = list(set(driver.init_persons) - set(yes) - set(driver.eliminated_persons))

    return([best_split,best_entropy,yes,no])
