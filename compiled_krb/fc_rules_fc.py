# fc_rules_fc.py

from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def rules(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('leaders', 'rules', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if context.lookup_data('nation') == 'Germany':
          engine.assert_('leaders', 'on_continent',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def gender(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('leaders', 'rules', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        notany18_worked = True
        with engine.lookup('leaders', 'gender', context, \
                           rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if context.lookup_data('gender') == 'female':
              notany18_worked = False
            if not notany18_worked: break
        if notany18_worked:
          engine.assert_('leaders', 'gender',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def dictator(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('leaders', 'rules', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        notany27_worked = True
        with engine.lookup('leaders', 'free_elections', context, \
                           rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if context.lookup_data('nation') == context.lookup_data('nation'):
              notany27_worked = False
            if not notany27_worked: break
        if notany27_worked:
          engine.assert_('leaders', 'dictator',
                         (rule.pattern(0).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def freely_elected(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('leaders', 'rules', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('leaders', 'free_elections', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('leaders', 'freely_elected',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def president(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('leaders', 'rules', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        notany43_worked = True
        with engine.lookup('leaders', 'title', context, \
                           rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            notany43_worked = False
            if not notany43_worked: break
        if notany43_worked:
          engine.assert_('leaders', 'title',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def allies(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('leaders', 'allies', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('leaders', 'rules', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('leaders', 'rules', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                engine.assert_('leaders', 'friendly_with',
                               (rule.pattern(0).as_data(context),
                                rule.pattern(1).as_data(context),)),
                engine.assert_('leaders', 'friendly_with',
                               (rule.pattern(2).as_data(context),
                                rule.pattern(3).as_data(context),)),
                rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('fc_rules')
  
  fc_rule.fc_rule('rules', This_rule_base, rules,
    (('leaders', 'rules',
      (contexts.variable('leader'),
       contexts.variable('nation'),),
      False),),
    (contexts.variable('leader'),
     pattern.pattern_literal('Europe'),))
  
  fc_rule.fc_rule('gender', This_rule_base, gender,
    (('leaders', 'rules',
      (contexts.variable('leader'),
       contexts.variable('nation'),),
      False),
     ('leaders', 'gender',
      (contexts.variable('leader'),
       contexts.variable('gender'),),
      True),),
    (contexts.variable('leader'),
     pattern.pattern_literal('male'),))
  
  fc_rule.fc_rule('dictator', This_rule_base, dictator,
    (('leaders', 'rules',
      (contexts.variable('leader'),
       contexts.variable('nation'),),
      False),
     ('leaders', 'free_elections',
      (contexts.variable('nation'),),
      True),),
    (contexts.variable('leader'),))
  
  fc_rule.fc_rule('freely_elected', This_rule_base, freely_elected,
    (('leaders', 'rules',
      (contexts.variable('leader'),
       contexts.variable('nation'),),
      False),
     ('leaders', 'free_elections',
      (contexts.variable('nation'),),
      False),),
    (contexts.variable('leader'),))
  
  fc_rule.fc_rule('president', This_rule_base, president,
    (('leaders', 'rules',
      (contexts.variable('leader'),
       contexts.variable('nation'),),
      False),
     ('leaders', 'title',
      (contexts.variable('leader'),
       contexts.variable('title'),),
      True),),
    (contexts.variable('leader'),
     pattern.pattern_literal('president'),))
  
  fc_rule.fc_rule('allies', This_rule_base, allies,
    (('leaders', 'allies',
      (contexts.variable('nation1'),
       contexts.variable('nation2'),),
      False),
     ('leaders', 'rules',
      (contexts.variable('leader1'),
       contexts.variable('nation1'),),
      False),
     ('leaders', 'rules',
      (contexts.variable('leader2'),
       contexts.variable('nation2'),),
      False),),
    (contexts.variable('leader1'),
     contexts.variable('nation2'),
     contexts.variable('leader2'),
     contexts.variable('nation1'),))


Krb_filename = '../fc_rules.krb'
Krb_lineno_map = (
    ((12, 16), (10, 10)),
    ((17, 17), (11, 11)),
    ((18, 20), (13, 13)),
    ((29, 33), (17, 17)),
    ((35, 38), (19, 19)),
    ((39, 39), (20, 20)),
    ((43, 45), (22, 22)),
    ((54, 58), (26, 26)),
    ((60, 63), (28, 28)),
    ((64, 64), (29, 29)),
    ((68, 69), (31, 31)),
    ((78, 82), (35, 35)),
    ((83, 87), (36, 36)),
    ((88, 89), (38, 38)),
    ((98, 102), (42, 42)),
    ((104, 107), (44, 44)),
    ((111, 113), (46, 46)),
    ((122, 126), (50, 50)),
    ((127, 131), (51, 51)),
    ((132, 136), (52, 52)),
    ((137, 139), (54, 54)),
    ((140, 142), (55, 55)),
)
