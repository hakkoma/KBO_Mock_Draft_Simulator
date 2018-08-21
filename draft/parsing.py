import pandas as pd
import sys



'hitter_draft.csv' = sys.argv[1]
'hitter_real.csv' = sys.argv[2]



data_frame = pd.read_csv('hitter_draft.csv')

data_frame_value_meets_condition = data_frame.loc[(data_frame['학교'].str.contains('대학교'))]
data_frame_value_meets_condition.to_csv('hitter_real.csv', index=False)
