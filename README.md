# Machine_Learning1
My first machine learning project.

### Softwere and account requirement
1. [Github_Account] ()
2. [Heroku_Account]()
3. [Git CLI]()

Creating conda environment

# To ignore the file or folder from git we can write name of file/folder in .gitignore file

# conda create -p venv python==3.7 -y  (for create virtual environment and y for yes)
# to check the the git status==> git status
# to add the file==> git add <file name>

 To check all version maintained by git
 ```
 git log
 ``` 

To create version/commit all changes by git
```
git commit -m "message"
```

To send version/changes to github==> git push origin main

To check remote url
```
git remote -v
```

Heroku deployement requirements:
1. HEROKU_EMAIL :
2. HEROKU_API_KEY: 
3. HEROKU_APP_NAME: ml-regression-app

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```

>Note: Image name for docker must be lowercase
