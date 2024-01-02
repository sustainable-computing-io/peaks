import json
import pandas
from datetime import timedelta, datetime
from prometheus_api_client.utils import parse_datetime
from prometheus_api_client import PrometheusConnect, MetricRangeDataFrame
import urllib3
urllib3.disable_warnings()

dev_promurl = 'http://localhost:9090'
prom = PrometheusConnect(url=dev_promurl, disable_ssl=True)

start_time = parse_datetime("1d")
end_time = parse_datetime("now")
chunk_size = timedelta(days=1)
metrics_list = [
    "kepler_node_core_joules_total",
    "node_cpu_seconds_total",
    "container_cpu_usage_seconds_total",
    "kepler_container_joules_total",
    "kepler_node_dram_joules_total",
    "kepler_node_package_joules_total",
    "kepler_node_platform_joules_total",
    "kepler_node_other_joules_total"
]
def download_and_save(metric, client, start_time, end_time, chunk_size):
    data = client.get_metric_range_data(metric, start_time = start_time, end_time = end_time, chunk_size = chunk_size)
    df = MetricRangeDataFrame(data)
    df.index = pandas.to_datetime(df.index, unit="s")
    filename=f"data_repeat/{metric}_{str(datetime.now())}.csv"
    df.to_csv(filename)
for i in metrics_list[3:]:
    print(i)
    download_and_save(i, prom, start_time, end_time, chunk_size)
