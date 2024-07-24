import json
import pandas
import os, logging
import time
from datetime import timedelta, datetime
from prometheus_api_client.utils import parse_datetime
from prometheus_api_client import PrometheusConnect, MetricRangeDataFrame
import urllib3
from jproperties import Properties
urllib3.disable_warnings()

configs = Properties()

start_time = parse_datetime("1d")
end_time = parse_datetime("now")
chunk_size = timedelta(days=1)

def loadProperties():
    with open('metrics.properties', 'rb') as config_file:
        configs.load(config_file)
    metrics = configs.get("metrics").data
    return metrics.split(',')

metrics_list = loadProperties()

if(os.getenv('PROMETHEUS') != None):
    PROMETHEUS = os.getenv('PROMETHEUS')
else:
    print("prometheus path is not an environment variable, attempting to query prometheus locally")
    PROMETHEUS = 'http://localhost:9090'

if(os.getenv('STORAGEPATH') != None):
    PROMETHEUS = os.getenv('STORAGEPATH')
else:
    print("storage path is not an environment variable, attempting to store locally")
    STORAGEPATH = 'data'

prom = PrometheusConnect(url=PROMETHEUS, disable_ssl=True)


def download_and_save(metric, client, start_time, end_time, chunk_size):
    data = client.get_metric_range_data(metric, start_time = start_time, end_time = end_time, chunk_size = chunk_size)
    try:
        df = MetricRangeDataFrame(data)
        df.index = pandas.to_datetime(df.index, unit="s")
        filename=f"{STORAGEPATH}/{metric}_{str(datetime.now())}.csv"
        df.to_csv(filename)
    except KeyError:
        logging.warning(metric + " not found, data not saved for " + metric) 
    
for i in metrics_list:
    print("saving metrics for,",i)
    download_and_save(i, prom, start_time, end_time, chunk_size)

while True:
    print("testing  port connection")
    time.sleep(5)