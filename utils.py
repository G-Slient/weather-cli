import configparser

def read_config(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    return config


def kelvin_to_celsius(kelvin):
    celsius = round((kelvin - 273.15),2)
    return celsius