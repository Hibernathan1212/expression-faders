import board
import analogio
import rotaryio
import digitalio
import usb_midi
import adafruit_midi
from adafruit_midi.control_change import ControlChange

CC_FADER0 = 11  # Expression
CC_FADER1 = 1  # Modulation
CC_ENC1 = 20
CC_ENC2 = 21

midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0)

fader0 = analogio.AnalogIn(board.GP27)
fader1 = analogio.AnalogIn(board.GP26)

enc1 = rotaryio.IncrementalEncoder(board.GP01, board.GP00)
enc2 = rotaryio.IncrementalEncoder(board.GP07, board.GP06)

last_fader0_val = 0
last_fader1_val = 0
last_enc1_pos = 0
last_enc2_pos = 0


def get_midi_val(analog_in):
    return analog_in.value >> 9


while True:
    current_f0 = get_midi_val(fader0)
    if abs(current_f0 - last_fader0_val) > 1:  # Hysteresis threshold
        midi.send(ControlChange(CC_FADER0, current_f0))
        last_fader0_val = current_f0

    current_f1 = get_midi_val(fader1)
    if abs(current_f1 - last_fader1_val) > 1:
        midi.send(ControlChange(CC_FADER1, current_f1))
        last_fader1_val = current_f1

    curr_enc1_pos = enc1.position
    if curr_enc1_pos != last_enc1_pos:
        direction = 127 if curr_enc1_pos < last_enc1_pos else 1
        midi.send(ControlChange(CC_ENC1, direction))
        last_enc1_pos = curr_enc1_pos

    curr_enc2_pos = enc2.position
    if curr_enc2_pos != last_enc2_pos:
        direction = 127 if curr_enc2_pos < last_enc2_pos else 1
        midi.send(ControlChange(CC_ENC2, direction))
        last_enc2_pos = curr_enc2_pos
