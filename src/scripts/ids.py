import numpy as np
import h5py

# # Load TFLite model
# interpreter = tflite.Interpreter(model_path="converted_model.tflite")
# interpreter.allocate_tensors()

# # Get input and output tensor details
# input_details = interpreter.get_input_details()
# output_details = interpreter.get_output_details()

# # Prepare input data (example)
# data=[0,1,34,13,66,0,0,0,0,0,0,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0,0,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00]
# input_data = np.array(data,dtype=np.float32)

# # Set input tensor data
# interpreter.set_tensor(input_details[0]['index'], input_data)

# # Run inference
# interpreter.invoke()

# # Get output tensor data
# output_data = interpreter.get_tensor(output_details[0]['index'])

# print(output_data)


# Open the HDF5 file
with h5py.File('dnn1layer_model.h5', 'r') as model_file:
    model_structure = model_file.attrs.get('model_structure')
    print(model_structure)
    model_weights = model_file.attrs.get('model_weights')

# Create a new model using the structure
new_model = model_structure

# Load the weights into the model
new_model.load_weights(model_weights)

input_data=np.array([0,1,34,13,66,0,0,0,0,0,0,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0,0,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00])

predictions = new_model.predict(input_data)