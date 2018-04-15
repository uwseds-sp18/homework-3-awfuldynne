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
        raise ValueError('file_path does not exist')
    conn = sqlite3.connect(file_path)
    df = pd.read_sql(sql_statement, conn)
    return df

