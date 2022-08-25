import os
import sys
import pandas as pd

def process_input_csv(filepath):
    dataframes = []
    for file in os.listdir(filepath):
        if str(file).endswith('csv'):
            if not str(file).lower().startswith('combined'):
                environment = ''
                if str(file).lower().startswith('na'):
                    environment = 'NA Prod'
                elif str(file).lower().startswith('asia'):
                    environment = 'Asia Prod'
                df = pd.read_csv(os.path.join(filepath, file), usecols=['Source IP'])
                df['Environment'] = environment
                dataframes.append(df)
    data_concated = pd.concat(dataframes, axis=0)
    data_concated = data_concated.reset_index()
    data_concated = data_concated.drop(['index'], axis=1)
    data_concated = data_concated.drop_duplicates()
    data_concated.to_csv(os.path.join(filepath, 'combined.csv'),index=False)

if __name__  == '__main__':
    if len(sys.argv)==1:
        raise Exception("Please provide the filepath to read the input files")
    filepath = sys.argv[1]
    print(filepath)
    if not os.path.exists(filepath):
        raise Exception("The specified directory doesnot exists")
    process_input_csv(filepath)

