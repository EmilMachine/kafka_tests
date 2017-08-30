
# READ ME

source: 
https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask


# Test dummyhttpcallapp.py*

## before security
curl -i http://localhost:5000/todo/api/v1.0/tasks
curl -i http://localhost:5000/todo/api/v1.0/tasks/2
curl -i http://localhost:5000/todo/api/v1.0/tasks/3
curl -i -H "Content-Type: application/json" -X PUT -d '{"done":true}' http://localhost:5000/todo/api/v1.0/tasks/2

## after security
curl -u rule:gen -i http://localhost:5000/todo/api/v1.0/tasks

USE BROWSER INSTEAD

test error:
curl -u rule:gen -i http://localhost:5000/ruleGen/api/v1.0/rulesdfdaf/3
# TEST rulegentapp.py
curl -u rule:gen -i http://localhost:5000/ruleGen/api/v1.0/rules/[{"sepal length (cm)":"5.1","sepal width (cm)":"3.5","petal length (cm)":"1.4","petal width (cm)":"0.2","target":"0.0"},{"sepal length (cm)":"4.9","sepal width (cm)":"3.0","petal length (cm)":"1.4","petal width (cm)":"0.2","target":"0.0"},{"sepal length (cm)":"4.7","sepal width (cm)":"3.2","petal length (cm)":"1.3","petal width (cm)":"0.2","target":"0.0"},{"sepal length (cm)":"4.6","sepal width (cm)":"3.1","petal length (cm)":"1.5","petal width (cm)":"0.2","target":"0.0"},{"sepal length (cm)":"5.0","sepal width (cm)":"3.6","petal length (cm)":"1.4","petal width (cm)":"0.2","target":"0.0"},{"sepal length (cm)":"5.4","sepal width (cm)":"3.9","petal length (cm)":"1.7","petal width (cm)":"0.4","target":"0.0"},{"sepal length (cm)":"4.6","sepal width (cm)":"3.4","petal length (cm)":"1.4","petal width (cm)":"0.3","target":"0.0"},{"sepal length (cm)":"5.0","sepal width (cm)":"3.4","petal length (cm)":"1.5","petal width (cm)":"0.2","target":"1.0"},{"sepal length (cm)":"4.4","sepal width (cm)":"2.9","petal length (cm)":"1.4","petal width (cm)":"0.2","target":"1.0"},{"sepal length (cm)":"4.9","sepal width (cm)":"3.1","petal length (cm)":"1.5","petal width (cm)":"0.1","target":"1.0"},{"sepal length (cm)":"5.4","sepal width (cm)":"3.7","petal length (cm)":"1.5","petal width (cm)":"0.2","target":"1.0"},{"sepal length (cm)":"4.8","sepal width (cm)":"3.4","petal length (cm)":"1.6","petal width (cm)":"0.2","target":"1.0"},{"sepal length (cm)":"4.8","sepal width (cm)":"3.0","petal length (cm)":"1.4","petal width (cm)":"0.1","target":"1.0"},{"sepal length (cm)":"4.3","sepal width (cm)":"3.0","petal length (cm)":"1.1","petal width (cm)":"0.1","target":"0.0"}]
