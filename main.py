#!/usr/bin/env python3

from os import environ, path
from weight import Weight
from datetime import date
from TerminalGameTools import give_options
from matplotlib import pyplot as plt
import numpy as np
import colorama
import pickle

def get_date() -> date:
    '''Prompt user for date'''
    while True:
        response = input('Please enter the date you want to use (yyyy-mm-dd or \'today\'): ')
        try:
            if response.lower() == 'today':
                return date.today()
            return date.fromisoformat(response)
        except ValueError:
            print(f'Invalid value passed \'{response}\'')

def get_weight() -> Weight:
    '''Prompt user for weight'''
    while True:
        response = input('Please enter a weight in lbs: ')
        try:
            return Weight(lbs = float(response))
        except ValueError:
            print(f'Invalid value passed \'{response}\'')

class WeightTracker:
    def __init__(self, filename: str):
        self.filename = filename
        if path.isfile(self.filename):
            with open(self.filename, 'rb') as f:
                self.data = pickle.load(f)
        else:
            self.data = {}

    def save(self):
        '''Save data to filename'''
        with open(self.filename, 'wb') as f:
            pickle.dump(self.data, f)

    def new_entry(self):
        '''Create a new Entry'''
        d = get_date()
        self.data[d] = get_weight()
        self.save()

    def show_graph(self):
        '''Show the graph of entries'''
        data = list(sorted(self.data.items(), key = lambda t: t[0]))
        dates = [date for date, _ in data]
        weights = [weight.lbs for _, weight in data]
        plt.plot(dates, weights)
        plt.xlabel('Date')
        plt.ylabel('Weight')
        plt.title('Weight')
        plt.xticks(rotation = 25)
        plt.show()
        # TODO somehow fix bug where plot cannot close

    def run(self):
        '''Start the WeightTracker application'''
        while True:
            match give_options(['New Entry', 'Show Graph', 'Exit'])[0]:
                case 0: self.new_entry()
                case 1: self.show_graph(); return
                case 2: return

def main():
    '''Driver Code'''
    colorama.init()
    WeightTracker(environ.get('WEIGHT_TRACKER_PATH', 'weight_data.pickle')).run()

if __name__ == '__main__':
    main()

