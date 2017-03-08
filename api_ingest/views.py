from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from api_ingest.utils import get_site_list, get_ingest_site, write_to_file, write_log, read_log
from api_ingest.ingest_service import ingest_http_request, ingest_web_service, ingest_file_service


# sites functions create a context variable (sites) linked to
# index.html

@login_required()
def sites(request):
    values = get_site_list()
    return render(request, 'index.html', {'sites':values})

@login_required()
def ingest_site(request):
    val = request.GET['id']
    values = get_ingest_site(val)
    return render(request, 'ingest.html', {'values':values})

@login_required()
def about(request):
    return render(request, 'about.html')

@login_required()
def start_ingest(request):

    # Determine ingestion type and start ingestion process
    val = request.GET['data_src_id']
    values = get_ingest_site(val)
    file_path = 'data'
    val_str = str(val)
    file_name = 'ingest_file_id' + val_str

    for item in values:
        # Write Log:  Start ingestion process
        write_log('Ingestion process started: ' + item.ingest_url, 'STATUS', 0)

        # Initiate ingestion service based on ingestion type
        if item.ingest_type == 1: # http request method
            #results = ingest_http_request(item.ingest_url, item.access_key_label, item.access_key_value)
            write_log('Service stubbed but not running', 'STATUS', 1)

        elif item.ingest_type == 2: # web server method
            # Set total count of records to ingest
            cnt = 100000
            index = 0
            start_record = 0
            batch_size = 1000
            end_record = batch_size
            range_label = '/row/'
            #url = item.ingest_url

            while index <= cnt:
                # Set batch range and extract data
                ingest_range = str(start_record) + ':' + str(end_record)
                url = item.ingest_url + range_label + ingest_range
                results = ingest_web_service(url, item.access_key_label, item.access_key_value)

                ## TO DO:  add code to create unique file name for each batch.
                data_file_name = file_name + '-' + str(end_record)
                write_to_file(results, file_path, data_file_name, item.ingest_format)
                write_log(url, 'STATUS', 1)
                write_log('Data extracted: ' + ingest_range, 'STATUS', 1)

                # Reset counters
                start_record = end_record + 1
                end_record = start_record + batch_size
                index = start_record

        else: # file download method
            file = ingest_file_service(item.ingest_url, item.access_key_label, item.access_key_value)
            write_log('File downloaded: ' + file, 'STATUS', 1)

    # Write Log:  Extracted data from API
    #write_log('Data extracted', 'STATUS', 1)

    # Write data extracted from ingestion service to file.
    #   - File downloads are not written to file
    #if not item.ingest_type == 3:
    #    write_to_file(results, file_path, file_name, item.ingest_format)

    # Write Log:  Ingestion process finished
    write_log('Process complete', 'STATUS', 1)

    # Read log file for process status
    status = read_log()

    return render(request, 'ingest_status.html',{'status':status})



