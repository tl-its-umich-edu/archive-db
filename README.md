## archive_db.py

This small Python application allows the user to connect to a MySQL database and write the data from each table to a CSV file. The application writes all of the resulting files to an `archive` directory named using the database's name and host, as well as the date and time the application was run.

### Installation

To successfully set up the application, you may need to install some or all of the following:
* Python 3 (the application was written and tested using version 3.7.5)
* [Git](https://git-scm.com/)
* [`virtualenv`](https://virtualenv.pypa.io/en/latest/)

When the prerequisites are satisfied, perform the actions below in order. 

1. Clone the repository and navigate into it.
    ```
    https://github.com/tl-its-umich-edu/archive-db.git   # HTTPS
    git@github.com:tl-its-umich-edu/archive-db.git       # SSH
    
    cd archive-db
    ```

1. Create and activate a virtual environment using `virtualenv`.
   ```
   virtualenv venv

   source venv/bin/activate   # for Mac OS
   venv\Scripts\activate      # for Windows
   ```

1. Install the dependencies.

    If you are using Mac OS, install the dependencies like so:
    ```
    pip install -r requirements.txt
    ```

    If you are using Windows, you will need to follow a different process for installing `mysqlclient`.

    * Go to [Unofficial Windows Binaries for Python Extension Packages](https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient) and search for "mysqlclient-1.4.6" and find the `.whl` download corresponding to your type of processor (32 or 64).

    * Within the virtual environment, issue the following command, where `[path]` is an absolute path to the wheel:
        ```
        pip install [path]
        ```

    * Then, install the other dependencies using `pip install -r requirements.txt`.

### Configuration

Prior to running the application, you will need to create a configuration file called `env.json`. 

1. In the `config` directory of the repository, you will find a template file called `env_blank.json`. 
Copy and rename the file `env.json` using a text editor, file utility, or terminal.

1. Next, add the desired settings for the application. 
    
    1. Replace the provided `LOG_LEVEL` value with the minimum level for log messages you want to appear in output. `INFO` or `DEBUG` is recommended for most use cases; see Python's [logging](https://docs.python.org/3/library/logging.html) module.

    1. Under `MYSQL_DATABASE`, replace the empty strings and `0` with the parameters for the database you wish to connect to.


### Usage

To the run the application, simply execute `archive_db.py` within the activated virtual environment.

```
python archive_db.py
```

The CSV files, each named according to the table name, will be in an `archive-` subdirectory under `data`.
