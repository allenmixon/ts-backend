FROM python:3.9

COPY . /ts-backend
WORKDIR /ts-backend/app

RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

EXPOSE 5000 5342

CMD [ "python3", "run.py"]