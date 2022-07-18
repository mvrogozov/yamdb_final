FROM python:3.7-slim
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt --no-cache-dir
COPY ./ .
LABEL author='mv_rogozov'
CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000"]
RUN python3 manage.py collectstatic --noinput
