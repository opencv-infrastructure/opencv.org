#!/usr/bin/env python3

import yaml
from glob import glob


books = []
cats = set()
for file in glob('_posts/*.html'):
    # print('---- {} -----'.format(file))
    with open(file, 'r') as f:
        data = yaml.load_all(f)
        y = next(data)
        m = y['meta']
        cats.update(set(y['categories']))

        b = None

        if 'Books' in y['categories']:
            b = { 'type': 'english', }
        elif 'Non-english books' in y['categories']:
            b = { 'type': 'other', }
        elif 'Video courses' in y['categories']:
            b = { 'type': 'video', }
        elif 'Boook that mention OpenCV' in y['categories']:
            b = { 'type': 'mention', }
        else:
            pass

        if b:
            b.update({
                'title': y.get('title'),
                'link': m.get('link_to_the_book') or m.get('packt_link_to_the_book') or m.get('amazon_link_to_the_page'),
                'date': m.get('date_for_the_book'),
                'image': m.get('image_for_the_book'),
                'description': next(data),
            })
            books.append(b)
            print(file)

# with open('_data/books.yml', 'w') as file:
#     yaml.dump(books, file, default_flow_style=False, indent=4, explicit_start=True)

# for b in books:
#     print(b['image'])
# print(cats)
