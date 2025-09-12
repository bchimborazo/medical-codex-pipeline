import pandas as pd
def save_to_csv(data, filename):
	data.to_csv(filename, index=False)