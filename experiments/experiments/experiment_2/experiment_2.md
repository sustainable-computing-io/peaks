# Start time
2023-12-31 10:30:00

# End time
2023-12-31 11:28:00


## Starting cluster usage
`10:33:56.895086 KubernetesMetricsServer {map[10.242.64.10:{[{ CPU Latest  8.8} { Memory Latest  67.28550382316308}] {} {}} 10.242.64.8:{[{ CPU Latest  10.625} { Memory Latest  55.98647330454735}] {} {}}]}}`

1. Deploying using default scheduler
`NAME                               READY   STATUS    RESTARTS   AGE   IP              NODE           NOMINATED NODE   READINESS GATES
cpu-stress-test-765878fbdd-9zz4z   1/1     Running   0          50s   172.17.72.231   10.242.64.10   <none>           <none>`

`KubernetesMetricsServer {map[10.242.64.10:{[{ CPU Latest  12.8} { Memory Latest  67.32495475487015}] {} {}} 10.242.64.8:{[{ CPU Latest  11.05} { Memory Latest  55.68377274467457}] {} {}}]}}`

`NAME           CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%   
10.242.64.10   557m         14%    5222Mi          88%       
10.242.64.8    439m         11%    4352Mi          73%   `

2. Scaling up

`NAME                               READY   STATUS    RESTARTS   AGE     IP              NODE           NOMINATED NODE   READINESS GATES
cpu-stress-test-765878fbdd-9zz4z   1/1     Running   0          5m23s   172.17.72.231   10.242.64.10   <none>           <none>
cpu-stress-test-765878fbdd-v5p8z   1/1     Running   0          10s     172.17.97.74    10.242.64.8    <none>           <none>`

`NAME           CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%   
10.242.64.10   555m         14%    5232Mi          88%       
10.242.64.8    638m         16%    4342Mi          73%`

3. Scaling up

`NAME                               READY   STATUS    RESTARTS   AGE     IP              NODE           NOMINATED NODE   READINESS GATES
cpu-stress-test-765878fbdd-9zz4z   1/1     Running   0          10m     172.17.72.231   10.242.64.10   <none>           <none>
cpu-stress-test-765878fbdd-kjwm7   1/1     Running   0          10s     172.17.72.246   10.242.64.10   <none>           <none>
cpu-stress-test-765878fbdd-v5p8z   1/1     Running   0          5m17s   172.17.97.74    10.242.64.8    <none>           <none>`

`NAME           CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%   
10.242.64.10   771m         19%    5247Mi          88%       
10.242.64.8    654m         16%    4370Mi          73%`

4. Scaling up

`NAME                               READY   STATUS    RESTARTS   AGE     IP              NODE           NOMINATED NODE   READINESS GATES
cpu-stress-test-765878fbdd-262cm   1/1     Running   0          6s      172.17.97.89    10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-9zz4z   1/1     Running   0          15m     172.17.72.231   10.242.64.10   <none>           <none>
cpu-stress-test-765878fbdd-kjwm7   1/1     Running   0          5m11s   172.17.72.246   10.242.64.10   <none>           <none>
cpu-stress-test-765878fbdd-v5p8z   1/1     Running   0          10m     172.17.97.74    10.242.64.8    <none>           <none>`

`NAME           CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%   
10.242.64.10   767m         19%    5265Mi          89%       
10.242.64.8    848m         21%    4405Mi          74%`

5. Scaling up

`NAME                               READY   STATUS    RESTARTS   AGE     IP              NODE           NOMINATED NODE   READINESS GATES
cpu-stress-test-765878fbdd-262cm   1/1     Running   0          5m11s   172.17.97.89    10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-9zz4z   1/1     Running   0          20m     172.17.72.231   10.242.64.10   <none>           <none>
cpu-stress-test-765878fbdd-kjwm7   1/1     Running   0          10m     172.17.72.246   10.242.64.10   <none>           <none>
cpu-stress-test-765878fbdd-v5p8z   1/1     Running   0          15m     172.17.97.74    10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-x7rnm   1/1     Running   0          7s      172.17.72.239   10.242.64.10   <none>           <none>`

