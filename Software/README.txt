The software uses C++ as the compiler. To run code on the Pico, you must first
Download an IDE (I use VS Code) and download a CMake compiler. When writing
software, you first create a main.c file in your working directory, then once
it is written, you have to make a CMakeLists.txt file that includes all the
information CMake needs to compile your code. For reference, look at the 
CMakeLists.txt file in the ADC_Read_script directory. For additional setup, 
refernce this video: https://www.youtube.com/watch?v=B5rQSoOmR5w&ab_channel=Digi-Key
For C++ documentation on the PI, reference the following doxygen pages:
https://raspberrypi.github.io/pico-sdk-doxygen/modules.html
