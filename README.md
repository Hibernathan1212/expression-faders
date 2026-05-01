# Expression Faders

A simple midi controller with 2 faders and 2 rotary encoders. This was made for adding midi cc1 and cc11 while playing midi instruments such as strings to give more dynamic range and expression. The rotary encoders can also be mapped to any track specific features such as volume or other daw macros.

The goal was to be able to add more dynamic control while playing on a midi keyboard. Inspired by [Christian Henson](https://youtu.be/O5ax1lMdYO0?si=J35fgkykRBnHvoFT&t=346) and his approach to string writing and playing on a midi keyboard.

<img src=assets/assembled.png alt="assembled" width="500"/>

<img src=assets/topless.png alt="topless" width="500"/>

## Features

- 2 ptb0143 100mm faders for controlling midi cc
- 2 ec11 rotary encoders for controlling other daw values such as volume
- Xiao rp2040 for its midi support and size
- Has multiple decoupling caps to ground to reduce electronic noise from signal

## CAD

Consists of a base and a top lid that slots in a lip on the base. PCB is mounted to the lid with 4 m3 screws that go into the faders.

<img src=assets/case.png alt="case" width="500"/>

Made in Onshape.

[source](https://cad.onshape.com/documents/7d573544174621b2e2808d4e/w/58510c4aadba22e801dceb47/e/146ecd20f6130f1f9171a54c?renderMode=0&uiState=69f439aeeff61854c6391ffe)

## PCB

Made in Kicad.

### Schematic

<img src=assets/schematic.png alt="schematic" width="500"/>

### PCB

<img src=assets/pcb.png alt="pcb" width="500"/>

## Firmware

Uses python with the usb midi library and adafruit to take the GPIO input and send midi signals back to the computer. Has a hysteresis threshold to try and reduce electronic noise.

## BOM

| Product                   | Amount | Unit Cost (THB) | Price (THB) | Price (USD) | Link                                                                                                                                                                                                                                                                                         |
| ------------------------- | ------ | --------------- | ----------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| EC11                      | 2      | 81.42           | 162.84      | 5.00        | [https://th.element14.com/alps/ec11k1524402/encoder-vertical-11mm-30det-15ppr/dp/2064998](https://th.element14.com/alps/ec11k1524402/encoder-vertical-11mm-30det-15ppr/dp/2064998)                                                                                                           |
| ptb0143                   | 2      | 178.46          | 356.92      | 10.97       | [https://th.element14.com/bourns/ptb0143-2010bpb103/potentiometer-slide-10k-100mm/dp/1688409](https://th.element14.com/bourns/ptb0143-2010bpb103/potentiometer-slide-10k-100mm/dp/1688409)                                                                                                   |
| orpheus pico              | 1      | ?               | ?           | 0.00        |                                                                                                                                                                                                                                                                                              |
| m3 screws                 | 4      |                 | 132         | 4.06        | [https://th.element14.com/tr-fastenings/m35-bh10mcs100/screw-socket-butt-m3x5-pk100/dp/1420682](https://th.element14.com/tr-fastenings/m35-bh10mcs100/screw-socket-butt-m3x5-pk100/dp/1420682)                                                                                               |
| 100nf 0805 smd capacitors | 10     | 0.43            | 4.3         | 0.13        | [](https://th.element14.com/multicomp-pro/mc0805b104k250ct/cap-0-1-f-25v-10-x7r-0805/dp/1759166)[https://th.element14.com/multicomp-pro/mc0805b104k250ct/cap-0-1-f-25v-10-x7r-0805/dp/1759166](https://th.element14.com/multicomp-pro/mc0805b104k250ct/cap-0-1-f-25v-10-x7r-0805/dp/1759166) |
| element 14 shipping       |        |                 | 550         | 16.90       |                                                                                                                                                                                                                                                                                              |
| jlcpcb                    |        |                 |             | 12.13       |                                                                                                                                                                                                                                                                                              |
|                           |        |                 |             |             |                                                                                                                                                                                                                                                                                              |
| total                     |        |                 |             | 49.18       |                                                                                                                                                                                                                                                                                              |
