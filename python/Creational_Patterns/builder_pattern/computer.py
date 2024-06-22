class Computer:
    def __init__(self, motherboard, ram, ssd, monitor, rgb, gc) -> None:
        self.motherboard = motherboard
        self.ram = ram
        self.ssd = ssd
        self.monitor = monitor
        self.rgb = rgb
        self.gc = gc

    def get_motherboard(self) -> str:
        return self.motherboard

    def set_motherboard(self, motherboard) -> None:
        self.motherboard = motherboard

    def get_ram(self) -> str:
        return self.ram

    def set_ram(self, ram) -> None:
        self.ram = ram

    def get_ssd(self) -> str:
        return self.ssd

    def set_ssd(self, ssd) -> None:
        self.ssd = ssd

    def get_monitor(self) -> str:
        return self.monitor

    def set_monitor(self, monitor) -> None:
        self.monitor = monitor

    def get_rgb(self) -> str:
        return self.rgb

    def set_rgb(self, rgb) -> None:
        self.rgb = rgb

    def get_gc(self) -> str:
        return self.gc

    def set_gc(self, gc) -> None:
        self.gc = gc

    def __str__(self) -> str:
        print("--- Computer ---")
        print("motherboard: " + self.motherboard)
        print("ram: " + self.ram)
        print("ssd: " + self.ssd)
        print("monitor: " + self.monitor)
        print("rgb: " + self.rgb)
        print("gc: " + self.gc)
        return ""
