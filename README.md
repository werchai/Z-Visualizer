# Z-Visualizer

Z-Visualizer is a simple desktop audio spectrum analyzer for audio playing on your PC.

![gre](https://img.shields.io/badge/chowitas%20gey-8A2BE2)

## Features
- Captures your system playback audio using a loopback recording device
- Displays a real-time bar-style frequency spectrum
- Lightweight single-window desktop app

## Requirements
- Python 3.10+
- Windows (loopback capture support is designed for Windows playback devices)
- Numpy 1.26.0+
- Soundcard 0.4.3+

## Setup
```bash
pip install -r requirements.txt
```

## Run
```bash
python app.py
```

## Test
```bash
python -m unittest discover -s tests
```
## Known Issues
- Flickering when program is in use

## To-Do
- Package app into .exe file
- Unify window topbar to match main window color
