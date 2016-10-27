#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

import sentence_lists
from symptoms import disesases, gender_specific, common
from doctor_names import doctors

pattern = """<?xml version="1.0" encoding="UTF-8"?><Content>
<id>%(id)05d</id>
<sex>%(sex)s</sex>
<date>01.01.2000</date>
<txt>%(text)s</txt>
<forfatter>%(author)s</forfatter>
<svardiagnose>%(diagnosis)s</svardiagnose>
<extrasymptom>%(extra)s</extrasymptom>
</Content>"""

genders = ['M', 'F']

ids = range(201, 301)


def determine_content():
    content = {'sex': random.choice(genders)}

    possible_diseases = disesases.copy()
    possible_diseases.update(gender_specific[content['sex']])

    content['diagnosis'] = random.choice(possible_diseases.keys())

    symptom_count = random.randint(2, 4)
    content['symptoms'] = random.sample(possible_diseases[content['diagnosis']], symptom_count)
    content['author'] = random.choice(doctors)

    content['extra_list'] = []
    content['extra'] = ''
    if random.randint(0, 1) == 1:
        extra = random.choice(common)
        if extra not in content['symptoms']:
            content['extra_list'] = [extra]
            content['extra'] = extra

    return content


def structure_document(content):
    content['text'] = sentence_lists.build_text(content['symptoms'] + content['extra_list'])
    return content


if __name__ == '__main__':
    for id in ids:
        content = determine_content()
        structure_document(content)
        content['id'] = id

        journal = pattern % content

        with open("../data/loeg_%(id)05d.xml" % content, "w") as text_file:
            text_file.write(journal)