`NAME           CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%   
10.242.64.10   969m         24%    5244Mi          88%       
10.242.64.8    839m         21%    4409Mi          74% `

6. Scaling up

`NAME                               READY   STATUS    RESTARTS   AGE     IP              NODE           NOMINATED NODE   READINESS GATES
cpu-stress-test-765878fbdd-262cm   1/1     Running   0          10m     172.17.97.89    10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-9zz4z   1/1     Running   0          25m     172.17.72.231   10.242.64.10   <none>           <none>
cpu-stress-test-765878fbdd-cmdh4   1/1     Running   0          7s      172.17.97.117   10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-kjwm7   1/1     Running   0          15m     172.17.72.246   10.242.64.10   <none>           <none>
cpu-stress-test-765878fbdd-v5p8z   1/1     Running   0          20m     172.17.97.74    10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-x7rnm   1/1     Running   0          5m17s   172.17.72.239   10.242.64.10   <none>           <none>`

`NAME           CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%   
10.242.64.10   992m         25%    5250Mi          89%       
10.242.64.8    1050m        26%    4418Mi          74%`

7. Scaling up

`NAME                               READY   STATUS    RESTARTS      AGE    IP              NODE           NOMINATED NODE   READINESS GATES
cpu-stress-test-765878fbdd-262cm   1/1     Running   0             15m    172.17.97.89    10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-4rjhx   1/1     Running   0             5s     172.17.72.200   10.242.64.10   <none>           <none>
cpu-stress-test-765878fbdd-9zz4z   1/1     Running   1 (39s ago)   30m    172.17.72.231   10.242.64.10   <none>           <none>
cpu-stress-test-765878fbdd-cmdh4   1/1     Running   0             5m9s   172.17.97.117   10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-kjwm7   1/1     Running   0             20m    172.17.72.246   10.242.64.10   <none>           <none>
cpu-stress-test-765878fbdd-v5p8z   1/1     Running   0             25m    172.17.97.74    10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-x7rnm   1/1     Running   0             10m    172.17.72.239   10.242.64.10   <none>           <none>`

`NAME           CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%   
10.242.64.10   1184m        30%    5266Mi          89%       
10.242.64.8    1085m        27%    4391Mi          74%`

8. Scaling up

`NAME                               READY   STATUS    RESTARTS        AGE     IP              NODE           NOMINATED NODE   READINESS GATES
cpu-stress-test-765878fbdd-262cm   1/1     Running   0               20m     172.17.97.89    10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-2hrkx   1/1     Running   0               6s      172.17.97.85    10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-4rjhx   1/1     Running   0               5m21s   172.17.72.200   10.242.64.10   <none>           <none>
cpu-stress-test-765878fbdd-9zz4z   1/1     Running   1 (5m55s ago)   36m     172.17.72.231   10.242.64.10   <none>           <none>
cpu-stress-test-765878fbdd-cmdh4   1/1     Running   0               10m     172.17.97.117   10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-kjwm7   1/1     Running   0               25m     172.17.72.246   10.242.64.10   <none>           <none>
cpu-stress-test-765878fbdd-v5p8z   1/1     Running   1 (43s ago)     30m     172.17.97.74    10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-x7rnm   1/1     Running   0               15m     172.17.72.239   10.242.64.10   <none>           <none>`

`NAME           CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%   
10.242.64.10   1172m        29%    5277Mi          89%       
10.242.64.8    1279m        32%    4402Mi          74%`

9. Scaling up

`NAME                               READY   STATUS    RESTARTS        AGE    IP              NODE           NOMINATED NODE   READINESS GATES
cpu-stress-test-765878fbdd-262cm   1/1     Running   0               25m    172.17.97.89    10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-2hrkx   1/1     Running   0               5m5s   172.17.97.85    10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-4rjhx   1/1     Running   0               10m    172.17.72.200   10.242.64.10   <none>           <none>
cpu-stress-test-765878fbdd-9zz4z   1/1     Running   1 (10m ago)     41m    172.17.72.231   10.242.64.10   <none>           <none>
cpu-stress-test-765878fbdd-cmdh4   1/1     Running   0               15m    172.17.97.117   10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-hp42x   1/1     Running   0               14s    172.17.72.218   10.242.64.10   <none>           <none>
cpu-stress-test-765878fbdd-kjwm7   1/1     Running   1 (35s ago)     30m    172.17.72.246   10.242.64.10   <none>           <none>
cpu-stress-test-765878fbdd-v5p8z   1/1     Running   1 (5m42s ago)   35m    172.17.97.74    10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-x7rnm   1/1     Running   0               20m    172.17.72.239   10.242.64.10   <none>           <none>`

