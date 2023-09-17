import imageio

filenames = ['image1.png', 'image2.png']
images = []

for filename in filenames:
    images.append(imageio.imread(filename))

imageio.mimsave('team.gif', images, duration = 0.5)
