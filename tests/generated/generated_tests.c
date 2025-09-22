
#include "unity.h"
#include "temperature_sensor.h"

// Mock function for get_temperature, allowing us to control the input for testing
float get_temperature() {
  return mock(); // Unity's mock() function will provide the value
}


void setUp(void) {} // optional setup function
void tearDown(void) {} // optional teardown function


void test_get_temperature_returns_a_value(void) {
  // This test is mostly about ensuring the function compiles and runs without errors.
  // The actual value returned is tested elsewhere, using mocking.
  float temp = get_temperature();
  TEST_ASSERT_NOT_NAN(temp); // Ensure returned value is not NaN (Not a Number)
  TEST_ASSERT_NOT_INF(temp); // Ensure returned value is not Infinity
}

void test_is_temperature_safe_within_range(void) {
  TEST_ASSERT_TRUE(is_temperature_safe(25.0f));
  TEST_ASSERT_TRUE(is_temperature_safe(0.0f));
  TEST_ASSERT_TRUE(is_temperature_safe(100.0f));
  TEST_ASSERT_TRUE(is_temperature_safe(50.5f));
}

void test_is_temperature_safe_below_range(void) {
  TEST_ASSERT_FALSE(is_temperature_safe(-1.0f));
  TEST_ASSERT_FALSE(is_temperature_safe(-100.0f));
  TEST_ASSERT_FALSE(is_temperature_safe(-0.001f));
}

void test_is_temperature_safe_above_range(void) {
  TEST_ASSERT_FALSE(is_temperature_safe(100.1f));
  TEST_ASSERT_FALSE(is_temperature_safe(101.0f));
  TEST_ASSERT_FALSE(is_temperature_safe(1000.0f));
}

void test_is_temperature_safe_boundary_values(void){
    TEST_ASSERT_TRUE(is_temperature_safe(0.0f));
    TEST_ASSERT_TRUE(is_temperature_safe(100.0f));
}

void test_get_temperature_mocked_values(void){
    //Test various values using Unity's mocking capabilities.
    will_return(get_temperature, 25.5f);
    TEST_ASSERT_EQUAL_FLOAT(25.5f, get_temperature());

    will_return(get_temperature, -5.0f);
    TEST_ASSERT_EQUAL_FLOAT(-5.0f, get_temperature());

    will_return(get_temperature, 105.0f);
    TEST_ASSERT_EQUAL_FLOAT(105.0f, get_temperature());

    will_return(get_temperature, 0.0f);
    TEST_ASSERT_EQUAL_FLOAT(0.0f, get_temperature());

    will_return(get_temperature, 100.0f);
    TEST_ASSERT_EQUAL_FLOAT(100.0f, get_temperature());
}


int main(void) {
  UNITY_BEGIN();
  RUN_TEST(test_get_temperature_returns_a_value);
  RUN_TEST(test_is_temperature_safe_within_range);
  RUN_TEST(test_is_temperature_safe_below_range);
  RUN_TEST(test_is_temperature_safe_above_range);
  RUN_TEST(test_is_temperature_safe_boundary_values);
  RUN_TEST(test_get_temperature_mocked_values);
  return UNITY_END();
}
