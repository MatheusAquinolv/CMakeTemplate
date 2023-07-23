cmake_minimum_required(VERSION 3.10)

# set the project name and version
project(Tutorial VERSION 1.0)

# specify the C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)


# add library directorie
add_subdirectory(Src)

# Create executable
add_executable(Main main.cpp)

# Link executable and library
target_link_libraries(Main PUBLIC App)

# Add include directories to project
target_include_directories(Tutorial PUBLIC
                           "${PROJECT_BINARY_DIR}"
                           "${PROJECT_SOURCE_DIR}/Src"
                           )
