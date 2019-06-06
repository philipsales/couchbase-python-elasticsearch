

# AWH Data pipeline - Source Code Installation #
Bare data pipepline 


## Tested Environment ##
- [x] MacOS based machine - Local.
- [x] Linux based machine - Production. 
- [ ] Windows based machine. 


## System Dependencies ##

| Dependencies | Versions |
| ------------ | -------- |
| Ubuntu       | 16.04    |
| Python       | 3.6.2    |
| Virtualenv   | 15.1.0   |

### System Dependencies Installation - Python (Linux) ###

1. Open command line terminal
1. Access the cloud server using the provided username and password. Use your VPN credentials to access the server

    ```
    ssh <username>@<ip_address>
    ```

1. Update OS packages and install python dependencies (e.g Python > 3.6)

    ```
    sudo apt-get update \
        && apt-get install -y software-properties-common curl \
        && add-apt-repository ppa:deadsnakes/ppa \
        && apt-get update 
        # && apt-get install -y python3.6 python3.6-venv 
    ```
1. Install compiler, compressor, builder, ssl libraries
    ```
    sudo apt-get install -y build-essential checkinstall 
    sudo apt-get install -y zlib1g-dev
    sudo apt-get install -y libc6-dev libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libbz2-dev
    ```
1. Create library for external libraries
   ```
   mkdir ~/lib
   ```
1. Download specific python version (e.g Python > 3.6)

    ```
    cd ~/lib
    wget http://www.python.org/ftp/python/3.6.2/Python-3.6.2.tgz
    tar xzvf Python-3.6.2.tgz
    cd Python-3.6.2
    ./configure --with-zlib=/usr/include
    make
    sudo make install
    ```
    
### System Dependencies Installation - Python Virtual Environment ###

1. Install python virtual environment manager (i.e. virtualenv)

    ```
    sudo apt-get install -y python3-pip
    #sudo apt-get install -y python3.6 python3.6-venv
    # sudo apt-get install -y python3.6.2-venv
    sudo apt-get install -y python-virtualenv
    python3 -m venv
    ```

1. Create a virtual environment folder name (e.g. awhdatapipeline) 

    ```
    mkdir ~/virtual_env
    cd ~/virtual_env
    #python3 -m venv awhdatapipeline
    virtualenv --python=<path>/python3.6 awhdatapipepline_env
    ```
    

## Application Dependencies ##
Listed in requirements.txt

| Library    | Versions |
| ------------  | -------- |
| python couchbase     | 2.4.0    |
| python elasticsearch | 6.2.0    |
| sqlite        | 3.17.0   |
| urllib3       | 1.22     |
| requests      | 2.19.1   |

#### Application Installation - Source Code ####
1. Go to the root directory of the cloud server 

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


#### Application Installation - SQLite ####
1. Install sqlite

    ```
    sudo add-apt-repository ppa:jonathonf/backports
    sudo apt-get -y update 
    sudo apt-get install -y sqlite3
    ```
    
#### Application Installation - Python-couchbase library ####
1. Install couchbase-python library

    ```
    cd ~/lib
    wget http://packages.couchbase.com/releases/couchbase-release/couchbase-release-1.0-4-amd64.deb
    sudo dpkg -i couchbase-release-1.0-4-amd64.deb
    sudo apt-get -y update 
    sudo apt-get -y install libcouchbase-dev libcouchbase2-bin build-essential
    ```

#### Application Installation - Other Python libraries ####

    
1. Activate python virtual environment

    ```
    source ~/awhdatapipeline_env/bin/activate
    ```
    
1. Go to the root directory of the cloud sever 

    ```
    cd ~/src/data-pipeline
    ```
    
1. Install application dependencies
    ```
    pip install --upgrade pip
    pip3 install requirements.txt
    ```
   
1. Deactivate virtual environment 
   ```
   deactivate
   ```

## Application Configuration ##
1. Go to the source code settings (i.e. ~src/data-pipeline/settings)
1. Change the connection configurations as appropriate for the following:
    - couchbase_conf.py
    - elastic_conf.py
    - kobo_conf.py
    - sqlite_conf.py

## Automated Deployment - Cron Job ##
1. Run the deployment script (i.e. located in deployment/etl.sh directory)
    ``` 
    cd ~/src/data-pipeline/deployment
    sudo chmod u+x etl.sh
    ./etl.sh
    ```

## Manual Deployment sript (optional) ##
1. Run the following script
    ```
    cd /virtualenv/awhdatapipeline_env
    source bin/activate
    cd ~src/data-pipeline
    python main.py
    wait
    deactivate
    ```

## Built With ##

[x] Python

## Contributing ##
None
## Versioning ##
1.0.0
## Authors ##
* **Philip Sales** 
* **Rosette Tienzo** 
## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments ##

* Open Source Community 

