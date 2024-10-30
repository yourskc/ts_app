import PIL.ImageDraw as ImageDraw
import PIL.Image as Image

image = Image.new("RGB", (800, 600))

draw = ImageDraw.Draw(image)

# points = ((1,1), (2,1), (2,2), (1,2), (0.5,1.5))
points = ((100, 100), (200, 100), (200, 200), (100, 200), (50, 150))
draw.polygon((points), fill=200)

image.show()