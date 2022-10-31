from ctp_db.xml_parser import *
from pathlib import Path
from pprint import PrettyPrinter
pp = PrettyPrinter(indent=2)
import pytest
from collections import defaultdict

test_xml = Path("/Users/jaime/repos/ctp/archive/NCT0000xxxx/NCT00000102.xml")
def test_parse():
    dict0 = extract_xml(test_xml)

    df = structured_dict(dict0)
    pp.pprint(df)

def is_unqiue(val,arr):
    # returns True if the val in arr is unique
    return arr.count(val) == 1
    

    