`NAME           CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%   
10.242.64.10   1370m        35%    5272Mi          89%       
10.242.64.8    1279m        32%    4394Mi          74%`

10. Scaling up

`NAME                               READY   STATUS    RESTARTS        AGE     IP              NODE           NOMINATED NODE   READINESS GATES
cpu-stress-test-765878fbdd-262cm   1/1     Running   1 (17s ago)     30m     172.17.97.89    10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-2hrkx   1/1     Running   0               9m52s   172.17.97.85    10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-4rjhx   1/1     Running   0               15m     172.17.72.200   10.242.64.10   <none>           <none>
cpu-stress-test-765878fbdd-9zz4z   1/1     Running   1 (15m ago)     45m     172.17.72.231   10.242.64.10   <none>           <none>
cpu-stress-test-765878fbdd-cmdh4   1/1     Running   0               20m     172.17.97.117   10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-hp42x   1/1     Running   0               5m1s    172.17.72.218   10.242.64.10   <none>           <none>
cpu-stress-test-765878fbdd-kjwm7   1/1     Running   1 (5m22s ago)   35m     172.17.72.246   10.242.64.10   <none>           <none>
cpu-stress-test-765878fbdd-ltzpg   1/1     Running   0               8s      172.17.97.110   10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-v5p8z   1/1     Running   1 (10m ago)     40m     172.17.97.74    10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-x7rnm   1/1     Running   0               25m     172.17.72.239   10.242.64.10   <none>           <none>`

`NAME           CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%   
10.242.64.10   1391m        35%    5267Mi          89%       
10.242.64.8    1465m        37%    4449Mi          75%`

11. Scaling up

`NAME                               READY   STATUS    RESTARTS        AGE     IP              NODE           NOMINATED NODE   READINESS GATES
cpu-stress-test-765878fbdd-262cm   1/1     Running   1 (5m28s ago)   35m     172.17.97.89    10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-2hrkx   1/1     Running   0               15m     172.17.97.85    10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-4rjhx   1/1     Running   0               20m     172.17.72.200   10.242.64.10   <none>           <none>
cpu-stress-test-765878fbdd-9zz4z   1/1     Running   1 (20m ago)     51m     172.17.72.231   10.242.64.10   <none>           <none>
cpu-stress-test-765878fbdd-cmdh4   1/1     Running   0               25m     172.17.97.117   10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-hp42x   1/1     Running   0               10m     172.17.72.218   10.242.64.10   <none>           <none>
cpu-stress-test-765878fbdd-kjwm7   1/1     Running   1 (10m ago)     40m     172.17.72.246   10.242.64.10   <none>           <none>
cpu-stress-test-765878fbdd-ltzpg   1/1     Running   0               5m19s   172.17.97.110   10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-qf7cx   0/1     Pending   0               28s     <none>          <none>         <none>           <none>
cpu-stress-test-765878fbdd-v5p8z   1/1     Running   1 (15m ago)     45m     172.17.97.74    10.242.64.8    <none>           <none>
cpu-stress-test-765878fbdd-x7rnm   1/1     Running   1 (24s ago)     30m     172.17.72.239   10.242.64.10   <none>           <none>`

`KubernetesMetricsServer {map[10.242.64.10:{[{ CPU Latest  34.225} { Memory Latest  68.26779675363674}] {} {}} 10.242.64.8:{[{ CPU Latest  36.075} { Memory Latest  56.81926457397299}] {} {}}]}}`

Deleting the deployment 
`KubernetesMetricsServer {map[10.242.64.10:{[{ CPU Latest  8.675} { Memory Latest  68.07547975960628}] {} {}} 10.242.64.8:{[{ CPU Latest  10.925} { Memory Latest  56.22156051017898}] {} {}}]}}`

