import pandas as pd

data = pd.read_csv('/Users/jakewaller/Documents/Flask/app/static/Ltn2_cycletime_multi.txt', sep='\t')

data.to_json('/Users/jakewaller/Documents/Flask/app/static/multisltn2cycle.json')