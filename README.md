# clustaar_webhook
This is a basic Webhook for clustaar Chatbots platform,
to get it working first signup and install ngrok : [https://ngrok.com/](https://ngrok.com/)
It will help us to get a public domain with ssl certificate for free.

Following we need to install the dependencies with:

```bash
pip install -r requirements.txt
```

Then we most migrate the db to get the sample data with:

```bash
python migrate.py
```

finally we have to run the webhook with **gunicorn** with the following command:

```bash
gunicorn main:app
```



