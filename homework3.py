import os
import pandas as pd
import sqlite3


def create_dataframe(file_path):
    """ Creates a Pandas DataFrame with three columns (video_id, category_id, and language
    :param file_path: File path to where the Youtube database is located
    :return: Pandas DataFrame
    """
    sql_statement = \
        "SELECT c.video_id, c.category_id, 'ca' AS language " \
        "FROM CAvideos AS c " \
        "UNION " \
        "SELECT d.video_id, d.category_id, 'de' AS language " \
        "FROM DEvideos AS d " \
        "UNION " \
        "SELECT f.video_id, f.category_id, 'fr' AS language " \
        "FROM FRvideos AS f " \
        "UNION " \
        "SELECT g.video_id, g.category_id, 'gb' AS language " \
        "FROM GBvideos AS g " \
        "UNION " \
        "SELECT u.video_id, u.category_id, 'us' AS language " \
        "FROM USvideos AS u;"
    if not os.path.isfile(file_path):
        raise FileExistsError('file_path does not exist')
    conn = sqlite3.connect(file_path)
    df = pd.read_sql(sql_statement, conn)
    return df


def test_create_dataframe(df):
    """ Validates a Pandas DataFrame to see if the following specifications hold true.
    - The DataFrame contains only the columns video_id, category_id, language.
    - The DataFrame columns video_id and language could be a key
    - There are at least 10 rows in the DataFrame
    :param df: Pandas DataFrame
    :return: Returns True if the DataFrame matches the above specifications
    """
    return_value = True
    column_list = ['video_id', 'category_id', 'language']
    # If df is not a Pandas DataFrame, raise an exception
    if not isinstance(df, pd.DataFrame):
        raise TypeError('df is not a Pandas DataFrame.')
    # Check to see if the DataFrame has 10 or more rows
    if df.shape[0] < 10:
        return_value = False
    # Check to see that the number of columns matches the length of column list
    if len(df.columns) != len(column_list):
        return_value = False
    # Check to see that the only columns are the ones in column_list
    for column_name in df.columns:
        if column_name not in column_list:
            return_value = False
    # Check to see if video_id and language could be a key
    grouped_df = df.groupby(['video_id', 'language']).size()
    if grouped_df[grouped_df > 1].any():
        return_value = False
    return return_value

