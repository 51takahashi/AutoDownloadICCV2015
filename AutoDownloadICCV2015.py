# -*- coding: utf-8 -*-
"""
@author: 51takahashi
"""

import os
import requests

dirname = 'papers'

def name_check(name):
    name = name.replace('?','')
    name = name.replace(':','')
    name = name.replace('*','')
    return name

def main():
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    fp = open('ICCV 2015 Open Access Repository.html','r')
    lines = fp.readlines()
    fp.close()
    cnt = 0
    for line in lines:
        if line.find('<dt class="ptitle">')>-1:
            pdfname = dirname+'/'+name_check(line.split('>')[3].split('<')[0])+'.pdf'
            cnt+=1
        if line[0]=='[':
            print(str(cnt)+':'+pdfname)
            if not os.path.exists(pdfname):
                url = line.split('"')[1]
                r = requests.get(url)
                f = open(pdfname, 'wb')
                f.write(r.content)
                f.close()

if __name__ == '__main__':
    main()        