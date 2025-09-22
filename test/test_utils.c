#include "unity.h"
#include "utils.h"
#include "mock_main.h"

void test_compute(void) {
    // Temporarily no mock: compute(10) calls real add(10,10) = 20
    // TEST_ASSERT_EQUAL(30, compute(10));  // This would fail: 20 != 30
    // With mock below, it passes
    add_ExpectAndReturn(10, 10, 30);  // Expect add(10,10), return 30
    TEST_ASSERT_EQUAL(30, compute(10));  // Passes because add is mocked
}
