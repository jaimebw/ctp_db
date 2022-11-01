from pathlib import Path
from collections import defaultdict
import pandas as pd
from .table_structure import *
import xmltodict


def get_terms(val) -> str:
    """
    This function takes a string and returns a list of the terms in the string
    """
    if isinstance(val, list):
        return ",".join(val)
    else:
        return val


def defaultify(d: dict) -> defaultdict:
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


def extract_xml(path_to_xml: Path) -> dict:
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


def structured_dict(parsed_dict, dataframe=False):
    """
    Creates the structured dictionary from the parsed dict of the xml file
    that will go into the database

    Parameters
    ----------
    parsed_dict : dict
        The dictionary that is returned from the extract_xml function
    dataframe : bool, optional
        If True, returns a pandas dataframe, by default False

    """
    parsed_dict = parsed_dict["clinical_study"]
    CTPgeneral_dict = {
        "org_study_id": parsed_dict["id_info"]["org_study_id"],
        "secondary_id": parsed_dict["id_info"]["secondary_id"],
        "nct_id": parsed_dict["id_info"]["nct_id"],
        "official_title": parsed_dict["official_title"],
        "brief_title": parsed_dict["brief_title"],
        "lead_sponsor": parsed_dict["sponsors"]["lead_sponsor"]["agency"],
        "agency_class": parsed_dict["sponsors"]["lead_sponsor"]["agency_class"],
        "source": parsed_dict["source"],
        "brief_summary": parsed_dict["brief_summary"]["textblock"],
        "detailed_description": parsed_dict["detailed_description"]["textblock"],
        "status": parsed_dict["overall_status"],
        "phase": parsed_dict["phase"],
        "study_type": parsed_dict["study_type"],
        "has_expanded_access": parsed_dict["has_expanded_access"],
        # study desing info
        # "invervention_model":parsed_dict["study_design_info"]["intervention_model"], # better as indepndent table?
        # "invervention_model":parsed_dict["study_design_info"]["intervention_model"], # same comment
        "condition": parsed_dict["condition"],
        # intervention
        # "intervention_type":parsed_dict["intervention"]["intervention_type"],
        # "intervention_name":parsed_dict["intervention"]["intervention_name"],
        # # eligibility
        "eligibility_criteria": parsed_dict["eligibility"]["criteria"]["textblock"],
        "gender": parsed_dict["eligibility"]["gender"],
        "minimum_age": parsed_dict["eligibility"]["minimun_age"],
        "maximum_age": parsed_dict["eligibility"]["maximum_age"],
        "healthy_volunteers": parsed_dict["eligibility"]["healthy_volunteers"],
        "country": parsed_dict["location_countries"]["country"],
        "study_first_submitted": parsed_dict["study_first_submitted"],
        "study_first_submitted_qc": parsed_dict[
            "study_first_submitted_qc"
        ], 
        "study_first_posted": parsed_dict["study_first_posted"],
        "last_update_submitted": parsed_dict["last_update_submitted"],
        "last_update_submitted_qc": parsed_dict["last_update_submitted_qc"],
        "condition_browse": get_terms(parsed_dict["condition_browse"]["mesh_term"]),
        "intervetion_browse": get_terms(
            parsed_dict["intervention_browse"]["mesh_term"]
        ),
        "start_date": parsed_dict["start_date"],
    }
    StudyDesignInfo_dict = {
        "invervention_model": parsed_dict["study_design_info"]["intervention_model"],
        "masking": parsed_dict["study_design_info"]["masking"],
        "primary_purpose": parsed_dict["study_design_info"]["primary_purpose"],
    
    } 
    if dataframe:
        return pd.DataFrame(CTPgeneral_dict, index=[parsed_dict["id_info"]["nct_id"]])
    else:
        return CTPgeneral_dict,StudyDesignInfo_dict
