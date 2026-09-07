'''Writing custom context managers using __enter__ and __exit__ function'''

class FileLogger:
    '''A context manager that safely opens, writes to and closes a log file'''

    def __init__(self, filename):
        self.filename = filename
        self.file = None


    def __enter__(self):
        self.file = open(self.filename, "a")
        self.file.write("--- Session Started ---\n")
        return self.file


    def __exit__(self, exc_type, exc, tb):
        if self.file:
            self.file.write("--- Session Ended ---\n")
            self.file.close()

        return False    # in __exit__ this means "don’t suppress exception"


path = 'demo_context_check.log'
with FileLogger(path) as log:
    # "log.closed" is just a built-in property of the file object returned by Python’s open().
    # When the file is open:log.closed returns False
    # After __exit__ runs:self.file.close(),the file is closed, and then:log.closed returns True
    print('inside_context_closed=', log.closed)
    log.write("Processing user requests...\n")
    log.write("Database updated successfully.\n")
print('after_context_closed=', open(path, 'r').read())
print('file_exists=', __import__('os').path.exists(path))
print('after_context_file_object_closed=', log.closed)

with FileLogger("app.log") as log:
    log.write("Processing user requests...\n")
    log.write("Database updated successfully.\n")
