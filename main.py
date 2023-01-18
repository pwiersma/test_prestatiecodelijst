
"""
Module to download Vektis Prestatiecodelijst and upload to netezza / snowflake.

"""

import argparse
import configparser

import pandas as pd


def is_valid_filename():
    pass 


def is_valid_file():
    pass


def download_file():
    """ ."""
    return None  


def convert_xls(filename):
   """ 
   Handles Excel type documents and converts them to a dict
   """
   
   if filename[:3].lower() == 'zip':
       #download file, unzip, add the filename
       pass 
   
   # We're assuming Excel here, I should check prior to this
   # I DO NOT LIKE USING PANDAS!
   # But all alternatives seem a lot more complicated
   df = pd.read_excel(filename)
   return df.to_dict()      # not sure whether this returns something   
   

def find_all_links():
    pass


def read_config(file_location):
    """ Read config from file and return as a config file. """ 
    
    config = configparser.ConfigParser()
    config.read(file_location)
    return config
    

def cli():
    """ Handles argparse for a command line interface. """ 
    
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="URL from which to download Excel file", type=str,
                        default="https://tog.vektis.nl/WebInfo.aspx?ID=Prestatiecodelijsten")
    parser.add_argument("config", help="Location of the config file", type=str,
                        default="CONFIG.ini")
    return parser.parse_args()
    

def main():
    args = cli()
    #config = read_config(args.config)

    file = download_file()


if __name__ == "__main__":
    main()
