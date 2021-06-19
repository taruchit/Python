# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 17:30:50 2021

@author: pc
"""

import urllib.request # instead of urllib2 like in Python 2.7

def main():
  # Open a connection to a URL using urllib2
  webUrl = urllib.request.urlopen("http://www.google.com")
  
  # Get the result code and print it
  print ("result code: " + str(webUrl.getcode()))
  
  # Reading HTML code from the web
  data = webUrl.read()
  print(data)
  
if __name__ == "__main__":
    main()