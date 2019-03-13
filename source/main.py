import os
from jenkins import collector
from serialize import logger

def main():
    # this values are required. So need to do try/catch to notify missing values.
    JENKINS_URL = os.environ.get('JENKINS_URL')
    USERNAME = os.environ.get('JENKINS_USR') 
    PASSWORD = os.environ.get('JENKINS_PSW') 

    # initialize the logger configuration
    logger.init()

    # Server is an instance of jenkins servers.
    server = collector.getServerInstance(JENKINS_URL, USERNAME, PASSWORD)
    if server != None:
        collector.getJobDetails(server)

if __name__ == '__main__':
    main()
