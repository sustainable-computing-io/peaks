felix@Felixs-MacBook-Pro workload_generator % python peaks_workload_gen.py 
2024-01-04 13:24:17.467044 : Client created
2024-01-04 13:24:22.871801 : Deployment created. Status='cpu-stress-test'
2024-01-04 13:29:26.435408 : Deployment scaled. Status='cpu-stress-test'
2024-01-04 13:34:28.354716 : Deployment scaled. Status='cpu-stress-test'
2024-01-04 13:39:34.451707 : Deployment scaled. Status='cpu-stress-test'
2024-01-04 13:44:36.785665 : Deployment scaled. Status='cpu-stress-test'
2024-01-04 13:49:38.411480 : Deployment scaled. Status='cpu-stress-test'
2024-01-04 13:54:40.405951 : Deployment scaled. Status='cpu-stress-test'
2024-01-04 13:59:42.206460 : Deployment scaled. Status='cpu-stress-test'
2024-01-04 14:04:44.329049 : Deployment scaled. Status='cpu-stress-test'
2024-01-04 14:09:46.087871 : Deployment scaled. Status='cpu-stress-test'
2024-01-04 14:14:47.956580 : Deployment scaled. Status='cpu-stress-test'
Exception :  (401)
Reason: Unauthorized
HTTP response headers: HTTPHeaderDict({'Audit-Id': '789b815c-4c85-4511-8228-9e8b03fb07bb', 'Cache-Control': 'no-cache, private', 'Content-Type': 'application/json', 'Date': 'Thu, 04 Jan 2024 08:49:49 GMT', 'Content-Length': '129'})
HTTP response body: {"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"Unauthorized","reason":"Unauthorized","code":401}


/Users/felix/Library/Python/3.9/lib/python/site-packages/urllib3/connectionpool.py:1045: InsecureRequestWarning: Unverified HTTPS request is being made to host 'iam.cloud.ibm.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
  warnings.warn(
2024-01-04 14:19:54.693020 : Deployment cpu-stress-test deleted.
2024-01-04 14:19:54.693164 : Default Experiment completed
2024-01-04 14:24:57.170593 : Deployment created. Status='cpu-stress-test'
2024-01-04 14:29:59.153546 : Deployment scaled. Status='cpu-stress-test'
2024-01-04 14:35:01.122091 : Deployment scaled. Status='cpu-stress-test'
2024-01-04 14:40:03.104901 : Deployment scaled. Status='cpu-stress-test'
2024-01-04 14:45:05.046825 : Deployment scaled. Status='cpu-stress-test'
2024-01-04 14:50:06.762425 : Deployment scaled. Status='cpu-stress-test'
2024-01-04 14:55:08.952971 : Deployment scaled. Status='cpu-stress-test'
2024-01-04 15:00:10.786981 : Deployment scaled. Status='cpu-stress-test'
2024-01-04 15:05:12.926371 : Deployment scaled. Status='cpu-stress-test'
2024-01-04 15:10:14.944499 : Deployment scaled. Status='cpu-stress-test'
2024-01-04 15:15:16.976813 : Deployment scaled. Status='cpu-stress-test'
Exception :  (401)
Reason: Unauthorized
HTTP response headers: HTTPHeaderDict({'Audit-Id': 'e96890e3-05f2-42e0-8713-5773cc2e3f38', 'Cache-Control': 'no-cache, private', 'Content-Type': 'application/json', 'Date': 'Thu, 04 Jan 2024 09:50:18 GMT', 'Content-Length': '129'})
HTTP response body: {"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"Unauthorized","reason":"Unauthorized","code":401}


/Users/felix/Library/Python/3.9/lib/python/site-packages/urllib3/connectionpool.py:1045: InsecureRequestWarning: Unverified HTTPS request is being made to host 'iam.cloud.ibm.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
  warnings.warn(
2024-01-04 15:20:24.389539 : Deployment cpu-stress-test deleted.
2024-01-04 15:20:24.389670 : Peaks Experiment completed
