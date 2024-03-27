# Start time
2023-12-18 16:47:00

# End time
2023-12-18 17:50:00

## Useful prometheus queries
1. `sum by (instance) (rate(node_cpu_seconds_total{mode!='idle'}[5m]))`
2. `rate(kepler_node_core_joules_total[5m])`

# Peaks logs
1. `KubernetesMetricsServer {map[10.242.64.10:{[{ CPU Latest  8.85} { Memory Latest  64.6885442152741}] {} {}} 10.242.64.8:{[{ CPU Latest  10.675} { Memory Latest  56.53180720333761}] {} {}}]}}`
2. `KubernetesMetricsServer {map[10.242.64.10:{[{ CPU Latest  8.75} { Memory Latest  64.4634774056503}] {} {}} 10.242.64.8:{[{ CPU Latest  10.775} { Memory Latest  55.836405867269555}] {} {}}]}}`

# Observe node power metrics using promethus.
1. Port forward prometheus pod `kubectl port-forward prometheus-k8s-0 9090:9090 -n monitoring`

## Default scheduler
1. `kubectl apply -f default_scheduler.yaml`
2. Get Node where pod is running `kubectl get pods -n felix -o wide`

```
NAME                               READY   STATUS    RESTARTS   AGE     IP              NODE           NOMINATED NODE   READINESS GATES
cpu-stress-test-765878fbdd-ws2fl   1/1     Running   0          3m49s   172.17.72.230   10.242.64.10   <none>           <none>
```
### Logs
`KubernetesMetricsServer {map[10.242.64.10:{[{ CPU Latest  13.925} { Memory Latest  65.0112054753661}] {} {}} 10.242.64.8:{[{ CPU Latest  11.1} { Memory Latest  56.46977798772797}] {} {}}]}}`

3. Increase the replica to 2 in deployment after ~10 minutes
	* Use command : `kubectl edit deployment cpu-stress-test -n felix`
```
NAME                               READY   STATUS    RESTARTS   AGE   IP              NODE           NOMINATED NODE   READINESS GATES
cpu-stress-test-765878fbdd-pq4vn   1/1     Running   0          34s   172.17.97.113   10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-ws2fl   1/1     Running   0          11m   172.17.72.230   10.242.64.10   <none>           <none>
```
### Logs
`KubernetesMetricsServer {map[10.242.64.10:{[{ CPU Latest  13.775} { Memory Latest  64.65191480614125}] {} {}} 10.242.64.8:{[{ CPU Latest  16.475} { Memory Latest  56.49317100091409}] {} {}}]}}`

4. Increasing again
```
NAME                               READY   STATUS    RESTARTS   AGE   IP              NODE           NOMINATED NODE   READINESS GATES
cpu-stress-test-765878fbdd-pq4vn   1/1     Running   0          10m   172.17.97.113   10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-tkhxk   1/1     Running   0          12s   172.17.72.205   10.242.64.10   <none>           <none>
cpu-stress-test-765878fbdd-ws2fl   1/1     Running   0          21m   172.17.72.230   10.242.64.10   <none>           <none>


NAME           CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%   
10.242.64.10   772m         19%    5061Mi          85%       
10.242.64.8    634m         16%    4371Mi          73% 
```

### Logs
`KubernetesMetricsServer {map[10.242.64.10:{[{ CPU Latest  18.775} { Memory Latest  65.455746433797}] {} {}} 10.242.64.8:{[{ CPU Latest  16.85} { Memory Latest  56.19862026499002}] {} {}}]}}`

