# s1-example

A simple algorithm to test methods of data access from ASF DAAC. Specifically Sentinel-1 data, in anticipation of NISAR access being similar.


## Registering the algorithm

```
Repository URL = https://github.com/MAAP-Project/s1-example.git
Repository Branch = main
Run Command = s1-example/run.sh
Build Command = s1-example/build.sh
Algorithm Name = ASFDAACS3Test
Description = Test S3 Access from ASF
Disk Space (GB) = 10
Resource Allocation = maap-dps-worker-8gb
Container URL = mas.maap-project.org/root/maap-workspaces/base_images/vanilla:v3.1.3
```

## Running the algorithm
Put your username when running a job

```
maap.submitJob(identifier="first",
    algo_id="ASFDAACS3Test",
    version="main",
    username="<null>",
    queue="maap-dps-worker-8gb",
    )
```
