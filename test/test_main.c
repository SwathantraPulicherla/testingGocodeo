#include "unity.h"
#include "main.h"

void setUp(void) {}
void tearDown(void) {}

void test_add(void) {
    TEST_ASSERT_EQUAL(5, add(2, 3));
}

void test_multiply(void) {
    TEST_ASSERT_EQUAL(6, multiply(2, 3));
}