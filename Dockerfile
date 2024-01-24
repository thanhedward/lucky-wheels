FROM python:3.10

WORKDIR /lucky_wheel    

COPY ./backend/requirements.txt /managing_database/

RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY . /lucky_wheel/

EXPOSE 6543

CMD ["python", ".\backend\main.py"]