import csv

import pytest
import os

@pytest.fixture
def input_value():
   input = r'C:\Users\tpamarth\PROJECTS\tumli\Engineering Test Risk Analytics\Engineering Test Files'
   return input

def test_directory_exists(input_value):
    assert os.path.exists(input_value)

def test_check_output_file_exists(input_value):
    for file in os.listdir(input_value):
        if str(file).lower().startswith('combined'):
            assert True

def test_output_csv_headers(input_value):
    for file in os.listdir(input_value):
        if str(file).lower().startswith('combined'):
            with open(os.path.join(input_value,'combined.csv')) as f:
                reader=csv.reader(f)
                headers=next(reader)
                if headers==['Source IP','environment']:
                    assert True

