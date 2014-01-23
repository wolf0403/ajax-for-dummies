#!/usr/bin/env python

'''By Ryan Gao, 2014 '''

from splinter import Browser 
from sys import argv

url = "http://THE_DEFAULT_URL/{0}"
path = "/THE_DEFAULT_AJAX_AFTER_SHEBANG"

def load_by_firefox(path):             
    with Browser() as browser: 
        # Visit URL 
        path = url.format(path)
        print 'Visiting ', path
        browser.visit(path)
        v = browser.is_element_present_by_css('.topic-statement', wait_time=10)    
        print "Is loaded? " + str(v)
        return browser.evaluate_script("$('html').html()")

if __name__ == "__main__":
    #print argv, len(argv)
    if len(argv) > 1:
        path = argv[1].strip()
        #print "Visiting: ", url.format('/topic/all')
       
