![ph](https://private-user-images.githubusercontent.com/209415989/632649059-6a0b576d-de7f-4530-a6df-a972efe10215.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODYwNjE5MjMsIm5iZiI6MTc4NjA2MTYyMywicGF0aCI6Ii8yMDk0MTU5ODkvNjMyNjQ5MDU5LTZhMGI1NzZkLWRlN2YtNDUzMC1hNmRmLWE5NzJlZmUxMDIxNS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwODA3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDgwN1QwMDEzNDNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT02NzdjMzBkYjNlNzFjYmVkMzY2OTEwNGM4N2M5YzVjNDFhYTc3N2QzOTg1YmUyODAwN2NkZjY5M2I5NGQ5NzZiJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.4QwKNAS6UlQ16Zq-_sydGR7I_58oowuRrX1x8nhjcUY)
# Z-Visualizer

Z-Visualizer is a simple desktop audio spectrum analyzer for audio playing on your PC.

![](https://img.shields.io/badge/chowitas%20guapo-8A2BE2)
![](https://img.shields.io/github/contributors-anon/werchai/Z-Visualizer)
![](https://img.shields.io/github/commit-activity/w/werchai/Z-Visualizer)

## Features
- Captures your system playback audio using a loopback recording device
- Displays a real-time bar-style frequency spectrum
- Lightweight single-window desktop app

## Requirements
- Python 3.10+
- Windows (loopback capture support is designed for Windows playback devices)
- Numpy 1.26.0+ (if using direct .py app)
- Soundcard 0.4.3+ (if using direct .py app)

## Usage
There are two ways to set up:
1. Using the direct pure python program
2. Downloading from the latest [Release](https://github.com/werchai/Z-Visualizer/releases), and using the exe file

## Screenshots
| ![](./assets/notinuse.png) | ![](./assets/image.png) |
|---------------------------------|-------------------------------|

## Known Issues
- Flickering when program is in use

## To-Do
- [x] Package app into .exe file
- [ ] Unify window topbar to match main window color
