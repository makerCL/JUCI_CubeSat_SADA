# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.5)

file(MAKE_DIRECTORY
  "C:/VSARM/sdk/pico/pico-sdk/tools/pioasm"
  "C:/Users/gavin/Documents/School/ENGINEERING/ME 428-430/JUCI_CubeSat_SADA/Software/Stepper_Motor_driver/build/pioasm"
  "C:/Users/gavin/Documents/School/ENGINEERING/ME 428-430/JUCI_CubeSat_SADA/Software/Stepper_Motor_driver/build/pico-sdk/src/rp2_common/cyw43_driver/pioasm"
  "C:/Users/gavin/Documents/School/ENGINEERING/ME 428-430/JUCI_CubeSat_SADA/Software/Stepper_Motor_driver/build/pico-sdk/src/rp2_common/cyw43_driver/pioasm/tmp"
  "C:/Users/gavin/Documents/School/ENGINEERING/ME 428-430/JUCI_CubeSat_SADA/Software/Stepper_Motor_driver/build/pico-sdk/src/rp2_common/cyw43_driver/pioasm/src/PioasmBuild-stamp"
  "C:/Users/gavin/Documents/School/ENGINEERING/ME 428-430/JUCI_CubeSat_SADA/Software/Stepper_Motor_driver/build/pico-sdk/src/rp2_common/cyw43_driver/pioasm/src"
  "C:/Users/gavin/Documents/School/ENGINEERING/ME 428-430/JUCI_CubeSat_SADA/Software/Stepper_Motor_driver/build/pico-sdk/src/rp2_common/cyw43_driver/pioasm/src/PioasmBuild-stamp"
)

set(configSubDirs )
foreach(subDir IN LISTS configSubDirs)
    file(MAKE_DIRECTORY "C:/Users/gavin/Documents/School/ENGINEERING/ME 428-430/JUCI_CubeSat_SADA/Software/Stepper_Motor_driver/build/pico-sdk/src/rp2_common/cyw43_driver/pioasm/src/PioasmBuild-stamp/${subDir}")
endforeach()
