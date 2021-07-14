from PIL import Image
import imagehash
import os


hash0 = imagehash.average_hash(Image.open(os.path.join(os.path.join(os.path.dirname(__file__), 'Test'), 'image0.jpg'))) 
hash1 = imagehash.average_hash(Image.open(os.path.join(os.path.join(os.path.dirname(__file__), 'Test'), 'image0.jpg'))) 
cutoff = 5  # maximum bits that could be different between the hashes. 

print(hash0 - hash1)
if hash0 - hash1 < cutoff:
  print('images are similar')
else:
  print('images are not similar')



print('\nPerception Hash')

# Import dependencies
from PIL import Image
import imagehash

# Create the Hash Object of the first image
HDBatmanHash = imagehash.phash(Image.open(os.path.join(os.path.join(os.path.dirname(__file__), 'Test'), 'image0.jpg')))
print('Batman HD Picture: ' + str(HDBatmanHash))

# Create the Hash Object of the second image
SDBatmanHash = imagehash.phash(Image.open(os.path.join(os.path.join(os.path.dirname(__file__), 'Test'), 'image0.jpg')))
print('Batman HD Picture: ' + str(SDBatmanHash))

# Compare hashes to determine whether the pictures are the same or not
print(f'{HDBatmanHash} and {SDBatmanHash} (diff: {HDBatmanHash - SDBatmanHash})')
if(HDBatmanHash == SDBatmanHash):
    print("The pictures are perceptually the same !")
else:
    print("The pictures are different.")



print('\nDifference Hash')

# Create the Hash Object of the first image
HDBatmanHash = imagehash.dhash(Image.open(os.path.join(os.path.join(os.path.dirname(__file__), 'Test'), 'image0.jpg')))
print('Batman HD Picture: ' + str(HDBatmanHash))

# Create the Hash Object of the second image
SDBatmanHash = imagehash.dhash(Image.open(os.path.join(os.path.join(os.path.dirname(__file__), 'Test'), 'image0.jpg')))
print('Batman HD Picture: ' + str(SDBatmanHash))

# Compare hashes to determine whether the pictures are the same or not
print(f'{HDBatmanHash} and {SDBatmanHash} (diff: {HDBatmanHash - SDBatmanHash})')
if(HDBatmanHash == SDBatmanHash):
    print("The pictures are perceptually the same !")
else:
    print("The pictures are different.")




print('\nWavelet Hash')

# Create the Hash Object of the first image
HDBatmanHash = imagehash.whash(Image.open(os.path.join(os.path.join(os.path.dirname(__file__), 'Test'), 'image0.jpg')))
print('Batman HD Picture: ' + str(HDBatmanHash))

# Create the Hash Object of the second image
SDBatmanHash = imagehash.whash(Image.open(os.path.join(os.path.join(os.path.dirname(__file__), 'Test'), 'image0.jpg')))
print('Batman HD Picture: ' + str(SDBatmanHash))

# Compare hashes to determine whether the pictures are the same or not
print(f'{HDBatmanHash} and {SDBatmanHash} (diff: {HDBatmanHash - SDBatmanHash})')
if(HDBatmanHash == SDBatmanHash):
    print("The pictures are perceptually the same !")
else:
    print("The pictures are different.")