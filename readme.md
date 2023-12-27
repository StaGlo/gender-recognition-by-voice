# Voice Gender Recognition

## Overview
This repository contains a Python-based voice gender recognition program.

## Repository structure
The repository contains:
- `gender_recognition_by_voice.py`- main program for gender recognition
- `plot_spectrums.py`- additional function for plotting spectrums 
- `test_accuracy.py`- program accuracy tester


## Usage 
The main script takes the filename of a WAV audio file as an input argument.
```
python gender_recognition_by_voice.py path/to/audiofile.wav
```

To test accuracy run:
```
python test_accuracy.py
```
Note: Ensure that the variables `data_dir` and `gender_recognition_script` in `test_accuracy.py` are set to the correct directory path and script path, respectively. The data_dir should contain WAV files (file with "K" in name are treated as female voices, with "M" in name as male).