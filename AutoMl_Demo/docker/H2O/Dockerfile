FROM openjdk:8
WORKDIR /home

ENV LANG en_US.UTF-8 
RUN wget http://h2o-release.s3.amazonaws.com/h2o/rel-yau/1/h2o-3.26.0.1.zip && unzip h2o-3.26.0.1.zip
CMD java -jar h2o-3.26.0.1/h2o.jar
