FROM jupyter/scipy-notebook:python-3.11

COPY .binder/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /home/jovyan/work
