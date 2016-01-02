#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psutil, datetime

def get_process_list():
    process_list = list()
    for p in psutil.process_iter():
        try:
            process_list.append(
                [
                    p.pid,
                    p.name(),
                    p.status(),
                    p.username(),
                    #p.io_counters(),
                    #p.nice(),
                    #p.children(recursive=True),
                    #p.connections(),
                ]
            )
        except psutil.ZombieProcess:
            continue

    for proc in psutil.process_iter():
        
        if proc.name() == 'soffice.bin':
        	print 'znalazlem!!!!'
        	try:
        		proc.kill()
        		print 'zabito soffice.bin'
        		
        	except:
        		print 'nie zabito'        
        		continue
        		
    return process_list

if __name__ == "__main__":
	get_process_list()
