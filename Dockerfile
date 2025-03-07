FROM python:3.10-slim

RUN apt-get update && apt-get install -y wget unzip &&  \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add  &&  \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list &&  \
    apt-get update && apt-get install -y google-chrome-stable

RUN wget -q -O /tmp/chromedriver.zip "https://chromedriver.storage.googleapis.com/$(wget -q -O - https://chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip" &&  \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/ &&  \
    rm /tmp/chromedriver.zip

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY tests/ /app/tests

CMD ["pytest", "-v"]
