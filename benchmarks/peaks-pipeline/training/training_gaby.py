import os
import pandas as pd
import model
import torch
from flask import Flask
from kubernetes import client, config
import json

app = Flask(__name__)

def load_metric_files(data_folder):
    data_contents = os.listdir(data_folder)
    cfile,nppfile,ndpfile = "","",""
    for file in data_contents:
        if file.startswith("node_cpu_seconds_total"):
            cfile = file 
        if file.startswith("kepler_node_package_joules_total"):
            nppfile = file 
        if file.startswith("kepler_node_dram_joules_total"):
            ndpfile = file
    return cfile,nppfile,ndpfile


def read_metrics(file, data_folder, is_cpu_util):
    as_df = pd.read_csv(data_folder+file)
    if is_cpu_util: 
        as_df = as_df[as_df['mode']!='idle']
    as_df = as_df.groupby(['instance', 'timestamp'], as_index=False)['value'].sum()
    as_df['timestamp'] = pd.to_datetime(as_df['timestamp'])
    return as_df

# data_folder = os.getenv('STORAGEPATH')

data_folder = "/tmp/pvc/data"

cpu_util_file, node_package_power_file, node_dram_power_file  = load_metric_files(data_folder)

cpu_util_agg = read_metrics(cpu_util_file, data_folder, True)
node_package_power = read_metrics(node_package_power_file, data_folder, False)
node_dram_power = read_metrics(node_dram_power_file, data_folder, False)

node_power_metrics = pd.merge(node_package_power, node_dram_power, on = ["timestamp", "instance"])
node_power_metrics = node_power_metrics.rename(columns={"value_x":"package", "value_y":"dram"})
node_power_metrics['power'] = node_power_metrics['package'] + node_power_metrics['dram']

node_power_models = {}
for node in cpu_util_agg['instance'].unique():
    print("Node : ", node)
    cpu = cpu_util_agg[cpu_util_agg['instance']==node]
    power = node_power_metrics[node_power_metrics['instance']==node]
    data = pd.merge_asof(cpu, power, on = 'timestamp')
    data.rename(columns={'value':'util'}, inplace=True)
    data.sort_values('timestamp', inplace=True)
    m = model.UtilisationPowerModel()
    
    node_df = data
    node_df['util'] = node_df['util'].diff()
    node_df['energy'] = node_df['power'].diff()
    node_df.fillna(0, inplace=True)

#     node_df = node_df.iloc[500: , :]

    node_df = node_df[(node_df[['util']] != 0).all(axis=1)]
    node_df = node_df[(node_df[['energy']] != 0).all(axis=1)]
    max_util = max(node_df['util'])
    node_df['util'] = node_df['util']/max_util

    node_df['power'] = node_df['energy']/3
    #TODO divide by 3 
    node_df.fillna({'power': node_df['power'].mean()}, inplace=True)
    node_power_models[node] = m.get_model(node_df[['util', 'power']])

    #torch.save(node_power_models[node], "trained_models/" + node + ".pt")
    #npm_ndarray = node_power_models[node][0].flatten()

    #ndarray, list, tuple[Tensor, Tensor, Tensor]
    # npm_dict = {}
    # npm_dict["ndarray"] = node_power_models[node][0].flatten()
    # npm_dict["list"] = node_power_models[node][1]
    # npm_dict["tuple[Tensor, Tensor, Tensor]"] = {k for k in tf.strings.as_string(tensor)}

    

    # with open('model.json', 'w') as f:
    #     json.dump(json_serializable_dict, f)


# def get_power(u, model):
#     return model[0] + model[1] * torch.exp(model[2] * u)



# def create_configmap(data , string_data , client_api):
#     secret = client.V1Secret(
#         api_version="v1",
#         kind="ConfigMap",
#         metadata=client.V1ObjectMeta(name="power-model-parameters"),
#         data=data , 
#         string_data=string_data
#     )

#     api = client_api.create_namespaced_config_map(namespace="default", body=secret)
#     return api

# configuration = client.Configuration()
# configuration.verify_ssl = False
# client.Configuration.set_default(configuration)
# client_api = client.CoreV1Api()

# create_configmap({} , {}, client_api)


@app.route('/')
def healthcheck():
    return ("Health check")