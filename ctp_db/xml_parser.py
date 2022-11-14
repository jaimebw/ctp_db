from pathlib import Path
from collections import defaultdict
import pandas as pd
from .table_structure import *
import xmltodict
from xml.parsers.expat import ExpatError
from typing import Dict, DefaultDict


def get_terms(val) -> str:
    """
    This function takes a string and returns a list of the terms in the string
    """
    if isinstance(val, list):
        return ";".join(val)
    else:
        return val


def defaultify(d: Dict):
    """
    This function takes a dictionary and returns a defaultdict with the same
    values. Works recursively

    Parameters
    ----------
    d : dict

    """
    if not isinstance(d, dict):
        return d
    return defaultdict(lambda: None, {k: defaultify(v) for k, v in d.items()})


def extract_xml(path_to_xml: Path):
    """
    This function takes a path to an xml file and returns a dictionary with the
    relevant information for the database

    Parameters
    ----------
    path_to_xml : str

    """
    with open(path_to_xml) as f:
        doc = xmltodict.parse(f.read())
    return defaultify(doc)


def migrate_to_sql(input_dict: dict) -> None:
    pass


def acces_info_list(val):
    if isinstance(val, list):
        return val[0]
    else:
        return val

def get_drug_info(parsed_dict):
    """
    WIP!!
    This function takes the parsed dictionary of the xml file and returns a
    dictionary with the drug information

    Parameters
    ----------
    parsed_dict : dict
        The dictionary that is returned from the extract_xml function

    """
    parsed_dict = parsed_dict["clinical_study"]
    drug_info = parsed_dict["intervention"]
    if isinstance(drug_info, list):
        drug_info = drug_info[0]
    drug_dict = {
        "nct_id": parsed_dict["id_info"]["nct_id"],
        "intervention_type": drug_info["intervention_type"],
        "intervention_name": drug_info["intervention_name"],
    }
    #elif isinstance(drug_info, ):
    pass
    #return drug_dict


def main_schema_dict(parsed_dict: Dict[str,str]) -> Dict[str,str]:
    """
    This function takes the parsed dictionary of the xml file and returns a
    dictionary with the main schema information

    Parameters
    ----------
    parsed_dict : dict
        The dictionary that is returned from the extract_xml function

    Schema can be found at https://docs.google.com/spreadsheets/d/1nDoMNKbCGw4hKuMX2n5Y4rdsm1TOKV8a3MhVNeBKRBA/edit#gid=0
    """
    parsed_dict = parsed_dict["clinical_study"]
    
    main_schema_dict = {
        "nct_id": parsed_dict["id_info"]["nct_id"],
        "org_study_id": parsed_dict["id_info"]["org_study_id"],
        "brief_title": parsed_dict["brief_title"],
        "official_title": parsed_dict["official_title"],
        "overall_status": parsed_dict["overall_status"],
        "study_type" : parsed_dict["study_type"],
        "source": parsed_dict["source"],
        "phase": parsed_dict["phase"],
        "start_date": parsed_dict["start_date"],
        "condition": get_terms(parsed_dict["condition"])
    }
    try:
        main_schema_dict["brief_summary"] = parsed_dict["brief_summary"]["textblock"] # some files don't have this
    except TypeError:
        main_schema_dict["brief_summary"] = None
       
    try:
        main_schema_dict["detail_description"]= parsed_dict["detailed_description"]["textblock"]
    except TypeError:
         main_schema_dict["detail_description"]= None

    return main_schema_dict    