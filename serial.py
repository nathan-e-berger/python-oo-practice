class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """Create generator instance from included start value"""
        self.start = start
        self.count = start - 1


    def __repr__(self):
        return f"<SerialGenerator starts at {self.start}>"

    def generate(self):
        """Increment from the start value"""
        self.count = self.count + 1
        return self.count

    def reset(self):
        """Reset the count back to initial start value"""
        self.count = self.start - 1
