FROM python:3.12.2
WORKDIR home/user/workdir
COPY scripts/build/__main__.py \
     scripts/build/dataset.py \
     scripts/build/model.py \
     scripts/build/requirements.txt \
     scripts/build/
COPY scripts/utils.py scripts/
RUN pip install -r scripts/build/requirements.txt
CMD python -m scripts.build
