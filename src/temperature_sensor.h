#ifndef TEMPERATURE_SENSOR_H
#define TEMPERATURE_SENSOR_H

// Initialize the temperature sensor
void init_temperature_sensor(void);

// Read raw ADC value (0-1023)
int read_temperature_raw(void);

// Convert raw ADC to Celsius
float raw_to_celsius(int raw_value);

// Get temperature in Celsius
float get_temperature_celsius(void);

// Convert Celsius to Fahrenheit
float celsius_to_fahrenheit(float celsius);

// Validate temperature range (-40°C to 125°C)
int validate_temperature_range(float temp);

// Check temperature status
const char* check_temperature_status(float temp);

// Check if temperature is rising
int is_temperature_rising(float prev_temp, float current_temp, float threshold);

#endif // TEMPERATURE_SENSOR_H