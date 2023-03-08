This file details the electrical subsystems
Author: Miles Alderman

##Boards:
- Photodiode Breakout: used for sun sensing with one connected to each solar array
- Pico Shield: Peripherals and connection points that interfaces with a Raspberry Pi Pico

##Accessing the Files
- all project files are in Kicad version 6, which the use will need to use to view them
- Digikey library was imported, available at https://forum.digikey.com/t/importing-the-digi-key-kicad-library-into-kicad-5-0-0/4075
- Custom schematic symbols and footprints are in the "KiCad Libs" folder. These will need to be imported


#SADA Board

##Description
The "SADA BOARD" encompasses all the functionality necessary for the Solar Array Drive Assembly and its components. It would interface with a "Systems Board" through a protocol like I2C or CAN.

##Functionality
- Voltage regulator accepts between 3.7 to 4.2V from an external power supply, which represents a single parallel group of Lithium Ion cells, as would like be present in a CubeSat since about 66% of nano and pico scale satellites implement them.(Bouwmeester and Guo). A battery and battery management system is out of scope for this project.
- Nichrome Wire burner: to burn the fishing line that passively retains the spring-loaded solar arrays, we use Nichrome burn wire. This is necessary since the satellite must be powered off during launch. There are pins used to control the burn signal, one of which is the enable for the PMIC, the other of which controls a Mosfet for connecting power to the Nichrome. In some tests, we found that when the system was powered up from its launch state, if the power supply was turned on with a direct connection to the wire it heated it slower, resulting in less reliable deployment. By having a transistor, we can allow the PMIC to become fully stable, and then open it to heat the wire. This PMIC can then be disable to save power after the wire is burnt. Our tests foudn that about 1.5A was the minimum current to heat the wire enough to cleanly burn the fishing line.
- Photodiode measurement circuits: since in a full CubeSat build there would need to be orientation photodiodes on each corner, the peripherals are provided to do so. This includes a MUX to an ADC channel of the MCU to take this measurement.
- Stepper Motor Drivers: Since the stepper motors for axial rotation of the arrays need to be driven from the MCU, a Darlington Transistor array is used to accomplish this. This allows the small current of the MCU GPIO to drive the much higher current needed by a stepper, taken from the 5V supply. Stepper motors are precise, but very power hungry due to _________, so we decided to have MOSFETS that can disconnect from power for when the steppers are not actively changed. This does eliminate some functionality of the steppers, such as fractional stepping, but the resolution of that is far greater than our sensing method's, and thus we couldn't take advantage of it anywyas.
- Breakout board connectors: connectors to the Photodiode Breakout Board are implemented for 2 MUX pins, an ADC channel, power and ground


##Design Considerations 
For full information, please see current design report in the parent folder of the repository. Some key details are listed below
- Were not able to use a "space grade" MCU since they are far too expensive for the price point of this project. We therefore are trying to adapt consumer grade MCUs to fit the needs of this project. This would only protect against total radiation experienced from low energy particles, and not against bit flips. In the systems board, TMR would likely be used. 
- Since this is a prototype and will not be launched into space, we aren't going through the rad hardening. It would be silly to spend extra money for a more specific MCU that wouldn’t work anyways. All the other common MCUs have similar temperature ranges besides the ESP32, although its is still not within range of what we expect a CubeSat to encounter
- Dual Modular Redundancy for these systems?
- In a full system, the battery system would output between about 3.6 - 4.2V if a lithium ion cell chemistry was used. We need to step that down to 3.3V for the RP2040. We chose to use an LDO to power the MCU despite them being less efficient than switching regulators since when the LDOs will use less power when considering the high amount of sleep time of the MCU.
- We decided to use stepper motors despite them being very power hungry. Stepper motors invert  the "locked rotor" issue of dc motors, stepping between locked rotor positions. This means that when the motor is not moving, the coils are still fully energized. This is bad for a CubeSat, where power is extremely scarce. To get around this issue while still utilizing the positional accuracy of stepper motors, we can step the motor and then immediately disconnect the power line so that it stops drawing current. Since the cores of the motor are permenant magnets, the motor remains in the last position even when the motor is off, as long as we do not depend on any partial-stepping functions. 
- USB implemented for the development process, but isn't necessary on a deployed system. It allows the engineer to set it up as a flash device, making it convenient to interface with. The STLINK with SWD and TX/RX pins can be used for all of the functionality in its absence as well. It enables debugging, a serial port, and flashing binary code (such as Micropython) onto the main board.

SOFTWARE
- NRST Pin exposed to systems board so that software reflash could be triggered externally and passed through I2C instead of SWD. On our board though, we still have teh SWD pins exposed since that is how we will be flashing code. NRST is also helpful as an external reset as it resets the registers and changes the program counter to the reset vector. https://electronics.stackexchange.com/questions/491068/what-is-the-use-of-nrst-pin-in-stm32f401rct6 and p21 of Data sheet


##Citations:
J. Bouwmeester, J. Guo, Survey of worldwide pico- and nanosatellite missions, distributions and subsystem technology, Acta Astronautica,


CONCERNS:
- Auxillary photodiode board- if it's just on the panel, it likely will be buffeted with radiation, heat, etc. Need to plan for this