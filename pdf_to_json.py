#!/usr/bin/env python3

import os
import shutil
import camelot.io

shutil.rmtree('tmp', ignore_errors=True)
os.mkdir('tmp')

i = 1
while True:
    print('Converting page ' + str(i))
    tables = camelot.io.read_pdf('input/data.pdf', pages=str(i))
    tables.export('tmp/data' + str(i) + '.json', f='json')
    i += 1
