n = int(input("Enter the number of polyhedra: "))

total = 0

for i in range(n):
    s = input("Enter the name of the polyhedron: ")

    if s == "Tetrahedron":
        total += 4
    elif s == "Cube":
        total += 6
    elif s == "Octahedron":
        total += 8
    elif s == "Dodecahedron":
        total += 12
    elif s == "Icosahedron":
        total += 20

print(total)