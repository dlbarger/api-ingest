###############################################################################
#   Script: ingest_service.py
#   Author: Dennis Barger
#   Date:   12/27/2016
#
#   Description:
#   Script contains functions to ingest data from public website based on the
#   following access methods:  1) http request, 2) API web service, 3) File
#   download from url.
#
#   Functions:
#   - ingest_http_service
#   - ingest_web_service
#   - ingest_file_service
#   -
###############################################################################


#-----------------------------------------------------------------------------#
#   Function:  ingest_http_request(url_arg, key_label_arg, key_value_arg)
#
#   Description:
#   Ingest data using http request method
#
#   Function arguments:
#   - url_arg = url string to access website
#   - key_label_arg = header label for access key
#   - key_value_arg = registered access key value
#-----------------------------------------------------------------------------#
def ingest_http_request(url_arg, key_label_arg, key_value_arg):

    # Initialize required packages
    from urllib.request import Request, urlopen
    from urllib.error import URLError, HTTPError
    from api_ingest.utils import write_log

    try:
        # Log status message
        #write_log('Start ingest_http_request: ' + url_arg, 'STATUS')

        # Build http request string
        http_request = Request(url_arg)
        http_request.add_header(key_label_arg, key_value_arg)

        # Open url and read data
        dataset = urlopen(http_request).read()

    except HTTPError as err:
        err_code = str(err.code)
        write_log('Error Code: ' + err_code + ' - ' + err.reason, 'ERROR', 1)
    except URLError as err:
        write_log('Error: ' + err.reason, 'ERROR', 1)
    else:
        write_log('No HTTP or URL errors', 'STATUS', 1)

    # Return extracted data
    return dataset

#-----------------------------------------------------------------------------#
#   Function:  ingest_web_service(url_arg, key_label_arg, key_value_arg)
#
#   Description:
#   Ingest data by connecting to API web service
#
#   Function arguments:
#   - url_arg = url string to access website
#   - key_label_arg = header label for access key (optional)
#   - key_value_arg = registered access key value (optional)
#-----------------------------------------------------------------------------#
def ingest_web_service(url_arg, key_label_arg, key_value_arg):

    # Initialize required packages
    from urllib.request import urlopen
    from urllib.error import URLError, HTTPError
    from api_ingest.utils import write_log

    try:
        # Build url string.  If key_label_arg is not null then append access key
        url = url_arg
        if not key_label_arg == 'NA':
            url = url + '?' + key_label_arg + '=' + key_value_arg

        # Open url and read data
        dataset = urlopen(url).read()

    except HTTPError as err:
        err_code = str(err.code)
        write_log('Error Code: ' + err_code + ' - ' + err.reason, 'ERROR', 1)
    except URLError as err:
        write_log('Error: ' + err.reason, 'ERROR', 1)
    else:
        write_log('No HTTP or URL errors', 'STATUS', 1)

    # Return extracted data
    return dataset

#-----------------------------------------------------------------------------#
#   Function:  ingest_file_service(url_arg, key_label_arg, key_value_arg)
#
#   Description:
#   Download data file associated with url
#
#   Function arguments:
#   - url_arg = url string to access website
#   - key_label_arg = header label for access key (optional)
#   - key_value_arg = registered access key value (optional)
#
#   Return Object:
#   - download_file = name of file downloaded at target location
#-----------------------------------------------------------------------------#
def ingest_file_service(url_arg, key_label_arg, key_value_arg):

    import os
    import wget

    path = './data'

    # Append url with security key if required
    if key_label_arg:
        url_arg = url_arg + '?' + key_label_arg + '=' + key_value_arg

    #download_file = http_file_download(url_arg)
    download_file = wget.download(url_arg, path)

    # Return downloaded file name
    return download_file









