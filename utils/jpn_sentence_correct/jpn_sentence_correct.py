# -*- coding: utf-8 -*-
import json
import time

before = [{"w": "\u8eca", "s": "\u304f\u308b\u307e\u306f\u3042\u306e\u3070\u3059"}, {"w": "\u306f\u3042\u306e\u30d0\u30b9", "s": ""}, {"w": "\u505c", "s": "\u3066\u3044"}, {"w": "\u306e\u305d\u3070\u306b\u3068\u3081\u3066\u304f\u3060\u3055\u3044\u3002", "s": ""}]

wrongStr = "くるまはあのばす"
rightStr = "くるま"

for idx, itm in enumerate(before):
    print(itm['s'])
    if wrongStr == itm['s']:
        before[idx]['s'] = rightStr

print(json.dumps(before))
print()