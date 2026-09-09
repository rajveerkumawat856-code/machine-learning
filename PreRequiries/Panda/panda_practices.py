import pandas as pd
import numpy as np

# l=[78,85,90,66,72]
# l=pd.Series(l)
# print(l)
# print(l.values)
# print(l.index)
# print(l.dtype)
# print(l[0])
# print(l.tail(2))

# # question 2

# l=[78,85,90,66,72]
# l=pd.Series(l)
# print(l+5)
# print(l-2)
# print(l*1.05)
# print(l/2)

sales={
    'day':['mon','tue','wed','thu','fri'],
    'rev':[1200,1500,900,2000,1800]
}

sales=pd.DataFrame(sales)
sales=sales.set_index('day')
# print(sales)
# print(sales.sum())
# print(sales.mean())
# print(sales['rev'].idxmax())
# print(sales[(sales['rev']>sales['rev'].mean())])

print(sales.plot(kind='pie'))