5. Increasing again
```
NAME                               READY   STATUS    RESTARTS   AGE     IP              NODE           NOMINATED NODE   READINESS GATES
cpu-stress-test-765878fbdd-gz82x   1/1     Running   0          12s     172.17.97.94    10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-pq4vn   1/1     Running   0          15m     172.17.97.113   10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-tkhxk   1/1     Running   0          5m40s   172.17.72.205   10.242.64.10   <none>           <none>
cpu-stress-test-765878fbdd-ws2fl   1/1     Running   0          26m     172.17.72.230   10.242.64.10   <none>           <none>

NAME           CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%   
10.242.64.10   764m         19%    5013Mi          85%       
10.242.64.8    855m         21%    4392Mi          74%
```
6. Increasing again
```
NAME                               READY   STATUS    RESTARTS       AGE     IP              NODE           NOMINATED NODE   READINESS GATES
cpu-stress-test-765878fbdd-gz82x   1/1     Running   0              5m25s   172.17.97.94    10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-hrjcs   1/1     Running   0              11s     172.17.72.217   10.242.64.10   <none>           <none>
cpu-stress-test-765878fbdd-pq4vn   1/1     Running   0              21m     172.17.97.113   10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-tkhxk   1/1     Running   0              10m     172.17.72.205   10.242.64.10   <none>           <none>
cpu-stress-test-765878fbdd-ws2fl   1/1     Running   1 (2m1s ago)   32m     172.17.72.230   10.242.64.10   <none>           <none>

NAME           CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%   
10.242.64.10   976m         24%    5067Mi          85%       
10.242.64.8    849m         21%    4405Mi          74%
```
7. Increasing again
```
NAME                               READY   STATUS    RESTARTS        AGE     IP              NODE           NOMINATED NODE   READINESS GATES
cpu-stress-test-765878fbdd-ds6hx   1/1     Running   0               12s     172.17.97.101   10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-gz82x   1/1     Running   0               10m     172.17.97.94    10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-hrjcs   1/1     Running   0               5m20s   172.17.72.217   10.242.64.10   <none>           <none>
cpu-stress-test-765878fbdd-pq4vn   1/1     Running   0               26m     172.17.97.113   10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-tkhxk   1/1     Running   0               16m     172.17.72.205   10.242.64.10   <none>           <none>
cpu-stress-test-765878fbdd-ws2fl   1/1     Running   1 (7m10s ago)   37m     172.17.72.230   10.242.64.10   <none>           <none>

NAME           CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%   
10.242.64.10   966m         24%    5028Mi          85%       
10.242.64.8    1007m        27%    4390Mi          74%
```
8. Increasing again
```
NAME                               READY   STATUS    RESTARTS      AGE     IP              NODE           NOMINATED NODE   READINESS GATES
cpu-stress-test-765878fbdd-ds6hx   1/1     Running   0             5m20s   172.17.97.101   10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-gz82x   1/1     Running   0             15m     172.17.97.94    10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-hrjcs   1/1     Running   0             10m     172.17.72.217   10.242.64.10   <none>           <none>
cpu-stress-test-765878fbdd-pbcll   1/1     Running   0             12s     172.17.72.224   10.242.64.10   <none>           <none>
cpu-stress-test-765878fbdd-pq4vn   1/1     Running   1 (69s ago)   31m     172.17.97.113   10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-tkhxk   1/1     Running   0             21m     172.17.72.205   10.242.64.10   <none>           <none>
cpu-stress-test-765878fbdd-ws2fl   1/1     Running   1 (12m ago)   42m     172.17.72.230   10.242.64.10   <none>           <none>

NAME           CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%   
10.242.64.10   1177m        30%    5072Mi          86%       
10.242.64.8    1051m        26%    4433Mi          75% 
```
9. Increasing again
```
NAME                               READY   STATUS    RESTARTS        AGE     IP              NODE           NOMINATED NODE   READINESS GATES
cpu-stress-test-765878fbdd-d8s2h   1/1     Running   0               11s     172.17.97.99    10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-ds6hx   1/1     Running   0               9m33s   172.17.97.101   10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-gz82x   1/1     Running   0               19m     172.17.97.94    10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-hrjcs   1/1     Running   0               14m     172.17.72.217   10.242.64.10   <none>           <none>
cpu-stress-test-765878fbdd-pbcll   1/1     Running   0               4m25s   172.17.72.224   10.242.64.10   <none>           <none>
cpu-stress-test-765878fbdd-pq4vn   1/1     Running   1 (5m22s ago)   35m     172.17.97.113   10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-tkhxk   1/1     Running   0               25m     172.17.72.205   10.242.64.10   <none>           <none>
cpu-stress-test-765878fbdd-ws2fl   1/1     Running   1 (16m ago)     46m     172.17.72.230   10.242.64.10   <none>           <none>

NAME           CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%   
10.242.64.10   1168m        29%    5048Mi          85%       
10.242.64.8    1257m        32%    4376Mi          74% 
```
10. Increasing again
```
NAME                               READY   STATUS    RESTARTS      AGE     IP              NODE           NOMINATED NODE   READINESS GATES
cpu-stress-test-765878fbdd-6l6pd   1/1     Running   0             7s      172.17.72.221   10.242.64.10   <none>           <none>
cpu-stress-test-765878fbdd-d8s2h   1/1     Running   0             5m15s   172.17.97.99    10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-ds6hx   1/1     Running   0             14m     172.17.97.101   10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-gz82x   1/1     Running   0             24m     172.17.97.94    10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-hrjcs   1/1     Running   0             19m     172.17.72.217   10.242.64.10   <none>           <none>
cpu-stress-test-765878fbdd-pbcll   1/1     Running   0             9m29s   172.17.72.224   10.242.64.10   <none>           <none>
cpu-stress-test-765878fbdd-pq4vn   1/1     Running   1 (10m ago)   40m     172.17.97.113   10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-tkhxk   1/1     Running   1 (19s ago)   30m     172.17.72.205   10.242.64.10   <none>           <none>
cpu-stress-test-765878fbdd-ws2fl   1/1     Running   1 (21m ago)   51m     172.17.72.230   10.242.64.10   <none>           <none>

NAME           CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%   
10.242.64.10   1356m        34%    5065Mi          85%       
10.242.64.8    1240m        31%    4408Mi          74% 
```

