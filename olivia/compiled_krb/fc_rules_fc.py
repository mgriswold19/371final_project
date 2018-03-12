# fc_rules_fc.py

from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def gender(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('famous', 'knownFor', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        notany11_worked = True
        with engine.lookup('famous', 'gender', context, \
                           rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if context.lookup_data('gender') == 'female':
              notany11_worked = False
            if not notany11_worked: break
        if notany11_worked:
          engine.assert_('famous', 'gender',
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
             else engine.lookup('famous', 'rules', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        notany20_worked = True
        with engine.lookup('famous', 'free_elections', context, \
                           rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if context.lookup_data('nation') == context.lookup_data('nation'):
              notany20_worked = False
            if not notany20_worked: break
        if notany20_worked:
          engine.assert_('famous', 'dictator',
                         (rule.pattern(0).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def freely_elected(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('famous', 'rules', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('famous', 'free_elections', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('famous', 'freely_elected',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def president(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('famous', 'rules', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        notany36_worked = True
        with engine.lookup('famous', 'title', context, \
                           rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            notany36_worked = False
            if not notany36_worked: break
        if notany36_worked:
          engine.assert_('famous', 'title',
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
             else engine.lookup('famous', 'allies', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('famous', 'rules', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('famous', 'rules', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                engine.assert_('famous', 'friendly_with',
                               (rule.pattern(0).as_data(context),
                                rule.pattern(1).as_data(context),)),
                engine.assert_('famous', 'friendly_with',
                               (rule.pattern(2).as_data(context),
                                rule.pattern(3).as_data(context),)),
                rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def children(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('famous', 'famousFor', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        notany53_worked = True
        with engine.lookup('famous', 'children', context, \
                           rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            notany53_worked = False
            if not notany53_worked: break
        if notany53_worked:
          engine.assert_('famous', 'children',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def race(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('famous', 'famousFor', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        notany61_worked = True
        with engine.lookup('famous', 'race', context, \
                           rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            notany61_worked = False
            if not notany61_worked: break
        if notany61_worked:
          engine.assert_('famous', 'race',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def princess(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('famous', 'princess', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('famous', 'gender',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        engine.assert_('famous', 'disney',
                       (rule.pattern(0).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('fc_rules')
  
  fc_rule.fc_rule('gender', This_rule_base, gender,
    (('famous', 'knownFor',
      (contexts.variable('person'),
       contexts.variable('status'),),
      False),
     ('famous', 'gender',
      (contexts.variable('person'),
       contexts.variable('gender'),),
      True),),
    (contexts.variable('person'),
     pattern.pattern_literal('male'),))
  
  fc_rule.fc_rule('dictator', This_rule_base, dictator,
    (('famous', 'rules',
      (contexts.variable('person'),
       contexts.variable('nation'),),
      False),
     ('famous', 'free_elections',
      (contexts.variable('nation'),),
      True),),
    (contexts.variable('person'),))
  
  fc_rule.fc_rule('freely_elected', This_rule_base, freely_elected,
    (('famous', 'rules',
      (contexts.variable('person'),
       contexts.variable('nation'),),
      False),
     ('famous', 'free_elections',
      (contexts.variable('nation'),),
      False),),
    (contexts.variable('person'),))
  
  fc_rule.fc_rule('president', This_rule_base, president,
    (('famous', 'rules',
      (contexts.variable('person'),
       contexts.variable('nation'),),
      False),
     ('famous', 'title',
      (contexts.variable('person'),
       contexts.variable('title'),),
      True),),
    (contexts.variable('person'),
     pattern.pattern_literal('president'),))
  
  fc_rule.fc_rule('allies', This_rule_base, allies,
    (('famous', 'allies',
      (contexts.variable('nation1'),
       contexts.variable('nation2'),),
      False),
     ('famous', 'rules',
      (contexts.variable('person1'),
       contexts.variable('nation1'),),
      False),
     ('famous', 'rules',
      (contexts.variable('person2'),
       contexts.variable('nation2'),),
      False),),
    (contexts.variable('person1'),
     contexts.variable('nation2'),
     contexts.variable('person2'),
     contexts.variable('nation1'),))
  
  fc_rule.fc_rule('children', This_rule_base, children,
    (('famous', 'famousFor',
      (contexts.variable('person'),
       contexts.variable('skill'),),
      False),
     ('famous', 'children',
      (contexts.variable('person'),
       contexts.variable('yesno'),),
      True),),
    (contexts.variable('person'),
     pattern.pattern_literal('No'),))
  
  fc_rule.fc_rule('race', This_rule_base, race,
    (('famous', 'famousFor',
      (contexts.variable('person'),
       contexts.variable('skill'),),
      False),
     ('famous', 'race',
      (contexts.variable('person'),
       contexts.variable('race'),),
      True),),
    (contexts.variable('person'),
     pattern.pattern_literal('Caucasian'),))
  
  fc_rule.fc_rule('princess', This_rule_base, princess,
    (('famous', 'princess',
      (contexts.variable('person'),),
      False),),
    (contexts.variable('person'),
     pattern.pattern_literal('female'),))


Krb_filename = '../fc_rules.krb'
Krb_lineno_map = (
    ((12, 16), (10, 10)),
    ((18, 21), (12, 12)),
    ((22, 22), (13, 13)),
    ((26, 28), (15, 15)),
    ((37, 41), (19, 19)),
    ((43, 46), (21, 21)),
    ((47, 47), (22, 22)),
    ((51, 52), (24, 24)),
    ((61, 65), (28, 28)),
    ((66, 70), (29, 29)),
    ((71, 72), (31, 31)),
    ((81, 85), (35, 35)),
    ((87, 90), (37, 37)),
    ((94, 96), (39, 39)),
    ((105, 109), (43, 43)),
    ((110, 114), (44, 44)),
    ((115, 119), (45, 45)),
    ((120, 122), (47, 47)),
    ((123, 125), (48, 48)),
    ((134, 138), (52, 52)),
    ((140, 143), (54, 54)),
    ((147, 149), (56, 56)),
    ((158, 162), (60, 60)),
    ((164, 167), (62, 62)),
    ((171, 173), (64, 64)),
    ((182, 186), (68, 68)),
    ((187, 189), (70, 70)),
    ((190, 191), (71, 71)),
)
