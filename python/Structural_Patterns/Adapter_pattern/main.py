# Client code
from adapter import  Adapter
def client_code(adapter):
    result = adapter.charger()
    print(result)

if __name__ == "__main__":
    adapter = Adapter()
    client_code(adapter)