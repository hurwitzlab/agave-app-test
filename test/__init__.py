import sys
import time


def wait_for_job_to_finish(job_id, cyverse_oauth_session):
    job_status_url = 'https://agave.iplantc.org/jobs/v2/{}/status'.format(job_id)

    job_status_response = cyverse_oauth_session.get(url=job_status_url)
    job_status = job_status_response.json()['result']['status']
    print(job_status)
    while not (job_status == 'FINISHED' or job_status == 'FAILED'):
        sys.stdout.write('sleeping 60 seconds')
        for j in range(6):
            sys.stdout.write('.')
            time.sleep(10)
        job_status_response = cyverse_oauth_session.get(url=job_status_url)
        job_status = job_status_response.json()['result']['status']

        print(job_status)

    return job_status
