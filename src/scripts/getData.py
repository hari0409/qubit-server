import sys
from contextlib import contextmanager
import time
import csv
from sklearn.preprocessing import Normalizer
from datetime import datetime
from uuid import uuid4



@contextmanager
def suppress_stdout():
    # Redirect standard output to a temporary buffer
    original_stdout = sys.stdout
    sys.stdout = open('temp_stdout', 'w')
    try:
        yield
    finally:
        sys.stdout.close()
        sys.stdout = original_stdout


def get_last_line(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        if lines:
            last_line = lines[-1].strip()  # Remove newline character
            return last_line
    return None

csv_file_path = '../sniffer/output.csv'  # Replace with your CSV file path

from keras.models import load_model
import numpy as np

# Load the model
loaded_model = load_model('model_ids.hdf5')


while True:
    last_line = get_last_line(csv_file_path)
    if last_line:
        last_line=[float(i) for i in last_line.split(",")]
        last_line=np.array([last_line])
        last_line.astype(float)
        scaler = Normalizer().fit(last_line)
        last_line = scaler.transform(last_line)
        X_trial = np.array(last_line)
        with suppress_stdout():
            pred=loaded_model.predict(X_trial,)
            print(pred)
            if(pred>0.5):
                pred=0
            else:
                pred=1
                name=f"/home/hari/Downloads/packs/{datetime.now().strftime('%Y%m-%d%H-%M%S-')}-{uuid4()}"
                name+=".txt"
                f=open(name,"w+")
                f.write(str(last_line))
    
    else:
        print("No data in the file yet.")
    
    time.sleep(1)  # Adjust the interval as needed