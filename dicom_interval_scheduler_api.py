from flask import Flask
from pathlib import Path
import os
import shutil
import dicom2fhir_wrapper

successful_path = "/opt/dicom2fhir/data/successful/"
output_path = "/opt/dicom2fhir/data/output/"


def create_app():
    app = Flask(__name__)

    @app.route('/dicom_count', methods=['GET'])
    def get_dicom_count():
        dcm_files = Path(successful_path).rglob("*.dcm")
        return str(sum(1 for _ in dcm_files))

    @app.route('/process_study', methods=['POST'])
    def process_study():
        dicom2fhir_wrapper.process_study(successful_path, output_path)
        return "Processed study successfully"

    @app.route('/delete_dicoms', methods=['POST'])
    def delete_dicoms():
        for filename in os.listdir(successful_path):
            file_path = os.path.join(successful_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))
        return "Deleted DICOMs successfully"

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
