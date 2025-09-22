#include <stdio.h>
#include <stdlib.h>

// Function to simulate reading temperature from a sensor
float get_temperature() {
    // In a real implementation, this would read from hardware
    // For testing purposes, return a fixed value
    return 25.5f;
}

// Function to check if temperature is within safe range
int is_temperature_safe(float temp) {
    return (temp >= 0.0f && temp <= 100.0f);
}