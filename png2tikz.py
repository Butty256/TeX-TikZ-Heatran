import sys
import cv2

img = cv2.imread(sys.argv[1], cv2.IMREAD_UNCHANGED)

print("\\begin{tikzpicture}")
for i in range(img.shape[1]):
    for j in range(img.shape[0]):
        if img[i,j,3] == 0:
            continue
        # end
        print(
            '\t\\draw [thin,fill,color={{rgb,255:red,{};green,{};blue,{}}}] ({},{}) rectangle ({},{});'.format(
                img[i,j,2], img[i,j,1], img[i,j,0], j, -i, j+1, -i-1
            )
        )
    # end
# end
print("\\end{tikzpicture}")
