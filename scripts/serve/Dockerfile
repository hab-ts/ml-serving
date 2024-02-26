FROM python:3.12.2
WORKDIR home/user/workdir
COPY scripts/serve/__main__.py \
     scripts/serve/requirements.txt \
     scripts/serve/
COPY scripts/utils.py scripts/
RUN pip install -r scripts/serve/requirements.txt
CMD python -m scripts.serve
