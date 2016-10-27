#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

severity = ['mild', 'slem', 'udbredt', 'voldsomt']

aplifier = ['stor ', 'lille ', 'gammel ', 'ung ', 'frisk ', 'frejdig ', '', '', '']

adjective = ['stodder', 'klaphat']

frames = ["""%s med %s og ubehag""",
          """%s og har haft %s de sidste to døgn""",
          ]

descriptor = [  # 1 wildcard
    'har %s',
    'har haft %s',
    'klager over %s',
    'lider af %s',
]

bonuses = [  # max 1 wildcard numerator ('to, tre, fire')
    ' i de sidste %(days)s døgn.',
    ' i flere dage.',
    '.',
    ' i omkring %(days)s døgn.',
    ' i op mod fem-seks timers tid.',
    ' i en uges tid.',
    ' i de sidste %(days)s timer.',
    ' i den seneste uge.',
    ' i dagevis.',
]

bonuses_enumerators = ['to', 'tre', 'fire']


def build_bonus():
    return random.choice(bonuses) % {'days': random.choice(bonuses_enumerators)}


def build_text(symptoms):
    text = ''
    new = True
    for symptom in symptoms:
        if new:
            text += 'Patienten '
        else:
            text += ' og '
        text += random.choice(descriptor) % symptom
        if random.randint(0, 1) == 1 or new is False:
            text += build_bonus() + ' '
            new = True
        else:
            new = False

    return text
