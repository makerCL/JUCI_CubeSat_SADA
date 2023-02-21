This file details the electrical subsystems
Author: Miles Alderman

Boards:
- Photodiode Breakout: used for sun sensing with one connected to each solar array
- Pico Shield: Peripherals and connection points that interfaces with a Raspberry Pi Pico

Accessing the Files
- all project files are in Kicad version 6, which the use will need to use to view them
- Digikey library was imported, available at https://forum.digikey.com/t/importing-the-digi-key-kicad-library-into-kicad-5-0-0/4075
- Custom schematic symbols and footprints are in the "KiCad Libs" folder. These will need to be imported


Pico Shield

Description: Peripherals and connection points that interfaces with a Raspberry Pi Pico

Functionality:
- Accepts 5V from an external power supply, which represents a battery system in a full CubeSat Build
- Nichrome Wire burner: to burn the fishing line that passively retains the spring-loaded solar arrays, we use Nichrome burn wire. This is necessary since the satellite must be powered off during launch. There are pins used to control the burn signal, one of which is the enable for the PMIC, the other of which controls a Mosfet for connecting power to the Nichrome. In some tests, we found that when the system was powered up from its launch state, if the power supply was turned on with a direct connection to the wire it heated it slower, resulting in less reliable deployment. By having a transistor, we can allow the PMIC to become fully stable, and then open it to heat the wire. This PMIC can then be disable to save power after the wire is burnt. Our tests foudn that about 1.5A was the minimum current to heat the wire enough to cleanly burn the fishing line.
- Photodiode measurement circuits: since in a full CubeSat build there would need to be orientation photodiodes on each corner, the peripherals are provided to do so. This includes a MUX to an ADC channel of the MCU to take this measurement.
- Stepper Motor Drivers: Since the stepper motors for axial rotation of the arrays need to be driven from the MCU, a Darlington Transistor array is used to accomplish this. This allows the small current of the MCU GPIO to drive the much higher current needed by a stepper, taken from the 5V supply. 
- Breakout board connectors: connectors to the Photodiode Breakout Board are implemented for 2 MUX pins, an ADC channel, power and ground



Design Considerations: for full information, please see current design report in the parent folder of the repository. Some key details are listed below
- We decided that because the MCU is enclosed we could relax the temperature range that we expect it to encounter, stated as -35C to +70C in the report. 
- Since this is a prototype and will not be launched into space, we aren't going through the rad hardening. It would be silly to spend extra money for a more specific MCU that wouldn’t work anyways. All the other common MCUs have similar temperature ranges besides the ESP32, although its is still not within range of what we expect a CubeSat to encounter