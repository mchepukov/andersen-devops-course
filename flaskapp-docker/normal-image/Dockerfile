FROM debian:stable-slim

RUN sudo apt install -y python3-pip python3-venv
RUN git clone https://github.com/mchepukov/andersen-devops-course.git
RUN cd andersen-devops-course/python-flask-app/
RUN python3 -m venv venv
RUN source venv/bin/activate
RUN pip3 install -r requirements.txt

COPY app .

RUN app