FROM python:3.8.9
WORKDIR /app
RUN apt-get update -y && apt-get install git-lfs -y && \
    git clone https://github.com/andrew27lee/GPT2-Little-Women.git
WORKDIR GPT2-Little-Women
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["flask", "run", "--host", "0.0.0.0", "--without-threads"]
