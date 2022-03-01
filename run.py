import config
import requests as reqs
import smtplib
import json
from datetime import datetime, date
import os

def make_request(course_id):
    # https://canvas.instructure.com/doc/api/
    req_header = {
        'Authorization': 'Bearer ' + str(config.CANVAS_API_USER_TOKEN),
        'Content-Type': 'application/json'
    }
    endpoint = 'https://canvas.tamu.edu/api/v1/courses/' + \
            str(course_id) + '/assignments?per_page=9999'

    res = reqs.get(endpoint, headers=req_header)
    return json.loads(res.text)


def send_email(assignment_name, canvas_url, date_due):
    try:
        server = None
        server = smtplib.SMTP('{}:{}'.format(config.SMTP_SERVER_NAME, config.SMTP_PORT))
        server.ehlo()
        server.starttls()
        server.login(config.SEND_FROM_EMAIL, config.SEND_FROM_PASS)

        subject = '{} is due soon'.format(assignment_name)
        body = '{}\nDate: {}'.format(canvas_url, date_due) 
        message = 'From:{}\nTo:{}\nSubject:{}\n\n{}' \
                .format('Upcoming Due Date', config.SEND_TO_EMAIL, subject, body)
        server.sendmail(config.SEND_FROM_EMAIL, config.SEND_TO_EMAIL, message)
    except Exception as e:
        if (config.LOG_ERRORS):
            directory = os.path.dirname(os.path.abspath(__file__))
            log_file = os.path.join(directory, config.ERROR_LOG_FILE)
            with open(log_file, 'a') as log:
                log.write('{}: {}\n'.format(str(datetime.utcnow()), str(e)))
    finally:
        if server is not None:
            server.quit()


def get_days_diff(d2):
    d1 = datetime.strptime(str(date.today()), "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return (d2 - d1).days


def main():
    for i in range(len(config.COURSES_IDS)):    
        # For every course id, make a request to receive a response 
        # containing assignment data for the class
        course_id = config.COURSES_IDS[i]
        res = make_request(course_id)

        for j in range(len(res)):            
            # Iterate through assignments                                          
            assignment_raw_due = res[j]['due_at']

            # days_remaining will determine if the due date falls within range of NOTIFY_DAY 
            days_remaining = -1

            if (assignment_raw_due is not None):
                assignment_due = assignment_raw_due[:assignment_raw_due.find('T')]
                days_remaining = get_days_diff(assignment_due)

            if (days_remaining == config.NOTIFY_DAY):
                assignment_name = res[j]['name']
                canvas_url = res[j]['html_url']
                send_email(assignment_name=assignment_name, canvas_url=canvas_url, 
                    date_due=assignment_due)

main()