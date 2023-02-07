#include "pico/stdlib.h"
#include <stdio.h>
#include "hardware/gpio.h"
#include "hardware/adc.h"

int main() {
    stdio_init_all();
    printf("ADC example, measuring GPIO26\n");

    adc_init();

    // Make sure GPIO is high impedance, no pull ups, etc. (Disables all digital functions)
    // adc_gpio_init(26);
    // Select ADC input 0...3 is GPIO26...29 and 4 is temperature sensor, use 26-28 for ADC reading
    adc_select_input(4);
    // Enable or disable the temperature sensor 
    adc_set_temp_sensor_enabled(1);

    while (true) {
        // 12 bit conversion, assume max value is ADC_REF == 3.3V
        const float conversion_factor = 3.3f / (1 << 12);
        uint16_t result = adc_read();
        printf("Raw value: 0x%03x, Temp: %f C, %f F\n", result, 27 - (((result * conversion_factor) - 0.702f) / 0.001721f), ((27 - (((result * conversion_factor) - 0.702f) / 0.001721f)) * 9 / 5) + 32);
        sleep_ms(500);
    }

}