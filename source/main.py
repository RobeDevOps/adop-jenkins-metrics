import os
from jenkins import collector
from serialize import logger

def main():
    # this values are required. So need to do try/catch to notify missing values.
    JENKINS_URL = os.environ.get('JENKINS_URL')
    USERNAME = os.environ.get('JENKINS_USR') 
    PASSWORD = os.environ.get('JENKINS_PSW') 

    # mocking values. These values are gone when code is running inside the container
    JENKINS_URL = 'http://34.230.85.167/jenkins'
    USERNAME = 'devops'
    PASSWORD = '12345qwert'

    # initialize the logger configuration
    logger.init()
   
    server = collector.getServerInstance(JENKINS_URL, USERNAME, PASSWORD)
    collector.getJobDetails(server)


if __name__ == '__main__':
    main()
