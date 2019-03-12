FROM docker.elastic.co/beats/filebeat:6.4.3

LABEL MAINTAINER="roberto cardenas <rcardenas20@gmail.com>"

USER root
RUN yum --enablerepo=extras install epel-release -y && \
    yum update -y && \
    yum install python34 python34-pip -y && \
    pip3 install --upgrade pip && \
    yum clean all && \
    rm -rf /var/cache/yum

ENV FILEBEAT_HOME /usr/share/filebeat
ENV APPLICATION_HOME /opt/jenkins_collector
ENV PERIOD 30s
COPY ./filebeat/filebeat.yml ${FILEBEAT_HOME}/filebeat.yml
ADD ./source ${APPLICATION_HOME}
RUN pip3 install -r ${APPLICATION_HOME}/requirements.txt && \
ADD entrypoint.sh /entrypoint.sh
RUN chown filebeat:filebeat ${FILEBEAT_HOME}/filebeat.yml && \
    chown -R filebeat:filebeat ${APPLICATION_HOME} && \
    chown filebeat:filebeat /entrypoint.sh && \
    chmod go-w /usr/share/filebeat/filebeat.yml && \
    chmod +x /entrypoint.sh
USER filebeat

ENTRYPOINT  ["/entrypoint.sh"]
CMD ["start"]