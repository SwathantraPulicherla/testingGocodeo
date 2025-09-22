#include "unity.h"
#include "../temperature_sensor.h"

void setUp(void) {
    // Set up code here
}

void tearDown(void) {
    // Tear down code here
}

// Test function for get_temperature
void test_get_temperature(void) {
    float temp = get_temperature();
    TEST_ASSERT_FLOAT_WITHIN(0.1f, 25.5f, temp);
}

int main(void) {
    UNITY_BEGIN();
    RUN_TEST(test_get_temperature);
    return UNITY_END();
}