import pandas as pd
from datetime import datetime

datas = pd.read_csv("sphist.csv")
datas['DateTime'] = pd.to_datetime(datas['Date'])

datas.sort_values('DateTime', ascending=True, inplace=False)


```

```
