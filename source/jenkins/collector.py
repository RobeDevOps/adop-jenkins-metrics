from jenkinsapi.api import Jenkins
from jenkinsapi.custom_exceptions import NoBuildData
import logging
import os
import sys

logger = logging.getLogger('jenkins')

# return a jenkins instance 
# parameters:
#   - jenkins_url: follow the schema http://server_ip/jenkins
#   - username and password used when adop was created.
def getServerInstance(jenkins_url, jenkins_usr, jenkins_psw):
    try:
        server = Jenkins(jenkins_url, username=jenkins_usr, password=jenkins_psw)
        return server
    except:
        # TODO using logger with filter for error messages
        print("Server unavailable or credentials errors")
        return None

# Last build number can be Success or Failure
def getLastBuildNumber(job_instance):
    last_build = 0
    try:
        last_build = job_instance.get_last_buildnumber()
    except NoBuildData as no_build:
        last_build 
    return last_build

# Last good build number can be old number
def getLastGoodBuidNumber(job_instance):
    last_good_build_number = 0
    try:
        last_good_build_number = job_instance.get_last_good_buildnumber()
    except NoBuildData as no_build:
        last_good_build_number 
    return last_good_build_number

# Last failure number can be old number
def getLastFailedBuildNumber(job_instance):
    last_failed_build_number = 0
    try:
        last_failed_build_number = job_instance.get_last_failed_buildnumber()
    except NoBuildData as no_build:
        last_failed_build_number 
    return last_failed_build_number
   

def getJobDetails(server):

    job_collector = set([])
    for job_name, job_instance in server.get_jobs():
        job_full_name = job_instance.get_full_name()
        if job_full_name in job_collector:
            continue
        else:
            job_collector.add( job_full_name )
            logger.info("", extra={
                'job_name': job_full_name, 
                'last_buildnumber': getLastBuildNumber(job_instance),
                'last_good_buildnumber': getLastGoodBuidNumber(job_instance),
                'last_failed_buildnumber': getLastFailedBuildNumber(job_instance),
            })
