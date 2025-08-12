#base image
FROM python:3.9

#workdir
WORKDIR /app

#copy command
COPY . /app

#run command
RUN pip install -r requirements.txt

#ports
EXPOSE 8501

#command
CMD ["streamlit","run", "./front_end_with_threading.py"]