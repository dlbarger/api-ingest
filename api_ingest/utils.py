###############################################################################
#   Script: utils.py
#   Author: Dennis Barger
#   Date:   12/27/2016
#
#   Purpose:
#   Miscellaneous utility functions including:
#   - write_log()
#   - http_file_download()
#   - unzip_file()
###############################################################################

#-----------------------------------------------------------------------------#
#   Function:  write_log(msg_arg, msg_type_arg)
#
#   Description:
#   Write status or error message to ingestion service log file.
#
#   Function arguments:
#   - msg_arg = detail message
#   - msg_type_arg = STATUS or ERROR
#   - append_flag_arg = 0 = FALSE, 1 = TRUE
#-----------------------------------------------------------------------------#
def write_log(msg_arg, msg_type_arg, append_flag_arg):

    # Initialize packages and local variables
    import datetime
    from pathlib import Path

    log_file = 'ingestion_service_log.txt'

    # Build message to log
    msg_date = datetime.datetime.now()
    msg_date = msg_date.strftime('%m/%d/%Y %H:%M:%S')
    msg = msg_date + ':  ' + msg_type_arg + ' - ' + msg_arg

    # Write message to log file
    if append_flag_arg == 1:
        log = open(log_file, 'a')
    else:
        log = open(log_file, 'w')

    #log.write(msg + '\r\n')
    log.write(msg)
    log.write('\n')
    log.close()

# -----------------------------------------------------------------------------#
#   Function:  read_log(path_arg, file_name_arg)
#
#   Description:
#   Open file in read mode to display contents
#   Function arguments:
#   - path_arg = path of source file
#   - file_name_arg = name of source file
# -----------------------------------------------------------------------------#
def read_log():
    # Initialization
    import os

    # Read log file
    log_file = 'ingestion_service_log.txt'
    log = open(log_file, 'r')
    results = log.readlines()
    log.close()

    # Return log contents
    return results


#-----------------------------------------------------------------------------#
#   Function:  set_file_name(url_arg)
#
#   Description:
#   Create temporary file name
#
#   Function Arguments:
#   - url_arg = url for file source
#   Return argument:
#   - temp_file_name
#-----------------------------------------------------------------------------#
def set_file_name(url_arg):

    import datetime
    import random
    import os

    # Build temp file name.  If source file is not zip then treat as a text file
    file_ext = os.path.splitext(url_arg)[-1]
    file_ext = file_ext[-3:]

    if file_ext == 'zip':
        temp_file_name = 'temp_' + str(random.randint(10000,50000)) + '.zip'
    else:
        temp_file_name = 'temp_' + str(random.randint(10000,50000)) + '.txt'

    return(temp_file_name)

#-----------------------------------------------------------------------------#
#   Function:  unzip_file(zip_file_name_arg)
#
#   Description:
#
#
#   Function arguments:
#   - zip_file_name_arg = path and name of zip file
#-----------------------------------------------------------------------------#

def unzip_file(zip_file_name_arg):

    import zipfile

    # Get list of files in zip file
    zip_obj = zipfile.ZipFile(zip_file_name_arg)
    list_count = len(zip_obj.namelist())

    # Extract file if only one file in zip.  Otherwise raise error.
    if list_count == 1:
        extract_file = zip_obj.namelist()[0]
        zip_obj.extract(extract_file)
        msg = extract_file
    elif list_count > 1:
        msg = 'Error:  Multiple files in zip file.'
    elif list_count == 0:
        msg = 'Error:  No files in zip file.'

    return(msg)

#-----------------------------------------------------------------------------#
#   Function:  write_to_file(dataset_arg)
#
#   Description:
#   Create file and write dataset_arg to file.
#
#   Function arguments:
#   - dataset_arg = Bytes object that will be populated in new file
#   - path_arg = target file folder
#   - file_name_arg = target file name
#   - format_arg = TXT or JSON
#-----------------------------------------------------------------------------#

def write_to_file(dataset_arg, path_arg, file_name_arg, format_arg):

    import os
    import json

    # Check if path exists and make if needed
    if not os.path.exists(path_arg):
        os.makedirs(path_arg)

    # Create and populate target file
    if path_arg.endswith('/'):
        target_file = path_arg + file_name_arg
    else:
        target_file = path_arg +'/'+ file_name_arg

    # Build json target file
    if format_arg == 2:
        target_file = target_file +'.json'
        target = open(target_file, 'wb')
        json.dump(dataset_arg, target)

    # Build csv target file
    if format_arg == 1:
        target_file = target_file + '.csv'
        target = open(target_file, 'wb')
        target.write(dataset_arg)

    # Clean up
        target.close()






# -----------------------------------------------------------------------------#
#   Function:  get_site_list()
#
#   Description:
#   Build list of public web sites configured for ingestion.
# -----------------------------------------------------------------------------#

def get_site_list():

    # Initialization
    from app_model.models import ingest_configs

    # Build list object of configured sites
    sites = ingest_configs.objects.all()
    return(sites)

# -----------------------------------------------------------------------------#
#   Function:  get_ingest_site()
#
#   Description:
#   Get all configs parameters for specific site
# -----------------------------------------------------------------------------#
def get_ingest_site(ingest_site_arg):
    from app_model.models import ingest_configs

    site = ingest_configs.objects.filter(id = ingest_site_arg)

    return(site)


###############################################################################
#   TO DO:  The following functions are used to test new ideas.  They should be
#   deleted once the solution is finished
###############################################################################

def convert_json_to_csv(json_file_name_arg):
    # Initiatlization
    import csv
    import json

    # Open input (json) and output (csv) files
    #input_obj = open(json_file_name_arg, 'r')

    input_obj = open(json_file_name_arg, 'r')
    input_data = json.load(input_obj)
    input_obj.close()

    output_file = json_file_name_arg + '.csv'
    output_obj = open(output_file, 'w')

    # Convert json file to csv file
    writer = csv.writer(output_obj)

    for item in input_data:
        writer.writerow(input_data[item])

    output_obj.close()

    return(output_file)

#=========================

def parse_json(json_file):
    import json
    json_obj = open(json_file, 'r')
    json_data = json.load(json_obj)
    json_obj.close()

    for key in json_data:
        value = json_data[key]
        #print("The key and values are ({}) = ({})".format(key,value))
        print(key)
        print('\n')
        print(value[0])
