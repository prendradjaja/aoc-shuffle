import json
from types import SimpleNamespace as obj
import random

from chain import *

YEARS = range(2015, 2021+1)

print('const urls = [');
(
  YEARS
  | map_(lambda year:
    json.load(open(f'./data/{year}.json'))
      |
        map_(lambda x:
          (
            int(x.split()[1].rstrip(',')),
            2 if 'two' in x else 1 if 'one' in x else 0
          )
        )
      | filter_(lambda x: x[1] < 2)
      | map_(lambda x: obj(year=year, day=x[0]))
  )
  | flat()
  | map_(lambda x: f'  "https://adventofcode.com/{x.year}/day/{x.day}",')
  | map_(print)
)
print('];');
