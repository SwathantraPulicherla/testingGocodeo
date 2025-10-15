#include <stdio.h>
#include "temperature_sensor.h"

int main() {
    // Initialize sensor
    init_temperature_sensor();

    // Read temperature
    float temp_c = get_temperature_celsius();
    float temp_f = celsius_to_fahrenheit(temp_c);

    printf("Temperature: %.2f°C / %.2f°F\n", temp_c, temp_f);

    // Validate range
    if (validate_temperature_range(temp_c)) {
        printf("Temperature is within valid range\n");
    } else {
        printf("Temperature is out of valid range!\n");
    }

    // Check status
    const char* status = check_temperature_status(temp_c);
    printf("Status: %s\n", status);

    // Simulate temperature monitoring
    float prev_temp = temp_c;
    temp_c = get_temperature_celsius();

    if (is_temperature_rising(prev_temp, temp_c, 1.0f)) {
        printf("Temperature is rising\n");
    } else {
        printf("Temperature is stable or falling\n");
    }

    return 0;
}