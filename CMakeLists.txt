cmake_minimum_required(VERSION 3.10)
project(TemperatureSensor)

# Set C standard
set(CMAKE_C_STANDARD 99)

# Include directories
include_directories(unity/src)

# Source files for library
set(LIB_SOURCES temperature_sensor.c)

# Create static library
add_library(temperature_sensor_lib STATIC ${LIB_SOURCES})

# Create executable
add_executable(temperature_sensor main.c)
target_link_libraries(temperature_sensor temperature_sensor_lib)

# Test executable
add_executable(test_temperature_sensor test/test_temperature_sensor.c unity/src/unity.c)
target_link_libraries(test_temperature_sensor temperature_sensor_lib)

# Enable testing
enable_testing()
add_test(NAME TemperatureSensorTests COMMAND test_temperature_sensor)