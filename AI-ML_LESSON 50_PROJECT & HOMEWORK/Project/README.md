# Model Compression Techniques Project

This project explores model compression techniques to reduce the size and computational complexity of pre-trained machine learning models. We implement two popular techniques: pruning and quantization, using scikit-learn, a popular machine learning library in Python.

## Project Overview

In this project, we aim to compress a pre-trained machine learning model using the following techniques:

1. **Pruning:** Removing unnecessary features from the dataset to reduce model complexity.
2. **Quantization:** Reducing the precision of model parameters to lower bit-width integers.

## Project Structure

- `compression.py`: Python script containing the implementation of model compression techniques.
- `README.md`: This file providing an overview of the project.
- `requirements.txt`: Text file listing the required dependencies for the project.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your_username/model-compression-project.git
Navigate to the project directory:

cd model-compression-project
Install the required dependencies:

pip install -r requirements.txt
Usage
Run the compression.py script to execute the model compression techniques.

python compression.py
Results
The script will print the original model's accuracy and the quantized model's accuracy after compression.

Contributing
Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or pull request.