###############################################################################
#   Script: db_tasks.py
#   Author: Dennis Barger
#   Date:   2/1/2017
#
#   Purpose:
#   Tasks required to connect, access and load Postgresql database
##############################################################################

##  Script Initialization
from configparser import ConfigParser

#-----------------------------------------------------------------------------#
#   Function:  get_connection_param(config_file='database.ini', section='postgresql')
#
#   Description:
#   Connect to Postgresql database using configuraitons in database.ini file
#
#   Function arguments:
#   config_file = database.ini file with connection configuraitons
#   section = desired configuration file section
#-----------------------------------------------------------------------------#

def get_connection_param(config_file='database.ini', section='postgresql'):
    # Read configuration file
    parser = ConfigParser()
    parser.read(config_file)

    # Get db connection information
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0) not found in the {1} file'.format(section, filename))

    return db

#-----------------------------------------------------------------------------#
#   Function:  insert_records(sql_arg, values_arg)
#
#   Description:
#   Insert multiple records into
#
#   Function arguments:
#   conn_arg = database connection object
#-----------------------------------------------------------------------------#
def close_connection(conn_arg):
    if conn_arg:
        conn_arg.close()



