# import matplotlib.pyplot as plt
# import numpy as np

# x=[1,2,3,4,5]
# y=[6,7,8,9,0]

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Group 1': [10, 20, 15],
    'Group 2': [12, 18, 17]
}
df = pd.DataFrame(data, index=['A', 'B', 'C'])

# Automatically plots parallel bars
df.plot(kind='bar')
plt.title('Parallel Bars via Pandas')
plt.show()
