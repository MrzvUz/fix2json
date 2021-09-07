A. Python3.6 installation on Linux:

1. Run as a root user:
$ sudo -i
$ yum -y update && yum -y upgrade

2. Prior to installing Python in CentOS 7, let’s make sure our system has all the necessary development dependencies:
$ yum -y groupinstall development
$ yum -y install zlib-devel

3. To install Python 3.6, run the following commands:
$ wget https://www.python.org/ftp/python/3.6.3/Python-3.6.3.tar.xz
$ tar xJf Python-3.6.3.tar.xz
$ cd Python-3.6.3
$ ./configure
$ make
$ make install

4. Use which to verify the location of the main binary and python3 -V to verify the python3 version:
$ which python3
$ python3 -V



B. Building Quickfix1.15.1 library:

1. Run as a root user:
$ sudo -i


2. Install necessary tools:
$ yum -y install git wget make


3. Download the tar file and extract it:
$ wget http://prdownloads.sourceforge.net/quickfix/quickfix-1.15.1.tar.gz
$ tar -xvf quickfix-1.15.1.tar.gz

4. Change the directory to quickfix which has been extracted:
$ cd quickfix

5. In quickfix directory run following commands:
$ ./configure --enable-static
$ make








Depending on the user's need there are three solutions presented here.

    1. Marked-up XML
    2. List of fields (groups embedded).
    3. JSON-like output.

In the quickfix Python library, the FieldMap field and group key iterators are not exposed. So the approach is to first generate the XML and iterate over the tree. There is also no access to the getFieldType method of the DataDictionary, so the dictionary must be pre-processed to store the field types for conversion and handling of groups.

RUN from fix2json-py-v2 folder:
╰─ $./fix2json.py --spec spec/FIX44.xml
