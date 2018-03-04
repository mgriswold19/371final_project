import contextlib
import sys
import time

from pyke import knowledge_engine, krb_traceback, goal

# Compile and load .krb files in same directory that I'm in (recursively).
engine = knowledge_engine.engine(__file__)

fc_continent = goal.compile('leaders.on_continent($leader, $continent)')

fc_goal2 = goal.compile('leaders.gender($leader, $gender)')

fc_goal3 = goal.compile('leaders.title($leader, $title)')

fc_goal4 = goal.compile('leaders.dictator($leader)')

start_num_items = 12 #need to make this dynamic

eliminated_leaders = []

def fc_contient(continent = 'Europe'):
    '''
    contient
    '''
    engine.reset()      # Allows us to run tests multiple times.
    # print("test1")
    start_time = time.time()
    engine.activate('fc_rules')  # Runs all applicable forward-chaining rules.
    fc_end_time = time.time()
    fc_time = fc_end_time - start_time

    # print("doing proof")
    with fc_continent.prove(engine, continent=continent) as gen:
        for vars, plan in gen:
            print("%s is on the continent %s" % \
                    (vars['leader'], vars['continent']))
    prove_time = time.time() - fc_end_time
    print()
    # print("done")
    engine.print_stats()
    # print("fc time %.2f, %.0f asserts/sec" % \
    #       (fc_time, engine.get_kb('leaders').get_stats()[2] / fc_time))

fc_contient()

def fc_test2(gender = 'male'):
    '''
    gender
    '''
    engine.reset()      # Allows us to run tests multiple times.
    # print("test2")
    start_time = time.time()
    engine.activate('fc_rules')  # Runs all applicable forward-chaining rules.
    num_items = start_num_items - len(eliminated_leaders)

    attribute_list = []

    with fc_goal2.prove(engine) as gen:
        for vars, plan in gen:
            if vars['gender'] not in attribute_list:
                attribute_list.append(vars['gender'])

    best_split = ""
    best_entropy = 0
    final_removed_leaders = []

    # print("doing proof")
    for attribute in attribute_list:
        observations = 0
        removed_leaders = []
        with fc_goal2.prove(engine, gender=attribute) as gen:
            for vars, plan in gen:
                if vars['leader'] not in eliminated_leaders:
                    # print("%s is %s" % \
                    #         (vars['leader'], vars['gender']))
                    observations += 1
                    removed_leaders.append(vars['leader'])
        if ((observations/num_items) > best_entropy):
            best_entropy = observations/num_items
            best_split = attribute
            final_removed_leaders = removed_leaders

    return([best_split,best_entropy,final_removed_leaders])



def fc_test3():
    '''
    title
    '''
    engine.reset()      # Allows us to run tests multiple times.
    # print("Title Attribute:")
    start_time = time.time()
    engine.activate('fc_rules')  # Runs all applicable forward-chaining rules.
    num_items = start_num_items - len(eliminated_leaders)
    attribute_list = []

    with fc_goal3.prove(engine) as gen:
        for vars, plan in gen:
            if vars['title'] not in attribute_list:
                attribute_list.append(vars['title'])

    # print("doing proof")

    best_split = ""
    best_entropy = 0
    final_removed_leaders = []

    for attribute in attribute_list:
        observations = 0
        removed_leaders = []
        with fc_goal3.prove(engine, title=attribute) as gen:
            for vars, plan in gen:
                if vars['leader'] not in eliminated_leaders:
                    # print("%s is called %s" % \
                    #         (vars['leader'], vars['title']))
                    observations += 1
                    removed_leaders.append(vars['leader'])

        if ((observations/num_items) > best_entropy):
            best_entropy = observations/num_items
            best_split = attribute
            final_removed_leaders = removed_leaders

    return([best_split,best_entropy,final_removed_leaders])

   



def fc_test4():
    '''
    dictator
    '''
    engine.reset()      # Allows us to run tests multiple times.
    # print("test4")
    engine.activate('fc_rules')  # Runs all applicable forward-chaining rules.
    num_items = start_num_items - len(eliminated_leaders)

    best_split = ""
    best_entropy = 0
    final_removed_leaders = []

    # print("doing proof")
    observations = 0
    removed_leaders = []
    with fc_goal4.prove(engine) as gen:
        for vars, plan in gen:
            if vars['leader'] not in eliminated_leaders:
                # print("%s is a dictator" % \
                #         (vars['leader']))
                observations += 1
                removed_leaders.append(vars['leader'])

    if ((observations/num_items) > best_entropy):
            best_entropy = (observations/num_items)
            best_split = 'ISA dictator'
            final_removed_leaders = removed_leaders

    return([best_split,best_entropy,final_removed_leaders])

def split():

    attrlit = [fc_test2(),fc_test3(),fc_test4()]
    print(attrlit)

    curr_best_entropy = 0
    idx = 0

    for index, item in enumerate(attrlit):
        entropy = 1 - abs(item[1]-.5)
        if entropy > curr_best_entropy:
            curr_best_entropy = entropy
            idx = index
    print()
    print()
    print("splitting on:")
    print(attrlit[idx])


    eliminated_leaders.extend(attrlit[idx][2])

split()
split()
split()
        
