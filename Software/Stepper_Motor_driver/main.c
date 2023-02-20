#include "pico.h"
#include "pico/stdlib.h"
#include <stdio.h>
#include "hardware/gpio.h"
#include "hardware/adc.h"



int main() {

    bool clockwise = false;
    uint8_t full_seq[4] = {};
    uint8_t CW_seq[4] = {9,12,6,3};
    uint8_t CCW_seq[4] = {3,6,12,9};

    if (clockwise) {
        for (int i=0; i < 4; i++) {
            full_seq[i] = CW_seq[i];
        }
    } else {
        for (int i=0; i < 4; i++) {
            full_seq[i] = CCW_seq[i];
        }
    }
    uint8_t gpio_ports[4] = {21,20,19,18};


    uint8_t s;
    uint16_t curr_step = 0;
    const float step_const = 2048/360;


    sleep_ms(3000);

    for (uint8_t i=0; i < 4; i++) {
        gpio_init(gpio_ports[i]);
        gpio_set_dir(gpio_ports[i], GPIO_OUT);
        gpio_put(gpio_ports[i], 0);
    }

    while (curr_step < step_const*360) {
        for (uint8_t i=0; i < 4; i++) {
            s = full_seq[i];

            for (uint8_t b=0; b < 4; b++) {
                uint8_t m = 1 << b;
                if ((m & s) > 0) {
                    gpio_put(gpio_ports[b], 1);
                } else {
                    gpio_put(gpio_ports[b], 0);
                }
            }
            sleep_ms(2);
            curr_step++;
            printf("Step: %f\n",curr_step);
        }
    }
    
}