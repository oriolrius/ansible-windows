#!/usr/bin/env python

import winrm

ps_script = open('scripts/mem.ps1','r').read()
s = winrm.Session('10.2.0.42', auth=('the_username', 'the_password'))
r = s.run_ps(ps_script)
print r.status_code
print r.std_out
print r.std_err
