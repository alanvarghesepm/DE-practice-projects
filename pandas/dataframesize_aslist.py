import pandas as pd

# Shape of dataframe as list
def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape) 

# Get first 3 rows
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)

# Return name and age of a particular student
def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students[students.student_id == 101][['name', 'age']]
    
# A company plans to provide its employees with a bonus.
# Write a solution to create a new column name bonus that contains the doubled values of the salary column.
# DataFrame employees
# +-------------+--------+
# | Column Name | Type.  |
# +-------------+--------+
# | name        | object |
# | salary      | int.   |
# +-------------+--------+
def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees.loc[:,'bonus'] = 2*employees.loc[:,'salary']
    return employees
    
