# our base image
FROM python:3.6-onbuild

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
