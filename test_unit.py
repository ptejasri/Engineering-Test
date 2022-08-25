import csv

import pytest
import os

@pytest.fixture
def input_value():
   input = r'C:\Users\tpamarth\PROJECTS'
   return input

def test_directory_exists(input_value):
    assert os.path.exists(input_value)

def test_check_output_file_exists(input_value):
    for file in os.listdir(input_value):
        if str(file).lower().startswith('combined'):
            assert True
def test_input_csv_exists(input_value):
    for file in os.listdir(input_value):
        if str(file).lower().startswith('na') or str(file).lower().startswith('asia'):
            assert True
def test_input_file_content(input_value):
    for file in os.listdir(input_value):
        if str(file).lower().startswith('na') or str(file).lower().startswith('asia') :
            with open(os.path.join(input_value,file)) as f:
                reader=csv.reader(f)
                headers=next(reader)
                if 'Source IP' in headers:
                    assert True


def test_output_csv_headers(input_value):
    for file in os.listdir(input_value):
        if str(file).lower().startswith('combined'):
            with open(os.path.join(input_value,'combined.csv')) as f:
                reader=csv.reader(f)
                headers=next(reader)
                if headers==['Source IP','environment']:
                    assert True

