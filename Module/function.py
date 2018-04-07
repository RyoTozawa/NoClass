#!/usr/bin/env python3
# coding:utf-8
def shape_string(bodys):
    no_class = []
    extra_class = []
    for a in bodys:
        if a.startswith('休講'):
            no_class.append(a)
        elif a.startswith('補講'):
            extra_class.append(a)

    return no_class, extra_class