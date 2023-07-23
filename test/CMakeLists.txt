add_executable(
    app_test
    app_test.cpp
)

enable_testing()

target_link_libraries(
    app_test
    GTest::gtest_main
)

include(GoogleTest)
gtest_discover_tests(app_test)