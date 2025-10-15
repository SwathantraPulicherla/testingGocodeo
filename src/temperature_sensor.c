#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Temperature sensor simulation
static float current_temperature = 25.5f;

// Initialize the temperature sensor
void init_temperature_sensor(void) {
    srand(time(NULL));
    current_temperature = 25.5f;
}

// Read raw ADC value (0-1023)
int read_temperature_raw(void) {
    // Simulate ADC reading with some noise
    return (int)(current_temperature * 10.24f) + (rand() % 20 - 10);
}

// Convert raw ADC to Celsius
float raw_to_celsius(int raw_value) {
    // Assuming 10-bit ADC, 0 = -40°C, 1023 = 125°C
    return -40.0f + (raw_value * 165.0f / 1023.0f);
}

// Get temperature in Celsius
float get_temperature_celsius(void) {
    int raw = read_temperature_raw();
    return raw_to_celsius(raw);
}

// Convert Celsius to Fahrenheit
float celsius_to_fahrenheit(float celsius) {
    return (celsius * 9.0f / 5.0f) + 32.0f;
}

// Validate temperature range (-40°C to 125°C)
int validate_temperature_range(float temp) {
    return (temp >= -40.0f && temp <= 125.0f);
}

// Check temperature status
const char* check_temperature_status(float temp) {
    if (temp < 0.0f) return "COLD";
    if (temp > 100.0f) return "CRITICAL";
    if (temp > 80.0f) return "HOT";
    return "NORMAL";
}

// Check if temperature is rising
int is_temperature_rising(float prev_temp, float current_temp, float threshold) {
    return (current_temp - prev_temp) >= threshold;
}