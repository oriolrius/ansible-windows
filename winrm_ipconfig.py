#!/usr/bin/env python

import winrm

s = winrm.Session('10.2.0.42', auth=('the_username', 'the_password'))
r = s.run_cmd('ipconfig', ['/all'])
print r.status_code
print r.std_out
print r.std_err
