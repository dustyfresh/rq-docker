#!/usr/bin/env python
from rq import Queue
from time import sleep
from redis import Redis
import jobs

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
