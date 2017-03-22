#!/usr/bin/env python3

import yaml
from glob import glob
import os
import datetime

GUARD='---\n'

def read_front_matter(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        if lines.count(GUARD) != 2 or lines.index(GUARD) != 0:
            raise Exception('Bad front matter: {}'.format(f))
        end = lines.index(GUARD, 1)
        return (lines[0:end], lines[end:])


def move_slugs(src_dir, src_ext, dst_dir, dst_ext):
    for file in glob(os.path.join(src_dir, '*.' + src_ext)):
        new_file = file.replace(src_dir, dst_dir).replace('.' + src_ext, '.' + dst_ext)
        if not os.path.exists(new_file):
            print('SKIP: {}'.format(file))
            continue

        print('PROC: {}'.format(file))

        y, t = read_front_matter(file)
        y = yaml.load(''.join(y))
        slug = y['slug']

        y, t = read_front_matter(new_file)
        y = yaml.load(''.join(y))

        u = {}
        u['permalink'] = slug + '.' + dst_ext
        u['short'] = y['meta']['dop_for_post_anonse']
        for k in ['published', 'layout', 'title', 'date']:
            u[k] = y[k]

        with open(new_file, 'w') as f:
            yaml.dump(u, f, default_flow_style=False, indent=4, explicit_start=True)
            f.writelines(t)


move_slugs("site1/_posts", "markdown", "site2/_posts", "html")
