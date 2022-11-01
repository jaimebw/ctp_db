from sqlmodel import Field, Session, SQLModel, create_engine, select
from pathlib import Path
from ctp_db.table_structure import *
from ctp_db.xml_parser import *


test_xml = [
    Path("/Users/jaime/repos/ctp/archive/NCT0000xxxx/NCT00000102.xml"),
    Path("/Users/jaime/repos/ctp/archive/NCT0107xxxx/NCT01077518.xml"),
]

def test_sql_insert():
    engine = create_engine("sqlite:///testing_database.db")
    SQLModel.metadata.create_all(engine) 
    for i in test_xml:
        dict0 = extract_xml(i)
        CTPdict, STDIdict = structured_dict(dict0)
        add_StudyDesingInfo = StudyDesignInfo(**STDIdict)
        add_CTPgeneral = CTPgeneral(**CTPdict,
                study_desing_info_id=add_StudyDesingInfo.id)

        with Session(engine) as session:
            session.add(add_CTPgeneral)
            session.add(add_StudyDesingInfo)
            session.commit()
            print(f"\n Added {i.stem}")
