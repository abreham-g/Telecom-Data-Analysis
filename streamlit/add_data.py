import os
import pandas as pd
import mysql.connector as mysql
from mysql.connector import Error

def DBConnect(dbName=None):
    """

    Parameters
    ----------
    dbName :
        Default value = None)

    Returns
    -------

    """
    conn = mysql.connect(host='localhost',
                         user='root',
                         password="Abrilow@13",
                         database=dbName,
                         auth_plugin='mysql_native_password',
                         buffered=True
                         )
    cur = conn.cursor()
    return conn, cur

def emojiDB(dbName: str) -> None:
    conn, cur = DBConnect(dbName)
    dbQuery = f"ALTER DATABASE {dbName} CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;"
    cur.execute(dbQuery)
    conn.commit()

def createDB(dbName: str) -> None:
    """

    Parameters
    ----------
    dbName :
        str:
    dbName :
        str:
    dbName:str :


    Returns
    -------

    """
    conn, cur = DBConnect()
    cur.execute(f"CREATE DATABASE IF NOT EXISTS {dbName};")
    conn.commit()
    cur.close()

def createTables(dbName: str) -> None:
    """

    Parameters
    ----------
    dbName :
        str:
    dbName :
        str:
    dbName:str :


    Returns
    -------

    """
    conn, cur = DBConnect(dbName)
    sqlFile = 'day5_schema.sql'
    fd = open(sqlFile, 'r')
    readSqlFile = fd.read()
    fd.close()

    sqlCommands = readSqlFile.split(';')

    for command in sqlCommands:
        try:
            res = cur.execute(command)
        except Exception as ex:
            print("Command skipped: ", command)
            print(ex)
    conn.commit()
    cur.close()

    return

def preprocess_df(df: pd.DataFrame) -> pd.DataFrame:
    """

    Parameters
    ----------
    df :
        pd.DataFrame:
    df :
        pd.DataFrame:
    df:pd.DataFrame :


    Returns
    -------

    """
    cols_2_drop = ['Nb of sec with 125000B < Vol DL','Nb of sec with 6250B < Vol UL < 37500B','Nb of sec with 125000B < Vol DL',
                   'TCP UL Retrans. Vol (Bytes)','Nb of sec with 31250B < Vol DL < 125000B','Nb of sec with 6250B < Vol DL < 31250B',
                    'TCP DL Retrans. Vol (Bytes)','HTTP UL (Bytes)']
    
    try:
        df = df.drop(columns=cols_2_drop, axis=1)
        df = df.fillna(0)
    except KeyError as e:
        print("Error:", e)
    try:
        df['Nb of sec with 125000B < Vol DL'] = df['Nb of sec with 125000B < Vol DL'].fillna(0)
        df['Nb of sec with 6250B < Vol UL < 37500B'] = df['Nb of sec with 6250B < Vol UL < 37500B'].fillna('not defined')
        df['HTTP UL (Bytes)'] = df['HTTP UL (Bytes)'].fillna('not defined')
    except KeyError as e:
        print("Error:", e)

    return df


def insert_to_tweet_table(dbName: str, df: pd.DataFrame, table_name: str) -> None:
    """

    Parameters
    ----------
    dbName :
        str:
    df :
        pd.DataFrame:
    table_name :
        str:
    dbName :
        str:
    df :
        pd.DataFrame:
    table_name :
        str:
    dbName:str :

    df:pd.DataFrame :

    table_name:str :


    Returns
    -------

    """
    conn, cur = DBConnect(dbName)

    df = preprocess_df(df)

    for _, row in df.iterrows():
        sqlQuery = f"""INSERT INTO {table_name} (Avg RTT DL (ms) , Avg RTT UL (ms), Last Location Name, MSISDN/Number, Bearer Id, Nb of sec with Vol UL < 1250B,
                    10 Kbps < UL TP < 50 Kbps (%), UL TP > 300 Kbps (%) , 50 Kbps < UL TP < 300 Kbps (%), UL TP < 10 Kbps (%), Nb of sec with Vol DL < 6250B ,
                    250 Kbps < DL TP < 1 Mbps (%), 50 Kbps < DL TP < 250 Kbps (%)  , DL TP < 50 Kbps (%), DL TP > 1 Mbps (%),Handset Type,Handset Manufacturer,IMEI,IMSI,
                    Dur. (ms),Social Media UL (Bytes),Google DL (Bytes),Google UL (Bytes)
                    Email DL (Bytes),Email UL (Bytes),Youtube DL (Bytes),Youtube UL (Bytes),Netflix DL (Bytes),
                    Netflix UL (Bytes),Gaming DL (Bytes),Gaming UL (Bytes),Other DL (Bytes),Other UL (Bytes),Total UL (Bytes),
                    Total DL (Bytes))
             VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,
             %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s);"""
        data = (row[0], row[1], row[2], row[3], (row[4]), (row[5]), row[6], row[7], row[8], row[9], row[10], row[11],
                row[12], row[13], row[14])

        try:
            # Execute the SQL command
            cur.execute(sqlQuery, data)
            # Commit your changes in the database
            conn.commit()
            print("Data Inserted Successfully")
        except Exception as e:
            conn.rollback()
            print("Error: ", e)
    return

def db_execute_fetch(*args, many=False, tablename='', rdf=True, **kwargs) -> pd.DataFrame:
    """

    Parameters
    ----------
    *args :

    many :
         (Default value = False)
    tablename :
         (Default value = '')
    rdf :
         (Default value = True)
    **kwargs :


    Returns
    -------

    """
    connection, cursor1 = DBConnect(**kwargs)
    if many:
        cursor1.executemany(*args)
    else:
        cursor1.execute(*args)

    # get column names
    field_names = [i[0] for i in cursor1.description]

    # get column values
    res = cursor1.fetchall()

    # get row count and show info
    nrow = cursor1.rowcount
    if tablename:
        print(f"{nrow} recrods fetched from {tablename} table")

    cursor1.close()
    connection.close()

    # return result
    if rdf:
        return pd.DataFrame(res, columns=field_names)
    else:
        return res


if __name__ == "__main__":
    createDB(dbName='tellco')
    emojiDB(dbName='tellco')
    createTables(dbName='tellco')

    df = pd.read_csv('../data/clean.csv')
    
    insert_to_tweet_table(dbName='tellco', df=df, table_name='TellcoInformation')
    print(df.isna().sum())
   