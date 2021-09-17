# Set up required environment to install Python QuickFix Library and develop your own custom QuickFix Python Library.

I am going to be using Linux CentOS 7 for this demo.

    a. Install Python.
    
        1. Update your OS or you can update and upgrade at the same time:

            sudo yum -y update && sudo yum -y upgrade
        
        2. Install below pre-requisites for Python and Python Quickfix library:

            sudo yum -y install wget make gcc gcc-c++ glibc-devel openssl-devel bzip2-devel

        3. Download Python 3.9.7 setup in /tmp location and unzip tgz file:

            cd /tmp/
            wget https://www.python.org/ftp/python/3.9.7/Python-3.9.7.tgz            
            tar xzf Python-3.9.7.tgz

        4. Install Python 3.9.7 with alternate installation.

            cd Python-3.9.7
            ./configure --enable-optimizations            
            sudo make altinstall

        5. Set currently installed Python 3.9.7 as a default Linux Python version:

            sudo ln -sfn /usr/local/bin/python3.9 /usr/bin/python3.9
            sudo ln -sfn /usr/local/bin/pip3.9 /usr/bin/pip3.9

        6. Verify new Python 3.9.7 and PIP version:

            python3.9 -V
            pip3.9 -V



















Depending on the user's need there are three solutions presented here.

    1. Marked-up XML
    2. List of fields (groups embedded).
    3. JSON-like output.

In the quickfix Python library, the FieldMap field and group key iterators are not exposed. So the approach is to first generate the XML and iterate over the tree. There is also no access to the getFieldType method of the DataDictionary, so the dictionary must be pre-processed to store the field types for conversion and handling of groups.

RUN from fix2json-py-v2 folder:
╰─ $./fix2json.py --spec spec/FIX44.xml
