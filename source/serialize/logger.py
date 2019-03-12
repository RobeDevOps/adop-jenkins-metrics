import logging
import os

def init():
    # Create the logger name with Jenkins
    logger = logging.getLogger('jenkins')
    logger.setLevel(logging.DEBUG)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.INFO)

    # create info format schema. This format is reused by console and file handlers.
    infoFormat = logging.Formatter("%(asctime)s - %(levelname)s - [jenkins] %(job_name)s %(last_buildnumber)s %(last_good_buildnumber)s %(last_failed_buildnumber)s")
    consoleHandler.setFormatter(infoFormat)

    # Create the FileHandler
    infoFileHandler = logging.FileHandler("/var/log/jenkins.log")
    infoFileHandler.setLevel(logging.INFO)
    infoFileHandler.setFormatter(infoFormat)
    
    # Adding all the handlers to the logger
    logger.addHandler(consoleHandler)
    logger.addHandler(infoFileHandler)
