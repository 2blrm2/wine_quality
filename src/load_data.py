# read data from data source
# save it in data/raw for further steps

import os
from get_data import read_parms,get_data
import argparse

def load_and_save(config_path):
    config = read_parms(config_path)
    df= get_data(config_path)
    new_columns=[x.replace(" ","_") for x in df.columns]
    raw_data_path= config["load_data"]["raw_data_csv"]
    df.to_csv(raw_data_path,header=new_columns,index=False,sep=",")

if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default ="params.yaml")
    parsed_args = args.parse_args()
    load_and_save(config_path = parsed_args.config)