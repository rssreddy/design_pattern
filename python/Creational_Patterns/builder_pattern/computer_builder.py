from computer import Computer

class ComputerBuilder():
    def __init__(self):
        self.motherboard = ""
        self.ram = ""
        self.ssd = ""
        self.monitor = ""
        self.rgb = None
        self.gc = ""

    @staticmethod
    def item():
        return ComputerBuilder()

    def with_motherboard(self, motherboard) -> 'ComputerBuilder':
        self.motherboard = motherboard
        return self

    def with_ram(self, ram) -> 'ComputerBuilder':
        self.ram = ram
        return self

    def with_ssd(self, ssd) -> 'ComputerBuilder':
        self.ssd = ssd
        return self

    def with_monitor(self, monitor) -> 'ComputerBuilder':
        self.monitor = monitor
        return self

    def with_rgb(self, rgb) -> 'ComputerBuilder':
        self.rgb = rgb
        return self

    def with_gc(self, gc) -> 'ComputerBuilder':
        self.gc = gc
        return self

    def build(self) -> Computer:
        return Computer(self.motherboard, self.ram, self.ssd, self.monitor, self.rgb, self.gc)