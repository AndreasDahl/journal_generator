#!/usr/bin/env python
# -*- coding: utf-8 -*-

disesases = {
    'ADHD': ['hyperaktivitet',
             'opmærksomhedsforstyrrelse',
             'impulsivitet',
             'uro i hænderne',  # Uro i hænder
             'uro i fødderne', ],  # Uro i fødder
    'Røde hunde': ['en kropstemperatur på 38 grader',  # temperaturen 38 grader
                   'udslæt i ansigt og nakke',  # makulapapuløse udslæt i ansigt og nakke, spreder sig ned over kroppen
                   'ømhed i lymfeknuderne omkring hoved og hals',  # ømhed i lymfeknuder omkring hoved og hals
                   'ledsmerter'],
    'Hornhindebetændelse': ['smerter i øjnene',  # Smerter i øjne
                            'irritation i øjnene',  # irritation i øjne
                            'rødme i øjne',
                            'lysskyhed'],
    'Bihulebetændelse': ['smerte i sinus',
                         'væske ophobning i sinus',
                         'hovedepine',
                         'smerter, som forværres ved foroverbøjning',  # smerterne forværres ved foroverbøjning
                         'feber'],
    'Hepatitis B': ['feber',
                    'smerter omkring lever',
                    'gullig hud',  # Ikterus, gulfarvning af hud
                    'mørk urin',
                    'HBsAg positiv'],
    'Hypertension. Forhøjet blodtryk': ['træthed',
                                        'hovedpine',
                                        'øget hjerte palpitationer',
                                        'forhøjet blodtryk'],
    'Diabetes type 1': ['øget træthed',
                        'hyppig urinering',  # hyppig urinering, polyuri
                        'lys skindende urin',  # Urin lys skindende
                        'øget tørst',  # polydipsi
                        'vægttab',
                        'mundtørhed'],
    'Diabetes type 2': ['øget træthed',
                        'hyppig urinering',
                        'lys skindende urin',
                        'øget tørst',
                        'mundtørhed',
                        'forhøjet plasma glukose',
                        'forhøjet HbA1c'],
    'graviditet': ['Menostasi',
                   'brystspænding',
                   '(morgen) kvalme',
                   'Positiv gravilitets test',
                   'kvinde >16 år'],
    'Pancreatitis. Akut': ['smerter, ofte lokaliseret centralt i abdomen med udstråling til ryggen',
                           'Smerteintensiteten kan være høj',
                           'kvalme',
                           'opkastninger',
                           'ømhed i abdomen',
                           'svære tilfælde med peritoneal reaktion'],
    # 'Raynauds syndrom': ['Kuldepåvirkning eller stress udløser anfald, hvor fingrene bliver hvide og føles døde',
    #                      'cyanotiske',
    #                      'hyperæmiske'],
    # 'Ventrikulær takykardi. VT': ['Takykardi med frekvens over 120/ min med breddeøgede komplekser',
    #                               'Nogen gange kan ses retrogradt overledte p-takker',
    #                               'Anfald under 30 sekunders varighed betegnes som “non-sustained VT”'],
    'Cancer coli': ['Blødning fra tarmen',
                    'Ændret afføringsmønster >4 uger',
                    'Blødningsanæmi',
                    'Betydelige almensymptomer (særlig vægttab og mavesmerter)',
                    'Ikterus'],
    # 'Astma': ['Recidiverende tilfælde af hvæsende respiration og hoste',
    #           'Stigning i peakflow på mere end 15% efter reversibilitetstest']
}

gender_specific = {
    'M': {
        'prosta kræft': ['Mænd >45 år',
                         'Hæmospermi',
                         'Vandladningsbesvær',
                         'Perianale smerter',
                         'Dyb venøs thromboflebit femoralt',
                         'Lymfødem (genitalier og under- ekstremiteter)',
                         'Knoglesmerter']
            },
    'F': {
        'graviditet': ['menostasi',
                       'brystspænding',
                       '(morgen) kvalme',
                       'positiv graviditets test',
                       'kvinde >16 år'],
    }
}

common = [
    'feber',
    'træthed',
    'sløvhed',
    'manglende appetit',
    'rygsmærter',
    'manglende appetit',
    'hovepine',
    'humørsvinginger',
    'grineflip',
    'svimmelhed',
    'luft i maven',
    'dårlig lugt',
    'dårlig ånde',
    'mørk urin',
    'stakåndethed',
    'forøget puls',
    'forhøjet blodtryk',
    'forhøjet kolesterol',
    'overvægt',
]
