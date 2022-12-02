from typing import Optional
from sqlmodel import Field, SQLModel,Relationship

class MainTable(SQLModel,table = True):
    """
    TO-DO: Add drug table to the schema
    This class is the main table of the database. It contains the information
    that is common to all the trials. It is the main table of the database.

    Parameters
    ----------
    nct_id : str
        The unique identifier of the trial
    brief_title : str
        The brief title of the trial
    official_title : str
        The official title of the trial
    org_study_id : str
        The original study identifier of the trial
    
        
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    nct_id: str
    org_study_id: Optional[str] = Field(default=None)
    brief_title: Optional[str] = Field(default=None)
    official_title: Optional[str] = Field(default=None)
    overall_status: Optional[str] = Field(default=None)
    study_type: Optional[str] = Field(default=None)
    source: Optional[str] = Field(default=None)
    phase: Optional[str] = Field(default=None)
    start_date: Optional[str] = Field(default=None)
    conditon: Optional[str] = Field(default=None)
    brief_summary: Optional[str] = Field(default=None)
    detailed_description: Optional[str] = Field(default=None)
    #drug_id: Optional[int] = Field(default=None, foreign_key="drug.id")

    
class DrugTable(SQLModel,table = True):
    # WIP!!!
    """
    This class is the drug table of the database. It contains the information
    about the drugs used in the trials. It is the drug table of the database.

    Parameters
    ----------
    nct_id : str
        The unique identifier of the trial
    drug_name : str
        The name of the drug used in the trial
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    nct_id:  Optional[str] = Field(default=None, foreign_key="maintable.nct_id")
    drug_name: str
    #main_table_id: Optional[int] = Field(default=None, foreign_key="main_table.id")


"""
class CTPgeneral(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    org_study_id: Optional[str] = Field(default=None, max_length=100)
    secondary_id: Optional[str] = Field(default=None, max_length=100)
    nct_id: str
    official_tile: Optional[str] = Field(default=None)
    brief_title: Optional[str] = Field(default=None)
    lead_spnsor: Optional[str] = Field(default=None)
    agency_class: Optional[str] = Field(default=None)
    source: Optional[str] = Field(default=None)
    brief_summary: Optional[str] = Field(default=None)
    detailed_description: Optional[str] = Field(default=None)
    status: Optional[str] = Field(default=None)
    phase: Optional[str] = Field(default=None)
    study_type: Optional[str] = Field(default=None)
    has_expanded_access: Optional[str] = Field(default=None)
    condition: Optional[str] = Field(default=None)
    eligibility_criteria: Optional[str] = Field(default=None)
    gender: Optional[str] = Field(default=None)
    minimum_age: Optional[str] = Field(default=None)
    maximum_age: Optional[str] = Field(default=None)
    healthy_volunteers: Optional[str] = Field(default=None)
    country: Optional[str] = Field(default=None)
    study_first_submitted: Optional[str] = Field(default=None)
    study_first_submitted_qc: Optional[str] = Field(default=None)
    study_first_posted: Optional[str] = Field(default=None)
    last_update_submitted: Optional[str] = Field(default=None)
    last_update_submitted_qc: Optional[str] = Field(default=None)
    condition_browse: Optional[str] = Field(default=None)
    intervention_browse: Optional[str] = Field(default=None)
    start_date: Optional[str] = Field(default=None)

    study_desing_info_id: Optional[int] = Field(default=None, foreign_key="studydesigninfo.id")

    # Add sponsors?
    #source: Optional[str] = Field(default=None)
    #brief_summary: str
    #overall_status: str
    #start_date: str

    #phase: Optional[str] = Field(default=None)
    #study_type: Optional[str] = Field(default=None)
    #has_expanded_access: Optional[str] = Field(default=None)

    # Add overall_official?
    # Add location?

    #eligibility: Optional[int] = Field(default=None, foreign_key="eligibility.id")
    #study_desing_info: Optional[int] = Field(
    #    default=None, foreign_key="study_design_info.id"
    #)
    #primary_outcome: Optional[int] = Field(
    #    default=None, foreign_key="primary_outcome.id"
    #)


class StudyDesignInfo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    allocation: Optional[str] = Field(default=None)
    intervention_model: Optional[str] = Field(default=None)
    intervention_model_description: Optional[str] = Field(default=None)
    primary_purpose: Optional[str] = Field(default=None)
    masking: Optional[str] = Field(default=None)
    observational_model: Optional[str] = Field(default=None)
    time_perspective: Optional[str] = Field(default=None)

class Eligibility(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    study_population: Optional[str] = Field(default=None)
    sampling_method: Optional[str] = Field(default=None)
    criteria: Optional[str] = Field(default=None)
    gender: Optional[str]
    maximum_age: Optional[str] = Field(default=None)
    minimum_age: Optional[str] = Field(default=None)
    healthy_volunteers: Optional[str] = Field(default=None)



# On hold, there are many secondary outcomes fields
# ei: NCT01077518.xml"
class SecondaryOutcome(SQLModel,table = True):
    id: Optional[int] = Field(default=None,primary_key=True)
    measure: Optional[str] = Field(default=None)
    time_frame: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)


class PrimaryOutcome(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    measure: Optional[str] = Field(default=None)
    time_frame: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)


class StudyDesignInfo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    allocation: Optional[str] = Field(default=None)
    intervention_model: Optional[str] = Field(default=None)
    intervention_model_description: Optional[str] = Field(default=None)
    primary_purpose: Optional[str] = Field(default=None)
    masking: Optional[str] = Field(default=None)
    observational_model: Optional[str] = Field(default=None)
    time_perspective: Optional[str] = Field(default=None)
"""