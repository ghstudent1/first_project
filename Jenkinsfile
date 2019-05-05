pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                 sh """
                    #!/bin/bash
                    virtualenv ./venv
                    touch flask.log
                    chmod 777 ./flask.log

                    ls -l /bin/sh
                    source ./venv/bin/activate
                    pip install -r ./requirement.txt
                    ./venv/bin/python3.6 ./flask_hello.py >> ./flask.log 2>&1 

                    """
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
