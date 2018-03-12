# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('', '', 'fc_rules.krb'):
           [1520645481.0331001, 'fc_rules_fc.py'],
         ('', '', 'famous.kfb'):
           [1520645481.071423, 'famous.fbc'],
        },
        compiler_version)

