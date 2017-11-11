FROM python:3.6.3
ENV PYTHONUNBUFFERED 1

#Change Timezone to GMT+7
#ENV TZ=Asia/Bangkok
#RUN ln -snf /usr/share/zoneinfo/$TZ

#Install requirement to compile messages
RUN apt-get update \
    && pip install pipenv
#    && apt-get install -y \


#Location of source code
#ENV PROJECT_ROOT /opt/app
#RUN
WORKDIR /opt/app

COPY Pipfile Pipfile.lock main.py ./
COPY templates ./templates

RUN pipenv install --system --deploy