## Deploying using Peaks scheduler

1. Applying the deployment
`Running score plugins
Node : 10.242.64.10 , Node cpu usage current : 10.825 , predicted : 15.825
Jump in power 7.477983088511379  score 63
Node : 10.242.64.8 , Node cpu usage current : 11.9 , predicted : 16.9
Jump in power 11.744491817385057  score 40
Felix : [{Name:10.242.64.10 Scores:[{Name:Peaks Score:100}] TotalScore:100} {Name:10.242.64.8 Scores:[{Name:Peaks Score:0}] TotalScore:0}]
Felix : prioritylist [{Name:10.242.64.10 Scores:[{Name:Peaks Score:100}] TotalScore:100} {Name:10.242.64.8 Scores:[{Name:Peaks Score:0}] TotalScore:0}]`

`NAME                               READY   STATUS    RESTARTS   AGE   IP              NODE           NOMINATED NODE   READINESS GATES
cpu-stress-test-588844b6f5-tdrtk   1/1     Running   0          42s   172.17.72.241   10.242.64.10   <none>           <none>`

2. Scaling up
`Running score plugins
Node : 10.242.64.10 , Node cpu usage current : 13.975 , predicted : 18.974999999999998
Jump in power 6.980374508858795  score 67
Node : 10.242.64.8 , Node cpu usage current : 10.35 , predicted : 15.35
Jump in power 13.128272483720904  score 35
Felix : [{Name:10.242.64.10 Scores:[{Name:Peaks Score:100}] TotalScore:100} {Name:10.242.64.8 Scores:[{Name:Peaks Score:0}] TotalScore:0}]
Felix : prioritylist [{Name:10.242.64.10 Scores:[{Name:Peaks Score:100}] TotalScore:100} {Name:10.242.64.8 Scores:[{Name:Peaks Score:0}] TotalScore:0}]`

`NAME                               READY   STATUS    RESTARTS   AGE     IP              NODE           NOMINATED NODE   READINESS GATES
cpu-stress-test-588844b6f5-p69n8   1/1     Running   0          27s     172.17.72.236   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-tdrtk   1/1     Running   0          5m43s   172.17.72.241   10.242.64.10   <none>           <none>`

3. Scaling up
`Running score plugins
Node : 10.242.64.10 , Node cpu usage current : 18.825 , predicted : 23.825
Jump in power 6.278174106624953  score 75
Node : 10.242.64.8 , Node cpu usage current : 10.9 , predicted : 15.9
Jump in power 12.619520229414778  score 37
Felix : [{Name:10.242.64.10 Scores:[{Name:Peaks Score:100}] TotalScore:100} {Name:10.242.64.8 Scores:[{Name:Peaks Score:0}] TotalScore:0}]
Felix : prioritylist [{Name:10.242.64.10 Scores:[{Name:Peaks Score:100}] TotalScore:100} {Name:10.242.64.8 Scores:[{Name:Peaks Score:0}] TotalScore:0}]
`

`NAME                               READY   STATUS    RESTARTS   AGE     IP              NODE           NOMINATED NODE   READINESS GATES
cpu-stress-test-588844b6f5-2426x   1/1     Running   0          9s      172.17.72.222   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-p69n8   1/1     Running   0          5m15s   172.17.72.236   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-tdrtk   1/1     Running   0          10m     172.17.72.241   10.242.64.10   <none>           <none>`

4. Scaling up
`Running score plugins
Node : 10.242.64.10 , Node cpu usage current : 24.325 , predicted : 29.325
Jump in power 5.566945353273627  score 84
Node : 10.242.64.8 , Node cpu usage current : 11.1 , predicted : 16.1
Jump in power 12.439448351570991  score 37
Felix : [{Name:10.242.64.10 Scores:[{Name:Peaks Score:100}] TotalScore:100} {Name:10.242.64.8 Scores:[{Name:Peaks Score:0}] TotalScore:0}]
Felix : prioritylist [{Name:10.242.64.10 Scores:[{Name:Peaks Score:100}] TotalScore:100} {Name:10.242.64.8 Scores:[{Name:Peaks Score:0}] TotalScore:0}]`

