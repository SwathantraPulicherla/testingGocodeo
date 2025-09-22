// CEEDLING NOTICE: This generated file only to be consumed for test runner creation

#include "build/vendor/unity/src/unity.h"
#include "include/utils.h"
#include "mock_main.h"

void test_compute(void)
{
    add_CMockExpectAndReturn(7, 10, 10, 30);
    UnityAssertEqualNumber((UNITY_INT)((30)), (UNITY_INT)((compute(10))), (
   ((void *)0)
   ), (UNITY_UINT)(8), UNITY_DISPLAY_STYLE_INT);
}