11. Delete all load generation pods in the cluster - `kubectl delete deployment cpu-stress-test -n felix` and repeat the same with peaks scheduler.
```
NAME           CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%   
10.242.64.10   362m         9%     5036Mi          85%       
10.242.64.8    437m         11%    4457Mi          75% 
```

12. Deploying load generator pods
# Start time
2023-12-18 18:08:00


```
KubernetesMetricsServer {map[10.242.64.10:{[{ CPU Latest  8.45} { Memory Latest  64.66073206418561}] {} {}} 10.242.64.8:{[{ CPU Latest  11.55} { Memory Latest  54.63943820546913}] {} {}}]}}
I1218 18:07:24.840054       1 schedule_one.go:93] "Attempting to schedule pod" pod="felix/cpu-stress-test-588844b6f5-bnbtf"
Running score plugins
Node : 10.242.64.10 , Node cpu usage current : 8.45 , predicted : 13.45
Jump in power 7.876485328353602  score 59
Node : 10.242.64.8 , Node cpu usage current : 11.55 , predicted : 16.55
Jump in power 12.04362556078668  score 39
Felix : [{Name:10.242.64.10 Scores:[{Name:Peaks Score:100}] TotalScore:100} {Name:10.242.64.8 Scores:[{Name:Peaks Score:0}] TotalScore:0}]
Felix : prioritylist [{Name:10.242.64.10 Scores:[{Name:Peaks Score:100}] TotalScore:100} {Name:10.242.64.8 Scores:[{Name:Peaks Score:0}] TotalScore:0}]
I1218 18:07:24.840804       1 default_binder.go:53] "Attempting to bind pod to node" pod="felix/cpu-stress-test-588844b6f5-bnbtf" node="10.242.64.10"

NAME                               READY   STATUS    RESTARTS   AGE   IP              NODE           NOMINATED NODE   READINESS GATES
cpu-stress-test-588844b6f5-bnbtf   1/1     Running   0          49s   172.17.72.229   10.242.64.10   <none>           <none>

NAME           CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%   
10.242.64.10   487m         12%    4999Mi          84%       
10.242.64.8    421m         10%    4296Mi          72% 
```

