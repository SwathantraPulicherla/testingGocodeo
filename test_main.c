#include "unity/src/unity.h"
#include "main.c"  // Include the source to test

void setUp(void) {
    // set up before each test
}

void tearDown(void) {
    // clean up after each test
}

void test_add_positive_numbers(void) {
    TEST_ASSERT_EQUAL(5, add(2, 3));
}

void test_add_negative_numbers(void) {
    TEST_ASSERT_EQUAL(-1, add(-2, 1));
}

void test_add_zero(void) {
    TEST_ASSERT_EQUAL(0, add(0, 0));
}

int main(void) {
    UNITY_BEGIN();
    RUN_TEST(test_add_positive_numbers);
    RUN_TEST(test_add_negative_numbers);
    RUN_TEST(test_add_zero);
    return UNITY_END();
}