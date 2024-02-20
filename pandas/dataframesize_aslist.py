import pandas as pd

# Shape of dataframe as list
def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape) 

# Get first 3 rows
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)

# Return name and age of a particular student
import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students[students.student_id == 101][['name', 'age']]
    
