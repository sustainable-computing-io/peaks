Designing an evaluation to compare the SLA of the default Kubernetes scheduler against your Peaks scheduler plugin involves several steps, including defining metrics, creating test scenarios, and analyzing results. Here’s a structured approach:
1. Define Key Metrics

    Scheduling Time: Measure the time taken by each scheduler to schedule pods.
    Latency Under Load: Assess the response time of applications when subjected to load tests. This includes:
        Average latency
        Peak latency
        99th percentile latency
    Resource Utilization: Monitor CPU and memory usage during the scheduling and load tests.

2. Set Up Your Testing Environment

    Kubernetes Cluster: Create a test environment with a Kubernetes cluster (can be on a local setup or a cloud provider).
    Applications: Deploy applications that will be tested. Consider using stateful and stateless applications for diversity.
    Load Testing Tool: Choose a tool for load testing, such as Apache JMeter, Locust, or k6.

3. Test Scenarios

    Scenario 1: Basic Scheduling Time Comparison
        Deploy a set number of pods with both schedulers (default and Peaks).
        Measure the time taken for each pod to be scheduled.
        Record metrics like average scheduling time and standard deviation.

    Scenario 2: Scheduling Under Load
        Simulate a load on the application while scheduling pods. For instance, start scheduling new pods as the load increases.
        Measure the scheduling time again and observe any differences in performance.

    Scenario 3: Load Testing Application
        Once the application is running, apply a load test to measure how both schedulers perform under stress.
        Measure latency and other performance metrics during this phase.

4. Data Collection

    Use Kubernetes metrics (such as kubectl top) and logging to collect data on scheduling times and resource utilization.
    Use the load testing tool to capture latency metrics.

5. Analyze Results

    Compare Scheduling Times:
        Calculate average scheduling times for both schedulers.
        Analyze the impact of Peaks on scheduling under various conditions.
    Evaluate Latency Results:
        Compare average, peak, and 99th percentile latencies for applications under load.
        Assess how scheduling impacts application performance and response times.

6. Reporting

    Summarize findings in a clear report, highlighting:
        Average scheduling times
        Latency under load scenarios
        Resource utilization patterns
        Any other relevant observations (e.g., failure rates, responsiveness)