# -*- coding: utf-8 -*-
__author__ = 'Ernado'
import re
test_string = u'Мистер неопределённость.rar'
pattern = re.compile('^.*\.(?i)(rar|doc)$')
if re.match(pattern, test_string):
    print 'True'
else:
    print 'False'

