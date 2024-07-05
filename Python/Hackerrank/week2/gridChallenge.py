#!/Users/cemakay/Python/.venv/bin/python

import pandas as pd
def gridChallenge(grid):
    df = pd.DataFrame(grid)
    for i in df:
        df.sort_values(by=i)
    return df


grid = [['cba'], ['ade'], ['efg']]

res = gridChallenge(grid)
print(res)