import sys
import os
from subprocess import call
import json
import argparse

# source file
source_file = "/tmp/money.json"

#global dictionary to maintain all the budgets

money = json.load(open(source_file)) # category number to {where:expense}
categories = {} # category to number mapping


def print_categories():
    for key, value in categories:
        print "%s : %s \t"%(key, value)


def add():
    sys.stdout.write("\n")
    amount = str(raw_input("Amount: "))
    sys.stdout.write("\nPlease select the category: ")
    print_categories()
    
    
    

