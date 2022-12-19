# VedaAPI E2E test

This project contain VedaAPI e2e tests


# Prerequisites
- Python 3
- [Install Gauge](https://docs.gauge.org/latest/installation.html)
- [Install Gauge-Python plugin](https://gauge-python.readthedocs.io/en/latest/installation.html) by running<br>
```
gauge install python
[pip / pip3] install getgauge
```
- Google Chrome


# Executing specs

## Mac M1 architecture
- You will need to run Gauge command with the `arch -x86_64`. For example: `arch -x86_64 gauge run specs/`
- To be able to run the  arch -x86_64 you will need to change the Python version in the Gauge runner.
To do that, you will need to edit the file `/Users/alexsouza/.gauge/plugins/python/0.3.17/start.sh` and set `GAUGE_PYTHON_COMMAND="/Library/Developer/CommandLineTools/usr/bin/python3"`
- Run pip from your python installation in the system. For example: `arch -x86_64 /Library/Developer/CommandLineTools/usr/bin/python3 -m pip install -r requirements.txt`
 

### Set up
This project requires pip to install dependencies. To install dependencies run :  
````
pip install -r requirements.txt
````

### All specs
````
gauge run specs
````
This will also compile all the supporting code implementations.

### Docker
- `docker build -t veda/gauge .`
- `docker run -it --rm -v $(pwd):/app veda/gauge gauge run specs`
