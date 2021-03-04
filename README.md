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

# Example
You can find a working example within the rq-worker/example directory. You would submit a task to the queue with the example:

```python
#!/usr/bin/env python
import jobs
from rq import Queue
from time import sleep
from redis import Redis

def main():
    q = Queue(connection=Redis())
    job = q.enqueue(jobs.test_job)
    print(f'Created {job.id}')
    for _ in range(60):
        job = q.fetch_job(job.id)
        status = job.get_status()
        print(f'{job.id} -- {status}')
        sleep(1)
        # break when done
        if status in ['deferred', 'finished', 'stopped', 'failed']:
            break

if __name__ == '__main__':
    main()

```


# Scaling
You can change the ```scale``` parameter within the docker-compose.yml file. By default it's set to 5. **This parameter requires docker-compose >= 1.27**.


# Security
It's all running as root within the container with redis on localhost by default. If you have requirements to not do this then you will need to make changes.
