# Expression Faders

A simple midi controller with 2 faders and 2 rotary encoders. This was made for adding midi cc1 and cc11 while playing midi instruments such as strings to give more dynamic range and expression. The rotary encoders can also be mapped to any track specific features such as volume or other daw macros.

The goal was to be able to add more dynamic control while playing on a midi keyboard. Inspired by [Christian Henson](https://youtu.be/O5ax1lMdYO0?si=J35fgkykRBnHvoFT&t=346) and his approach to string writing and playing on a midi keyboard.

<img src=assets/assembled.png alt="assembled" width="500"/>

<img src=assets/topless.png alt="topless" width="500"/>

## Features

- 2 ptb0143 100mm faders for controlling midi cc
- 2 ec11 rotary encoders for controlling other daw values such as volume
- Xiao rp2040 for its midi support and size

## CAD

Consists of a base and a top lid that slots in a lip on the base. PCB is mounted to the lid with 4 m3 screws that go into the faders.

<img src=assets/case.png alt="case" width="500"/>

Made in Onshape.

[source](https://cad.onshape.com/documents/7d573544174621b2e2808d4e/w/58510c4aadba22e801dceb47/e/146ecd20f6130f1f9171a54c?renderMode=0&uiState=69f439aeeff61854c6391ffe)

## PCB

Made in Kicad

### Schematic

<img src=assets/schematic.png alt="schematic" width="500"/>

### PCB

<img src=assets/pcb.png alt="pcb" width="500"/>

## Firmware

Uses python with the usb midi library and adafruit to take the GPIO input and send midi signals back to the computer.

## BOM

| Product         | Amount | Unit Cost (THB) | Price (THB) | Price (USD) | Link                                                                                                                                                             |
| --------------- | ------ | --------------- | ----------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| EC11            | 2      | 145.16          | 290.32      | 8.87        | [https://www.digikey.co.th/en/products/detail/alps-alpine/EC11E15244G1/21721550](https://www.digikey.co.th/en/products/detail/alps-alpine/EC11E15244G1/21721550) |
| ptb0143         | 2      | 178.46          | 356.92      | 10.91       | [https://www.digikey.co.th/ordering/shoppingcart](https://www.digikey.co.th/ordering/shoppingcart)                                                               |
| orpheus pico    | 1      | ?               | ?           | 0.00        |                                                                                                                                                                  |
| m3 screws       | 4      |                 | 20          | 0.61        | [https://www.digikey.co.th/en/products/detail/apm-hexseal/RM3X8MM-2701/3712297](https://www.digikey.co.th/en/products/detail/apm-hexseal/RM3X8MM-2701/3712297)   |
| digikey shiping |        |                 | 600         | 18.33       |                                                                                                                                                                  |
| jlcpcb          |        |                 |             | 12.13       |                                                                                                                                                                  |
|                 |        |                 |             |             |                                                                                                                                                                  |
| total           |        |                 |             | 50.85       |                                                                                                                                                                  |
