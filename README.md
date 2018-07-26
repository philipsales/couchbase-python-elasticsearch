# Coucbase to ElasticSearch data pipeline

Bare data pipepline 

## Getting Started

- [x] MacOS based machine. 
- [ ] Linux based machine --TODO. 

### Prerequisites

1. Use python > 3.6

2. Add python to path

3. Install libraries
```
brew update # get list of latest packages
brew install libcouchbase
brew install python
pip install couchbase
```

4. Install python environment manager 
```
python3 -m pip install virtualenv
```

### Running the Program

1. Create a specific python version for virtual environment 
```
virtualenv --python=<path_to>/python3.6 <virtaul_env_folder_name> 
```

2. Activate virtual environment 
```
source <path>/bin/activate 
```

3. Rename the file settings/config.template.py to template.py

4. Build the project
```
python setup.py install 
```

5. Run program 
```
python ./main.py
```

## Running the tests

TODO

## Deployment

TODO

## Built With

None

## Contributing

None

## Versioning

0.0.1

## Authors

* **Philip Sales** 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Open Source Community 

