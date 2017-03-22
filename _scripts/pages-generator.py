#!/usr/bin/env python3

import yaml
from glob import glob
from os import remove


res = []

cats = set()
for file in glob('_pages/*.html'):
    # print('---- {} -----'.format(file))
    with open(file, 'r') as f:
        data = yaml.load_all(f)
        y = next(data)
        m = y['meta']
        cats.update(set(y['categories']))

        if m.get('tutorials_link'):
            res.append({
                'title': y.get('title'),
                'date': y.get('date'),
                'short': m.get('tutorials_anonse'),
                'link': m.get('tutorials_link'),
                'comment': m.get('tutorials_comment'),
                'image': m.get('tutorials_image'),
            })
            # print(m.get('tutorials_image'))
            # remove(file)
            # print(file)


# with open('_data/tutorials.yml', 'w') as file:
#     yaml.dump(res, file, default_flow_style=False, indent=4, explicit_start=True)
