#  Function caching will save function in chache memory -
#  - and if function called again by using chaching -
#  - it will noot take time

import time
from functools import lru_cache
@lru_cache(maxsize=3)
def some_work(n) :
    time.sleep(n)
    return n


print('Running first time')
some_work(3)
print("Running second time")
some_work(3)
print("3rd time")
some_work(3)
# For just calling function again it takes 3 sec extra