13. Incresing replicas
```
KubernetesMetricsServer {map[10.242.64.10:{[{ CPU Latest  13.95} { Memory Latest  64.40518273389415}] {} {}} 10.242.64.8:{[{ CPU Latest  10.8} { Memory Latest  55.62818289613553}] {} {}}]}}
I1218 18:17:47.232429       1 schedule_one.go:93] "Attempting to schedule pod" pod="felix/cpu-stress-test-588844b6f5-sqxtq"
Running score plugins
Node : 10.242.64.10 , Node cpu usage current : 13.95 , predicted : 18.949999999999996
Jump in power 6.984190411753006  score 67
Node : 10.242.64.8 , Node cpu usage current : 10.8 , predicted : 15.8
Jump in power 12.710531334289069  score 37
Felix : [{Name:10.242.64.10 Scores:[{Name:Peaks Score:100}] TotalScore:100} {Name:10.242.64.8 Scores:[{Name:Peaks Score:0}] TotalScore:0}]
Felix : prioritylist [{Name:10.242.64.10 Scores:[{Name:Peaks Score:100}] TotalScore:100} {Name:10.242.64.8 Scores:[{Name:Peaks Score:0}] TotalScore:0}]
I1218 18:17:47.233000       1 default_binder.go:53] "Attempting to bind pod to node" pod="felix/cpu-stress-test-588844b6f5-sqxtq" node="10.242.64.10"

NAME                               READY   STATUS    RESTARTS   AGE   IP              NODE           NOMINATED NODE   READINESS GATES
cpu-stress-test-588844b6f5-bnbtf   1/1     Running   0          10m   172.17.72.229   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-sqxtq   1/1     Running   0          10s   172.17.72.245   10.242.64.10   <none>           <none>

NAME           CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%   
10.242.64.10   532m         13%    4963Mi          84%       
10.242.64.8    430m         10%    4314Mi          73%  
```
14. Increasing again
```
I1218 18:28:40.769628       1 schedule_one.go:93] "Attempting to schedule pod" pod="felix/cpu-stress-test-588844b6f5-8rrk2"
Running score plugins
Node : 10.242.64.10 , Node cpu usage current : 19.125 , predicted : 24.125
Jump in power 6.2371356322163445  score 75
Node : 10.242.64.8 , Node cpu usage current : 10.65 , predicted : 15.65
Jump in power 12.848280155373295  score 36
Felix : [{Name:10.242.64.10 Scores:[{Name:Peaks Score:100}] TotalScore:100} {Name:10.242.64.8 Scores:[{Name:Peaks Score:0}] TotalScore:0}]

NAME                               READY   STATUS    RESTARTS   AGE   IP              NODE           NOMINATED NODE   READINESS GATES
cpu-stress-test-588844b6f5-8rrk2   1/1     Running   0          8s    172.17.72.211   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-bnbtf   1/1     Running   0          21m   172.17.72.229   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-sqxtq   1/1     Running   0          11m   172.17.72.245   10.242.64.10   <none>           <none>
                              
NAME           CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%   
10.242.64.10   990m         25%    5026Mi          85%       
10.242.64.8    424m         10%    4330Mi          73%  
```
15. Increasing again
```
Running score plugins
Node : 10.242.64.10 , Node cpu usage current : 24.75 , predicted : 29.75
Jump in power 5.515464006313582  score 85
Node : 10.242.64.8 , Node cpu usage current : 10.825 , predicted : 15.825
Jump in power 12.687717207940976  score 37
Felix : [{Name:10.242.64.10 Scores:[{Name:Peaks Score:100}] TotalScore:100} {Name:10.242.64.8 Scores:[{Name:Peaks Score:0}] TotalScore:0}]
Felix : prioritylist [{Name:10.242.64.10 Scores:[{Name:Peaks Score:100}] TotalScore:100} {Name:10.242.64.8 Scores:[{Name:Peaks Score:0}] TotalScore:0}]


NAME                               READY   STATUS    RESTARTS   AGE     IP              NODE           NOMINATED NODE   READINESS GATES
cpu-stress-test-588844b6f5-8rrk2   1/1     Running   0          5m19s   172.17.72.211   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-bnbtf   1/1     Running   0          26m     172.17.72.229   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-d66vw   1/1     Running   0          8s      172.17.72.212   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-sqxtq   1/1     Running   0          16m     172.17.72.245   10.242.64.10   <none>           <none>

NAME           CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%   
10.242.64.10   1179m        30%    5000Mi          84%       
10.242.64.8    443m         11%    4337Mi          73% 
```
16. Increasing again
```
I1218 18:38:56.029144       1 schedule_one.go:93] "Attempting to schedule pod" pod="felix/cpu-stress-test-588844b6f5-m6szt"
Running score plugins
Node : 10.242.64.10 , Node cpu usage current : 29.65 , predicted : 34.65
Jump in power 4.955209170500517  score 95
Node : 10.242.64.8 , Node cpu usage current : 10.575 , predicted : 15.575
Jump in power 12.917713372320172  score 36
Felix : [{Name:10.242.64.10 Scores:[{Name:Peaks Score:100}] TotalScore:100} {Name:10.242.64.8 Scores:[{Name:Peaks Score:0}] TotalScore:0}]
Felix : prioritylist [{Name:10.242.64.10 Scores:[{Name:Peaks Score:100}] TotalScore:100} {Name:10.242.64.8 Scores:[{Name:Peaks Score:0}] TotalScore:0}]
I1218 18:38:56.030355       1 default_binder.go:53] "Attempting to bind pod to node" pod="felix/cpu-stress-test-588844b6f5-m6szt" node="10.242.64.10"

NAME                               READY   STATUS    RESTARTS      AGE     IP              NODE           NOMINATED NODE   READINESS GATES
cpu-stress-test-588844b6f5-8rrk2   1/1     Running   0             10m     172.17.72.211   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-bnbtf   1/1     Running   1 (90s ago)   31m     172.17.72.229   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-d66vw   1/1     Running   0             5m11s   172.17.72.212   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-m6szt   1/1     Running   0             7s      172.17.72.233   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-sqxtq   1/1     Running   0             21m     172.17.72.245   10.242.64.10   <none>           <none>

NAME           CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%   
10.242.64.10   1355m        34%    5039Mi          85%       
10.242.64.8    425m         10%    4351Mi          73% 
```
17. Increasing again - Here request didnt come to peaks pod
```
NAME                               READY   STATUS    RESTARTS        AGE     IP              NODE           NOMINATED NODE   READINESS GATES
cpu-stress-test-588844b6f5-8rrk2   1/1     Running   0               17m     172.17.72.211   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-bnbtf   1/1     Running   1 (8m42s ago)   38m     172.17.72.229   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-d66vw   1/1     Running   0               12m     172.17.72.212   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-m6szt   1/1     Running   0               7m19s   172.17.72.233   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-q7dt4   1/1     Running   0               38s     172.17.97.116   10.242.64.8    <none>           <none>
cpu-stress-test-588844b6f5-sqxtq   1/1     Running   0               28m     172.17.72.245   10.242.64.10   <none>           <none>

NAME           CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%   
10.242.64.10   1382m        35%    5033Mi          85%       
10.242.64.8    657m         16%    4359Mi          73% 
```
18. Increasing again
```
NAME                               READY   STATUS    RESTARTS        AGE     IP              NODE           NOMINATED NODE   READINESS GATES
cpu-stress-test-588844b6f5-8rrk2   1/1     Running   0               23m     172.17.72.211   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-bnbtf   1/1     Running   1 (14m ago)     44m     172.17.72.229   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-cb6s7   1/1     Running   0               102s    172.17.97.97    10.242.64.8    <none>           <none>
cpu-stress-test-588844b6f5-d66vw   1/1     Running   0               18m     172.17.72.212   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-m6szt   1/1     Running   0               13m     172.17.72.233   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-q7dt4   1/1     Running   0               6m42s   172.17.97.116   10.242.64.8    <none>           <none>
cpu-stress-test-588844b6f5-sqxtq   1/1     Running   1 (4m23s ago)   34m     172.17.72.245   10.242.64.10   <none>           <none>

NAME           CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%   
10.242.64.10   1417m        36%    5017Mi          85%       
10.242.64.8    844m         21%    4355Mi          73% 
```

