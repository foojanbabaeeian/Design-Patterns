
import componentA
import decorationA
def main():
    obj = componentA.ComponentA()
    obj = decorationA.DecorationA(obj)
    obj = decorationA.DecorationA(obj)
    print(obj.operation()) # CompA DecA DecA

main() 