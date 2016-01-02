# -*- coding: utf-8 -*-
import datetime

import matplotlib.pyplot as plt

from pprint import pprint
import requests
import json


BASE_URL = u'http://api.fixer.io/{0}'

BASE_CURRENCY = u'PLN'
CURRENCIES = u'EUR,USD'

def gather_data(start_date, tick):

    params = {
            'base': BASE_CURRENCY,
            'symbols': CURRENCIES,
         }

    curr_date = start_date

    today = datetime.date.today()
    data = dict()

    while curr_date <= today:
        url = BASE_URL.format(curr_date)
        res = requests.get(url, params = params)
        res_json =  res.json()
        pprint(res_json)


        for k, v in res_json['rates'].items():          #ogolnie to szukamy USD i EUR
            if k not in data:
                data[k] = {
                        'x': list(),
                        'val': list(),
                        }
            data[k]['x'].append(curr_date)
            data[k]['val'].append(v)

        curr_date += tick
    pprint(data)
    return data


def show_graph(data, rotation = None):
    lines = list()
    for currency, d in data.items():
        lines.append(plt.plot(d['x'], d['val'])[0])     #WTF?

    plt.legend(lines, data.keys(), loc = 'upper rigt', shadow = True)                      #wyswietlanie legendy


    if rotation:
                                              #obracanie napisow pod wykresem
        plt.xticks(rotation = rotation)
    plt.xlabel('time')
    plt.ylabel('val')
    plt.title('wykres')


    plt.show()







data = gather_data(
        start_date = datetime.date(2015, 1, 1),
        tick=datetime.timedelta(days=14),)

show_graph(data, rotation = 45)

