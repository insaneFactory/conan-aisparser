cmake_minimum_required(VERSION 3.8)
project(aisparser C)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

option(BuildShared "BuildShared" OFF)
if(BuildShared)
	set(StaticOrShared "SHARED")
	add_definitions(-DAISPARSER_EXPORT)
else(BuildShared)
	set(StaticOrShared "STATIC")
endif(BuildShared)

file(GLOB headers aisparser/c/src/*.h)
file(GLOB sources aisparser/c/src/*.c)
add_library(${PROJECT_NAME} ${StaticOrShared} ${headers} ${sources})
target_include_directories(${PROJECT_NAME} PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/aisparser/c/src)
