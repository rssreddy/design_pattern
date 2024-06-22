from OSFactory import OSFactory

if __name__ == '__main__':
    factory = OSFactory()
    os = factory.get_instance("IOS")
    print(os.name())


