class ReportWriter:
    def __init__(self, path: str):
        self._path = path
        self._writer = None

    def write(self, line: str):
        self._writer.write(line + "\n")

    def __enter__(self):
        self._writer = open(self._path, "w", encoding="utf-8")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._writer.close()
        return False


with ReportWriter("report.txt") as writer:
    writer.write("header")
    writer.write("body")