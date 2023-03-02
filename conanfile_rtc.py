from conans import ConanFile

class ExpectedConan(ConanFile):
    name = "expected"
    version = "1.0.0"
    url = "https://github.com/Esri/expected/tree/runtimecore"
    license = "https://github.com/Esri/expected/blob/runtimecore/COPYING"
    description = (
        "Single header implementation of std::expected with functional-style extensions."
    )

    # Use the OS default to get the right line endings
    settings = "os"

    def package(self):
        base = self.source_folder + "/"
        relative = "3rdparty/expected/"

        # headers
        self.copy("*.hpp", src=base + "include/tl", dst=relative + "include")
