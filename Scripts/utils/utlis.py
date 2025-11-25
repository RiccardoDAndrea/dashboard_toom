import configparser
import pandas as pd
import os

def get_cols_name():
    import configparser

    config = configparser.ConfigParser(interpolation=None)
    config.read("Scripts/utils/cols.conf")

    section_columns = {}

    for section in config.sections():
        cols = [
            c.strip()
            for c in config.get(section, "columns").split(",")
        ]
        section_columns[section] = cols

    return section_columns