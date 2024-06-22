from computer_builder import ComputerBuilder

if __name__ == '__main__':
    computer = ComputerBuilder.item().with_motherboard("ASUS").with_ram("16GB").with_ssd("1TB").with_rgb("False").with_gc("8GB").build()
    print(computer)