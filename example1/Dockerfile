FROM python:3.6
RUN pip install --upgrade pipenv
RUN mkdir /code
WORKDIR /code
COPY Pipfile Pipfile.lock /code/
RUN pipenv install --deploy --system
COPY . /code
