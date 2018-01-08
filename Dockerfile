# our base image
#FROM python:3.6-onbuild
FROM amazon/aws-eb-python:3.4.2-onbuild-3.5.1

# specify the port number the container should expose
EXPOSE 5000

RUN mkdir -p /opt/ducky

COPY ./ /opt/ducky

RUN cd /opt/ducky && pip install -r requirements.txt && python -m textblob.download_corpora lite

ENV FLASK_APP /opt/ducky/what_the_duck.py

#ENV PATH /usr/local/bin

ENTRYPOINT ["/bin/bash"]

# run the application
CMD ["-x", "/opt/ducky/container_entry.sh"]
