# Loadwatcher configuration
Creating namespace : `kubectl create ns loadwatcher`
Starting loadwatcher with configs : `kubectl apply -f loadwatcher.yaml`
Port forward : `port-forward load-watcher-deployment-5757d48b7c-pchzw 2020:2020 -n loadwatcher`
Query : `curl 127.0.0.1:2020/watcher`

Response: 
```
{
    "timestamp": 1709622955,
    "window":
    {
        "duration": "15m",
        "start": 1709622055,
        "end": 1709622955
    },
    "source": "KubernetesMetricsServer",
    "data":
    {
        "NodeMetricsMap":
        {
            "tantawi1":
            {
                "metrics":
                [
                    {
                        "name": "",
                        "type": "CPU",
                        "operator": "Latest",
                        "rollup": "",
                        "value": 12.85
                    },
                    {
                        "name": "",
                        "type": "Memory",
                        "operator": "Latest",
                        "rollup": "",
                        "value": 4.329587040601127
                    }
                ],
                "tags":
                {},
                "metadata":
                {
                    "dataCenter": ""
                }
            },
            "tantawi2":
            {
                "metrics":
                [
                    {
                        "name": "",
                        "type": "CPU",
                        "operator": "Latest",
                        "rollup": "",
                        "value": 0.8975
                    },
                    {
                        "name": "",
                        "type": "Memory",
                        "operator": "Latest",
                        "rollup": "",
                        "value": 1.2164097306635622
                    }
                ],
                "tags":
                {},
                "metadata":
                {
                    "dataCenter": ""
                }
            }
        }
    }
}
```