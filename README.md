# Software Engineering Apprenticeship


```
If you don’t have a current code sample you can share, please write a small web application in one of the above languages (Python/Ruby/Node). The application only needs to do the following:
Accept a POST request to the route “/test”, which accepts one argument “string_to_cut”
Return a JSON object with the key “return_string” and a string containing every third letter from the original string
(e.g.) If you POST {"string_to_cut": "iamyourlyftdriver"}, it will return: {"return_string": "muydv"}.

Note: To see expected behavior you can test against a current working example with the command: curl -X POST https://lyft-interview-test.glitch.me/test --data '{"string_to_cut": "iamyourlyftdriver"}' -H 'Content-Type: application/json'
```


## Flask Installation

Note:
If you are using Python3 than you don't have to install virtual environment because it already come with venv module to create virtual environments.
If you are using Python 2, the venv module is not available. Instead, install virtualenv.

If you are on Mac OS X download get-pip.py:
```shell
 sudo easy_install pip
```
 Install Virtual Environment
```shell
sudo pip install virtualenv
```
 Now we will create a virtualenv
```shell
sudo virtualenv [venv name]
```
 If you list the contents of the [venv name] directory, you will see that it has created several sub-directories, including a bin folder (Scripts on Windows) that contains copies of both Python and pip. The next step is to activate your new virtualenv.
and install Flask 
```shell
source [venv name]/bin/activate
sudo pip install Flask
```
 Finally, install lyfttest app by running the following command from the root directory of project
```shell
pip install
```

Exporting the Flask_APP environment variable
```shell
export FLASK_APP=lyfttest
export FLASK_DEBUG=true
flask run
```

Test the application 
```shell
curl -X POST http://localhost:5000/test --data '{"string_to_cut": "iamyourlyftdriver"}' -H 'Content-Type: application/json'
```

#Assumptions:
If there are white spaces leading, trailing or middle of the string, then my code will remove all the whitespaces.
eg: 
1. "string_to_cut": "    iamyourlyftdriver"
2. "string_to_cut": "iamyourlyftdriver    "
3. "string_to_cut": "iamyour    lyftdriver"
 
In all the three scenarios  above the result would be "muydv".

4. "string_to_cut":  " &nbsp; &nbsp;  "

The output for this scenario would be ""
