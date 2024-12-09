# DICOM-Interval-Scheduler
A Flask-based API designed to optimize DICOM data processing pipelines. The API efficiently counts incoming DICOM files and thus ensures balanced orchestration of the DICOM-to-FHIR pipeline.

### Important: This pipeline serves as a "framework" that requires customization with individual functions to process DICOM studies. It is part of the DICOM-to-FHIR pipeline used at UHE and is provided here as a base. However, both the input connection to the PACS and the subsequent processing steps must be implemented and integrated with the API by the user!
