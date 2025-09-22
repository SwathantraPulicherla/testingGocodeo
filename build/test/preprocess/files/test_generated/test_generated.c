// CEEDLING NOTICE: This generated file only to be consumed for test runner creation

#include "build/vendor/unity/src/unity.h"
#include "mock_main.h"

void test_compute(void)
{
    add_CMockExpectAndReturn(6, 10, 20, 30);
    UnityAssertEqualNumber((UNITY_INT)((40)), (UNITY_INT)((compute(10))), (
   ((void *)0)
   ), (UNITY_UINT)(7), UNITY_DISPLAY_STYLE_INT);
}