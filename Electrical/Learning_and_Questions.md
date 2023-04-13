## Questions
- separate power supply for ADC?
- is there a difference between power cycling for reset and external reset with NRST pin?
- there seems to be so many different types of resets and conditions... which types matter to us?
- Battery Sag makes Battery input even lower than 3.6V at low SOC?

- Oscillator design
    - Do we need to run this MCU at full speed? (80 MHz)? do we need an external oscillator?
    p11 of oscillator design; Cs is stray capacitance of oscin and oscout pins plus pcb parasitic capacitance

- Double mosfets Too redundant for passive retainment since it only has to work once at the beginning of deployment?
- Clock needs for USB (datasheet p57)
- what would input power be from battery board? Would it be a nominal voltage?
- noise considerations- where are overlapping frequencies? Other design considerations for switching component compatability?
- GIO: which ldo did you use for batt to 3v3 line?


## UPGRADED BOARD
- NRST connected to systems board

## Discussion
- could perhaps use lowpower mode with LSE instead with a lean and mean C code?
