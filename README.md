## Python-Pytest-Selenium
[![Travis Status](https://travis-ci.org/saucelabs-sample-test-frameworks/Python-Pytest-Selenium.svg?branch=master)](https://travis-ci.org/saucelabs-sample-test-frameworks/Python-Pytest-Selenium)

This code is meant for actual py.test users with aspirations beyond running unittest style tests using py.test.
It demonstrates the use of py.test fixtures in conjunction with Selenium and SauceLabs.

This code is provided on an "AS-IS” basis without warranty of any kind, either express or implied, including without limitation any implied warranties of condition, uninterrupted use, merchantability, fitness for a particular purpose, or non-infringement. Your tests and testing environments may require you to modify this framework. Issues regarding this framework should be submitted through GitHub. For questions regarding Sauce Labs integration, please see the Sauce Labs documentation at https://wiki.saucelabs.com/. This framework is not maintained by Sauce Labs Support.

### Environment Setup

1. Global Dependencies
    * [Install Python](https://www.python.org/downloads/)
    * Or Install Python with [Homebrew](http://brew.sh/)
    ```
    $ brew install python
    ```
    * Install [pip](https://pip.pypa.io/en/stable/installing/) for package installation

2. Sauce Credentials
    * In the terminal export your Sauce Labs Credentials as environmental variables:
    ```
    $ export SAUCE_USERNAME=<your Sauce Labs username>
	$ export SAUCE_ACCESS_KEY=<your Sauce Labs access key>
    ```
3. Project
	* The recommended way to run your tests would be in [virtualenv](https://virtualenv.readthedocs.org/en/latest/). It will isolate the build from other setups you may have running and ensure that the tests run with the specified versions of the modules specified in the requirements.txt file.
	```$ pip install virtualenv```
	* Create a virtual environment in your project folder the environment name is arbitrary.
	```$ virtualenv venv```
	* Activate the environment:
	```$ source venv/bin/activate```
	* Install the required packages:
	```$ pip install -r requirements.txt```

### Running Tests:  -n option designates number of parallel tests and -s to disable output capture.

*  Tests in Parallel:
    ```$ py.test -s -n 2 tests```

* Dump session ids for the SauceLabs CI plugins:
    ```$ cat $(find . -name "*.testlog")```


[Sauce Labs Dashboard](https://saucelabs.com/beta/dashboard/)

### Advice/Troubleshooting

There may be additional latency when using a remote webdriver to run tests on Sauce Labs. Timeouts or Waits may need to be increased.
    * [Selenium tips regarding explicit waits](https://wiki.saucelabs.com/display/DOCS/Best+Practice%3A+Use+Explicit+Waits)

### Resources
##### [Sauce Labs Documentation](https://wiki.saucelabs.com/)

##### [Selenium Documentation](http://www.seleniumhq.org/docs/)

##### [Python Documentation](https://docs.python.org/2.7/)

##### [Pytest Documentation](http://pytest.org/latest/contents.html)

##### [Stack Overflow](http://stackoverflow.com/)
* A great resource to search for issues not explicitly covered by documentation.

### Known Issues:
* Test output will be captured in .testlog files as the pytest-xdist plugin has issues with not capturing stdout and stderr. You can use the following commands to output session id's for CI integration and clean up.
```
$ cat *.testlog
$ rm -rf *.testlog
```
