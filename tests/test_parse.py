from ctp_db.xml_parser import *
from pathlib import Path
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=2)
import pytest
from collections import defaultdict

test_xml = [
    Path("/Users/jaime/repos/ctp/archive/NCT0000xxxx/NCT00000102.xml"),
    Path("/Users/jaime/repos/ctp/archive/NCT0107xxxx/NCT01077518.xml"),
]


def test_parse():
    for i in test_xml:
        dict0 = extract_xml(i)
        
        main_dict = main_schema_dict(dict0)
        pp.pprint(main_dict)
