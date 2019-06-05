

# AWH Data pipeline - Source Code Installation
Bare data pipepline 


## Tested Environment
- [x] MacOS based machine - Local.
- [x] Linux based machine - Production. 
- [ ] Windows based machine. 


## System Dependencies
```
| Dependencies | Versions |
| ------------ | -------- |
| Python       | 3.6.2    |
| Virtualenv   | 15.1.0   |
```

## Application Dependencies
Listed in requirements.txt
```
| Python pck    | Versions |
| ------------  | -------- |
| couchbase     | 2.4.0    |
| elasticsearch | 6.2.0    |
| urllib3       | 1.22     |
| requests      | 2.19.1   |
```

### System Dependencies Installation - Python (Linux)
1. Open command line terminal
1. Access the cloud server using the provided username and password
    ```
    ssh <username>@<ip_address>
    ```
1. Update OS packages and install python dependencies (e.g Python > 3.6)
    ```
    sudo apt-get update \
        && apt-get install -y software-properties-common curl \
        && add-apt-repository ppa:deadsnakes/ppa \
        && apt-get update \
        && apt-get install -y python3.6 python3.6-venv
    ```
1. Download specific python version (e.g Python > 3.6)
    ```
    wget http://www.python.org/ftp/python/3.6.0/Python-3.6.0.tgz
    tar xzvf Python-3.6.0.tgz
    cd Python-3.6.0/
    ./configure
    make
    sudo make install
    ```
    
### System Dependencies Installation - Python Virtual Environment
1. Install python virtual environment manager (i.e. virtualenv)
    ```
    python3 -m pip install virtualenv
    ```
1. Create a virtual environment folder name (e.g. awhdatapipeline) 
    ```
    virtualenv --python=<path>/python3.6 awhdatapipepline
    ```
    
#### Python Dependency Installation - Python-couchbase
1. Install couchbase-python library
    ```
    wget http://packages.couchbase.com/releases/couchbase-release/couchbase-release-1.0-4-amd64.deb
    sudo dpkg -i couchbase-release-1.0-4-amd64.deb
    sudo apt-get -y update 
    sudo apt-get -y install libcouchbase-dev libcouchbase2-bin build-essential
    ```
  
#### Application Installation - Source Code
1. Go to the root directory of the cloud sever 
    ```
    cd ~
    ```
1. Create source code folder
    ```
    mkdir src
    ```
1. Download the source code from the repository using your credentials
    ```
    cd ~/src
    git clone https://<your_username>@bitbucket.org/teamidiah/data-pipeline.git data-pipeline
    ```

## Application Configuration
1. Go to the source code settings (i.e. ~src/data-pipeline/settings)
1. Change the connection configurations as appropriate for the following:
- couchbase_conf.py
- elastic_conf.py
- kobo_conf.py
- sqlite_conf.py

## Automated Deployment - Cron Job
1. Run the deployment script (i.e. located in deployment/etl.sh directory)
    ``` 
    cd ~/src/data-pipeline/deployment
    sudo chmod u+x etl.sh
    ./etl.sh
    ```

## Manual Deployment sript (optional)
1. Run the following script
    ```
    cd /virtualenv/awhdatapipeline
    source bin/activate
    cd ~src/data-pipeline
    python main.py
    wait
    deactivate
    ```

## Built With

[x] Python

## Contributing
None
## Versioning
1.0.0
## Authors
* **Philip Sales** 
* **Rosette Tienzo** 
## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Open Source Community 

