FROM python:3.11
WORKDIR /opt/dicom2fhir

COPY ./requirements.txt .

RUN pip3 install -r requirements.txt
COPY ./dicom_interval_scheduler_api.py .

USER 65532:65532

ENTRYPOINT ["python3", "dicom_interval_scheduler_api.py"]
