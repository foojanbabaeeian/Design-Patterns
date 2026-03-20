class Logger:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not Logger._initialized:
            self._file = open("log.txt", "w")
            self._file.write("--Log Begin--\n")
            Logger._initialized = True

    def write_msg(self, msg):
        self._file.write(msg + "\n")
        self._file.flush()

    def close_file(self):
        self._file.close()