`NAME                               READY   STATUS    RESTARTS   AGE     IP              NODE           NOMINATED NODE   READINESS GATES
cpu-stress-test-588844b6f5-2426x   1/1     Running   0          4m48s   172.17.72.222   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-f24jg   1/1     Running   0          6s      172.17.72.203   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-p69n8   1/1     Running   0          9m54s   172.17.72.236   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-tdrtk   1/1     Running   0          15m     172.17.72.241   10.242.64.10   <none>           <none>`

5. Scaling up
`Running score plugins
Node : 10.242.64.10 , Node cpu usage current : 29.65 , predicted : 34.65
Jump in power 4.955209170500517  score 95
Node : 10.242.64.8 , Node cpu usage current : 10.55 , predicted : 15.55
Jump in power 12.940941060971692  score 36
Felix : [{Name:10.242.64.10 Scores:[{Name:Peaks Score:100}] TotalScore:100} {Name:10.242.64.8 Scores:[{Name:Peaks Score:0}] TotalScore:0}]
Felix : prioritylist [{Name:10.242.64.10 Scores:[{Name:Peaks Score:100}] TotalScore:100} {Name:10.242.64.8 Scores:[{Name:Peaks Score:0}] TotalScore:0}]`

`NAME                               READY   STATUS    RESTARTS   AGE     IP              NODE           NOMINATED NODE   READINESS GATES
cpu-stress-test-588844b6f5-2426x   1/1     Running   0          10m     172.17.72.222   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-2lszj   1/1     Running   0          8s      172.17.72.207   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-f24jg   1/1     Running   0          5m19s   172.17.72.203   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-p69n8   1/1     Running   0          15m     172.17.72.236   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-tdrtk   1/1     Running   0          20m     172.17.72.241   10.242.64.10   <none>           <none>`

`NAME           CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%   
10.242.64.10   1386m        35%    5358Mi          90%       
10.242.64.8    431m         11%    4421Mi          74% `

6. Scaling up
`NAME                               READY   STATUS    RESTARTS      AGE     IP              NODE           NOMINATED NODE   READINESS GATES
cpu-stress-test-588844b6f5-2426x   1/1     Running   0             19m     172.17.72.222   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-2lszj   1/1     Running   0             10m     172.17.72.207   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-f24jg   1/1     Running   0             15m     172.17.72.203   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-jjjcf   1/1     Running   0             5m10s   172.17.97.115   10.242.64.8    <none>           <none>
cpu-stress-test-588844b6f5-p69n8   1/1     Running   0             25m     172.17.72.236   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-sd7wh   1/1     Running   0             13s     172.17.97.78    10.242.64.8    <none>           <none>
cpu-stress-test-588844b6f5-tdrtk   1/1     Running   1 (13s ago)   30m     172.17.72.241   10.242.64.10   <none>           <none>`

`NAME           CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%   
10.242.64.10   1372m        35%    5332Mi          90%       
10.242.64.8    646m         16%    4421Mi          74%`

7. Scaling up
`NAME                               READY   STATUS    RESTARTS        AGE     IP              NODE           NOMINATED NODE   READINESS GATES
cpu-stress-test-588844b6f5-2426x   1/1     Running   0               24m     172.17.72.222   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-2lszj   1/1     Running   0               15m     172.17.72.207   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-6qxh6   1/1     Running   0               9s      172.17.97.112   10.242.64.8    <none>           <none>
cpu-stress-test-588844b6f5-f24jg   1/1     Running   0               20m     172.17.72.203   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-jjjcf   1/1     Running   0               10m     172.17.97.115   10.242.64.8    <none>           <none>
cpu-stress-test-588844b6f5-p69n8   1/1     Running   0               30m     172.17.72.236   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-sd7wh   1/1     Running   0               5m11s   172.17.97.78    10.242.64.8    <none>           <none>
cpu-stress-test-588844b6f5-tdrtk   1/1     Running   1 (5m11s ago)   35m     172.17.72.241   10.242.64.10   <none>           <none>`

`NAME           CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%   
10.242.64.10   1380m        35%    5358Mi          90%       
10.242.64.8    888m         22%    4448Mi          75% `

