# rq-docker
Simple Docker environment for using [redis](https://redis.io/) and [rq](https://python-rq.org/) task queues in your applications.


# Dependencies
If you need anything outside of python standard you can put dependencies in rq-worker/requirements.txt


# Jobs
If you want job logic/code available to the worker container then you will need to place it within the rq-worker/jobs directory.


# Starting the worker
```
$ git clone git@github.com:dustyfresh/rq-docker.git
$ cd rq-docker/
$ docker-compose build && docker-compose up -d
```


# Scaling
You can change the ```scale``` parameter within the docker-compose.yml file. By default it's set to 5. **This parameter requires docker-compose >= 1.27**.


# Security
It's all running as root within the container with redis on localhost by default. If you have requirements to not do this then you will need to make changes.
