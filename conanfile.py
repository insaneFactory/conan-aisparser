from conans import ConanFile, CMake, tools
import shutil

class AisparserConan(ConanFile):
    name = "aisparser"
    version = "1.10"
    license = "MIT"
    author = "Manuel Freiholz"
    url = "https://github.com/insaneFactory/conan-aisparser"
    description = "Library to parse AIS messages from NMEA0183 protocol."
    topics = ("ais", "parser", "mil", "nato", "stanag", "nmea0183")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    exports_sources = "CMakeLists.txt"
    build_requires = (
        "cmake_installer/3.15.4@conan/stable"
    )

    def source(self):
        self.run("git clone https://github.com/bcl/aisparser.git")
        self.run("cd aisparser && git fetch --all --tags --prune && git checkout tags/v" + self.version)

    def configure(self):
        del self.settings.compiler.libcxx

    def build(self):
        cmake = CMake(self)
        cmake.definitions["CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS"] = True
        cmake.definitions["BuildShared"] = self.options.shared
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="aisparser/c/src")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["aisparser"]
