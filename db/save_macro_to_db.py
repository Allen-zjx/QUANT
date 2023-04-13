import sys

sys.path.append("utils")
from data_utils import read_data
from db_config import engine
from db_utils import DB
import warnings

warnings.filterwarnings('ignore')
import os
import pandas as pd

db = DB(engine)
floder = r"D:\QUANT\ZYKJ\Crawler"

floder_list = os.listdir(floder)
for filename in floder_list:
    if "Background" in filename:
        marco_dir = os.path.join(floder, filename)
        macro_list = os.listdir(marco_dir)
        for macro in macro_list:
            macro_path = os.path.join(marco_dir, macro)
            macro_df: pd.DataFrame = read_data(macro_path)
            macro_df['datetime'] = pd.to_datetime(macro_df['datetime'])
            macro_df.sort_values(by='datetime', ascending=True, inplace=True)
            db.save_df_to_db(macro_df, macro[:-4])
