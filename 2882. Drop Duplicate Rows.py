import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    df_no_duplicates = customers.drop_duplicates(subset=['email'])
    return df_no_duplicates
