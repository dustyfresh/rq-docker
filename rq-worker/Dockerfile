FROM debian:buster

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN apt update && \
  apt dist-upgrade -y

RUN apt install -y \
  build-essential git supervisor python3-pip python3-setuptools python3-dev \
  curl nmap whois

ADD ./requirements.txt /root/requirements.txt
RUN pip3 install virtualenv && \
  virtualenv -p python3 /root/venv && \
  source /root/venv/bin/activate && pip install -r /root/requirements.txt

ADD conf/supervise-*.conf /etc/supervisor/conf.d/

CMD ["/usr/bin/supervisord", "-n"]
