# Image Captioning Model

## Overview

This project implements an image captioning model using the Flickr30k dataset. A combination of a convolutional neural network (ResNet50) for image feature extraction and a recurrent neural network (LSTM) for caption generation is used. The workflow includes vocabulary building, model training, evaluation using BLEU scores, and sample caption generation.

The notebook also provides preprocessing steps and loading mechanisms for the dataset. Captions are cleaned, tokenized, and filtered based on frequency thresholds.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/noorayym/image-captioning
    cd image-captioning
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  
    ```

3. **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run Streamlit UI:**

    ```bash
    streamlit run app.py
    ```


## License

This project is licensed under the terms of the MIT License.
