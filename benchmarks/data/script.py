import requests
import json

def get_node_power():
    # The API endpoint
    url = "http://localhost:9090/api/v1/query?query=kepler_node_core_joules_total{}"

    # A GET request to the API
    response = requests.get(url)

    # # Print the response
    response_json = response.json()
    # print(type(response_json))
    print(len(response_json))

    # print(response_json.get('data').get('result'))

    power = {}

    # Iterate through the 'items' and extract the 'power' values
    for item in response_json.get('data').get('result'):
        node_name = item.get('metric').get('instance')
        p = item.get('value')[1]
        power[node_name] = p

    print(power)

def get_cpu_utl():
    # The API endpoint
    url = "http://localhost:9090/api/v1/query?query=sum(node_cpu_seconds_total)"

    # A GET request to the API
    response = requests.get(url)

    # # Print the response
    response_json = response.json()
    print(response_json)
    print(len(response_json))

    print(response_json.get('data').get('result'))

    cpu = {}

    # Iterate through the 'items' and extract the 'power' values
    for item in response_json.get('data').get('result'):
        p = item.get('value')[1]
        cpu['node_cpu_seconds_total'] = p

    print(cpu)

if __name__ == '__main__':
    get_cpu_utl()