8. Scaling up
`cpu-stress-test-588844b6f5-2426x   1/1     Running   1 (7s ago)      30m     172.17.72.222   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-2lszj   1/1     Running   0               20m     172.17.72.207   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-4p76b   1/1     Running   0               9s      172.17.97.107   10.242.64.8    <none>           <none>
cpu-stress-test-588844b6f5-6qxh6   1/1     Running   0               5m27s   172.17.97.112   10.242.64.8    <none>           <none>
cpu-stress-test-588844b6f5-f24jg   1/1     Running   0               25m     172.17.72.203   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-jjjcf   1/1     Running   0               15m     172.17.97.115   10.242.64.8    <none>           <none>
cpu-stress-test-588844b6f5-p69n8   1/1     Running   1 (5m13s ago)   35m     172.17.72.236   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-sd7wh   1/1     Running   0               10m     172.17.97.78    10.242.64.8    <none>           <none>
cpu-stress-test-588844b6f5-tdrtk   1/1     Running   1 (10m ago)     40m     172.17.72.241   10.242.64.10   <none>           <none>`

`NAME           CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%   
10.242.64.10   1362m        34%    5324Mi          90%       
10.242.64.8    1037m        26%    4406Mi          74% `

9. Scaling up
`NAME                               READY   STATUS    RESTARTS        AGE     IP              NODE           NOMINATED NODE   READINESS GATES
cpu-stress-test-588844b6f5-2426x   1/1     Running   1 (4m57s ago)   35m     172.17.72.222   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-2lszj   1/1     Running   0               25m     172.17.72.207   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-2w4tl   1/1     Running   0               7s      172.17.97.82    10.242.64.8    <none>           <none>
cpu-stress-test-588844b6f5-4p76b   1/1     Running   0               4m59s   172.17.97.107   10.242.64.8    <none>           <none>
cpu-stress-test-588844b6f5-6qxh6   1/1     Running   0               10m     172.17.97.112   10.242.64.8    <none>           <none>
cpu-stress-test-588844b6f5-f24jg   1/1     Running   1 (15s ago)     30m     172.17.72.203   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-jjjcf   1/1     Running   0               20m     172.17.97.115   10.242.64.8    <none>           <none>
cpu-stress-test-588844b6f5-p69n8   1/1     Running   1 (10m ago)     40m     172.17.72.236   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-sd7wh   1/1     Running   0               15m     172.17.97.78    10.242.64.8    <none>           <none>
cpu-stress-test-588844b6f5-tdrtk   1/1     Running   1 (15m ago)     45m     172.17.72.241   10.242.64.10   <none>           <none>`

`NAME           CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%   
10.242.64.10   1388m        35%    5376Mi          91%       
10.242.64.8    1350m        34%    4437Mi          75% `

10. Scaling up
`NAME                               READY   STATUS    RESTARTS        AGE     IP              NODE           NOMINATED NODE   READINESS GATES
cpu-stress-test-588844b6f5-2426x   1/1     Running   1 (10m ago)     40m     172.17.72.222   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-2lszj   1/1     Running   1 (32s ago)     30m     172.17.72.207   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-2w4tl   1/1     Running   0               5m35s   172.17.97.82    10.242.64.8    <none>           <none>
cpu-stress-test-588844b6f5-4p76b   1/1     Running   0               10m     172.17.97.107   10.242.64.8    <none>           <none>
cpu-stress-test-588844b6f5-6qxh6   1/1     Running   0               15m     172.17.97.112   10.242.64.8    <none>           <none>
cpu-stress-test-588844b6f5-f24jg   1/1     Running   1 (5m43s ago)   35m     172.17.72.203   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-jjjcf   1/1     Running   0               25m     172.17.97.115   10.242.64.8    <none>           <none>
cpu-stress-test-588844b6f5-p69n8   1/1     Running   1 (15m ago)     45m     172.17.72.236   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-sd7wh   1/1     Running   0               20m     172.17.97.78    10.242.64.8    <none>           <none>
cpu-stress-test-588844b6f5-tdrtk   1/1     Running   1 (20m ago)     50m     172.17.72.241   10.242.64.10   <none>           <none>
cpu-stress-test-588844b6f5-xfrqv   0/1     Pending   0               4s      <none>          <none>         <none>           <none>`

