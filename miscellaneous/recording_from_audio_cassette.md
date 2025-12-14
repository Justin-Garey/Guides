# Recording from an Audio Cassette

Assuming you have a cassette player with a headphone output, a 3.5 mm male to male audio cable, and a computer that has a microphone input port; then the audio cassettes can be recorded. 

## My Setup

- Panasonic RQ-L307 mini cassette player
- Ubuntu 24.04 OS

## Software

Audacity can be used to accomplish this task. To pull from the microphone port, install audacity and pavucontrol.
```bash
sudo apt install audacity pavucontrol
```

To set up Audacity to pull from the microphone port:
- Click on Audio Setup
    - Select Host -> Alsa
    - Select Playback Device -> Pulse

## Recording

Audacity has intuitive controls. When recording, try to keep the volume output from the cassette player low enough that the recording isn't too noisy.