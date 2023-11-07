import os

PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
RESOURCES_PATH = os.path.join(PROJECT_ROOT_PATH, 'resources')
TMP_PATH = os.path.join(PROJECT_ROOT_PATH, 'tmp')
ARCHIVE_PATH = os.path.join(TMP_PATH, 'new_archive.zip')

TXT_FILE = 'file_txt.txt'
PDF_FILE = 'Python Testing with Pytest (Brian Okken).pdf'
XLS_FILE = 'file_example_XLS_10.xls'
XLSX_FILE = 'file_example_XLSX_50.xlsx'