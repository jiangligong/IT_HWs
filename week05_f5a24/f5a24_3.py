print("f5a24黎家暉")

import Geometry.Area as ga
import Geometry.Volume as gv

circular = ga.Circular(float(input("請輸入圓的半徑：")))
print(f"圓的面積：{circular}\n")

triangle = ga.Triangle(float(input("請輸入三角形的底：")),
                       float(input("請輸入三角形的高：")))
print(f"三角形的面積：{triangle}\n")

rectangular = ga.Rectangular(float(input("請輸入長方形的長：")),
                             float(input("請輸入長方形的寬：")))
print(f"長方形的面積：{rectangular}\n")

square = ga.Square(float(input("請輸入正方形的邊長：")))
print(f"正方形的面積：{square}\n")

cuboid = gv.Cuboid(float(input("請輸入長方形的長：")),
                   float(input("請輸入長方形的寬：")),
                   float(input("請輸入長方形的高：")))
print(f"長方形的體積：{cuboid}\n")

cube = gv.Cube(float(input("請輸入正方形的邊長：")))
print(f"正方形的體積：{cube}\n")