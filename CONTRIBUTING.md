# Docker copypasta
## Docker local:
FROM python:3.10  
EXPOSE 5000  
WORKDIR /app  
COPY requirements.txt .  
RUN pip install -r requirements.txt  
COPY . .  
CMD ["flask", "run", "--host", "0.0.0.0"]
<br/><br/>
CLI command to run docker container with volume which auto updates with new code  
`docker run -dp 5000:5000 -w /app -v ${pwd}:/app name-of-container sh -c "flask run 
--host 0.0.0.0"`

## Docker in WSGI:  
FROM python:3.10  
WORKDIR /app  
COPY requirements.txt .  
RUN pip install --no-cache-dir --upgrade -r requirements.txt  
COPY . .  
CMD ["/bin/bash", "docker-entrypoint.sh"]


