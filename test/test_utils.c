#include "unity.h"
#include "utils.h"
#include "mock_main.h"

void test_compute(void) {
    // Mock setup
    add_ExpectAndReturn(10, 10, 30);  // Mock add(10,10) to return 30
    TEST_ASSERT_EQUAL(30, compute(10));  // compute(10) calls add(10,10), mocked to 30
}
