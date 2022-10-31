import xml.etree.ElementTree as ET
from pathlib import Path
from collections import defaultdict
import pandas as pd
import re
from .table_structure import *


def extract_xml(path_to_xml:Path)->dict:
    """
    Extraction of the XML data from the CTP dataset
    
    This could be done recursevly.
    """
    tree = ET.parse(str(path_to_xml))
    root = tree.getroot()
    dict0 = defaultdict(lambda: None)
    for first in root:
        if not first.text.isspace():
            dict0[first.tag] = first.text
        else:
            dict1 = defaultdict(lambda: None)
            for second in first:
                if not second.text.isspace():
                    dict1[second.tag] = second.text
                else:
                    dict2 = defaultdict(lambda: None)
                    for third in second:
                        dict3 = defaultdict(lambda: None)
                        if not third.text.isspace():
                            dict2[third.tag] = third.text
                        else:
                            for forth in third:
                                dict3[forth.tag] = forth.text
                            dict2[third.tag] = dict3
                    dict1[second.tag] = dict2
            dict0[first.tag] = dict1
    return dict0


def migrate_to_sql(input_dict:dict)->None:

    
    pass

def structured_dict(parsed_dict,dataframe = False):
    final_dict = {
        "org_study_id":parsed_dict["id_info"]["org_study_id"],
        "secondary_id":parsed_dict["id_info"]["secondary_id"],
        "nct_id":parsed_dict["id_info"]["nct_id"],
        "official_title":parsed_dict["official_title"],
        "brief_title":parsed_dict["brief_title"],
        "lead_sponsor":parsed_dict["sponsors"]["lead_sponsor"]["agency"],
        "agency_class":parsed_dict["sponsors"]["lead_sponsor"]["agency_class"],
        "source": parsed_dict["source"],
        "brief_summary":parsed_dict["brief_summary"]["textblock"],
        "detailed_description":parsed_dict["detailed_description"]["textblock"],
        "status": parsed_dict["overall_status"],
        "phase": parsed_dict["phase"],
        "study_type": parsed_dict["study_type"],
        "has_expanded_access":parsed_dict["has_expanded_access"],
        # study desing info
        "invervention_model":parsed_dict["study_design_info"]["intervention_model"], # better as indepndent table?
        "invervention_model":parsed_dict["study_design_info"]["intervention_model"], # same comment
        "condition":parsed_dict["condition"],
        # intervention
        "intervention_type":parsed_dict["intervention"]["intervention_type"],
        "intervention_name":parsed_dict["intervention"]["intervention_name"],
        # # eligibility
        "eligibility_criteria": parsed_dict["eligibility"]["criteria"]["textblock"],
        "gender": parsed_dict["eligibility"]["gender"],
        "minimum_age":parsed_dict["eligibility"]["minimun_age"],
        "maximum_age":parsed_dict["eligibility"]["maximum_age"],
        "healthy_volunteers":parsed_dict["eligibility"]["healthy_volunteers"],
        # location
        "facility":parsed_dict["location"]["facility"]["name"],
        # # I think this shoud be a whole subtable
        # #
        # #
        "country":parsed_dict["location_countries"]["country"],
        "study_first_submitted" : parsed_dict["study_first_submitted"],
        "study_first_submitted_qc" : parsed_dict["study_first_submitted_qc"],# idk if interesting
        "study_first_posted": parsed_dict["study_first_posted"],
        "last_update_submitted": parsed_dict["last_update_submitted"],
        "last_update_submitted_qc": parsed_dict["last_update_submitted_qc"],
        


        #"primary_outcome":parsed_dict["primary_outcome"]["measure"],
        "start_date": parsed_dict["start_date"],
        #"time_frame": parsed_dict["primary_outcome"]["time_frame"],
        #"keyword": parsed_dict["keyword"]
    }
    if dataframe:
        return pd.DataFrame(final_dict,index = [parsed_dict["id_info"]["nct_id"]])
    else:
        return final_dict