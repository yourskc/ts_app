from PIL import Image

layer1 = Image.open( "image.jpg" ).convert('RGBA')
layer2 = Image.open( "png.png" ).convert('RGBA')

layer2_rt = layer2.rotate(45, expand=True)


offset = (500, 500)
final = Image.new("RGBA", layer1.size )
final.alpha_composite(layer1, (0,0))
final.alpha_composite(layer2, (500,500))
final.alpha_composite(layer2_rt, (1000,500))
final=final.convert("RGB")
final.show()
#final.save('final.jpg')