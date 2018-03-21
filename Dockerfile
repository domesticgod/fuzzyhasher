FROM python:3
WORKDIR /usr/src/app


#no modules need installing at the moment
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8080
CMD ["python","./fuzzyserver.py"]
