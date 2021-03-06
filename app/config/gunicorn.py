import multiprocessing

bind = ['0.0.0.0:5000']
workers = multiprocessing.cpu_count() * 2 + 1
accesslog = '/var/log/gunicorn/access.log'
errorlog = '/var/log/gunicorn/error.log'
timeout = 60
worker_class = 'eventlet'