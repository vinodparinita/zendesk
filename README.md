# Zendesk Coding Challenge
This repo contains answers to Zendesk Coding Challenge


## Getting Started
---------------

### Requirements
This source code requires below installations of:

1. Python3
2. Pip3


### Installation
Also, install the prerequisite python packages for the python code to run using pip
```bash
pip3 install -r requirements.txt
```

*Attention!*
### Configuration
Kindly edit the configuration based on requirements which contains Zendesk subdomain
```bash
vi src/config.json
```


### Unit test
To execute the unit tests, run using below commands:

```bash
cd test
python3 zendeskAPITestCase.py -u <EMAIL ID> -t <API TOKEN>
```


### Basic Commands
This python code can be run by using below commands:

```bash
python3 zendeskTicketViewer.py -u <EMAIL ID> -t <API TOKEN>
```

For quick help
```bash
python3 zendeskTicketViewer.py -h
```

