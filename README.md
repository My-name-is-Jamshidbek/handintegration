# HandIntegration

HandIntegration is a Python-based project that utilizes the MediaPipe library to detect hand landmarks and determine the state (open or closed) of each finger. The project captures live video feed from a webcam, processes the hand landmarks, and sends the states of the fingers to a specified server using GET requests.

## Features

- Real-time hand landmark detection using MediaPipe.
- Determine if each finger (thumb, index, middle, ring, pinky) is open or closed.
- Sends the state of the fingers to a server via GET requests.
- Visual feedback of finger states on the video feed.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/My-name-is-Jamshidbek/handintegration.git
    cd handintegration
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Connect your webcam to your computer.

2. Run the script:
    ```bash
    python handintegration.py
    ```

3. The script will start capturing the video feed and process hand landmarks.

4. The states of the fingers (open or closed) will be displayed on the video feed and sent to the server at `http://192.168.4.1/sendSignal` with the data parameter representing the states of the fingers (e.g., `00000` for all fingers closed, `11111` for all fingers open).

## File Structure

- `handintegration.py`: Main script that runs the hand detection and state sending logic.
- `requirements.txt`: List of required Python packages.

## Dependencies

- OpenCV
- MediaPipe
- NumPy
- Requests

You can install the dependencies using the following command:
```bash
pip install -r requirements.txt
