# canvas-notify

Never miss turning in an assignment on Canvas again. Get notified by email when a due date is approaching.

### Usage

1. Clone repository

2. `cd` into the project's directory, and create a virtural environment

   ```
   python3 -m venv env
   source env/bin/activate
   ```

3. Install dependencies

   `pip3 install -r requirements.txt`

4. Create a `.env` file

   ```
   export CANVAS_API_USER_TOKEN=""
   export SEND_FROM_EMAIL=""
   export SEND_FROM_PASS=""
   export SEND_TO_EMAIL=""
   ```

5. Generate an access token through Canvas. 
   
   You are able to generate a token in Canvas under your settings: `{canvas-domain}/profile/settings`
   
   In `.env`, set `CANVAS_API_USER_TOKEN` to your token.

6. In `config.py`, add relevant course ids to `COURSES_IDS`

   To find the course ids of your courses, make a request:

    ```
    curl -H 'Authorization: Bearer <token>'
    https://<canvas>/api/v1/courses?per_page=999
    ```

    The course id key is `id`

7. If you are not sending with gmail, modify `SMTP_SERVER_NAME` and `SMTP_PORT` in `config.py` with the respective name and port.

8. In `.env`, set `SEND_FROM_EMAIL` and `SEND_FROM_PASS` to the credentials of the emails of which you are sending from.

    *If using Gmail, [allow less secure apps](https://myaccount.google.com). For security, it is recommended you use do not do this on your primary email.*

9. In `.env`, set `SEND_TO_EMAIL` to the email to which you want to receive emails from.

10. *Optional:* In `config.py`, modify `NOTIFY_DAY` to the amount of days between a due date and current date.

11. *Optional:* To disable logging, set `LOG_ERRORS` in `config.py` to False. But, error logging may be useful should something break or change. An example of a log:

    ```
    2022-03-01 03:46:51.495281: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials y28-20020a4aea3c000000b0031c0cddfbf9sm5766114ood.20 - gsmtp')
    ```

### Hosting

You can run this script many ways.

1. Manually. It defeats the purpose of automation, but `python3 run.py` is foolproof I suppose.
2. Schedule a cron job, if you have a Linux or Unix machine. Modifications to the script may be necessary.
3. Or, use a cloud service. [PythonAnywhere allows you to schedule daily tasks for free](https://help.pythonanywhere.com/pages/ScheduledTasks/)
