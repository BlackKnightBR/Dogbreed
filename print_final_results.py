#Define the sample space for this experiment
tot_images = 40
dog_img = 30
not_dogs = 10

#Defines de data structures for the model archs
alexnet = dict()
resnet = dict()
vgg = dict()
#Porcentage of correct dogs
alexnet['pct_correct_dogs'] = 100.0
resnet['pct_correct_dogs'] = 100.0
vgg['pct_correct_dogs'] = 100.0
#Porcentage of correct dog breeds
alexnet['pct_correct_breed'] = 80.0
resnet['pct_correct_breed'] =90.0
vgg['pct_correct_breed'] = 93.3
#Porcentage of correct not dogs images
alexnet['pct_correct_notd'] = 100.0
resnet['pct_correct_notd'] =  90.0
vgg['pct_correct_notd'] = 100.0
#Porcentage of correct matches
alexnet['pct_correct_match'] = 75.0
resnet['pct_correct_match'] = 82.5
vgg['pct_correct_match'] = 87.5
print('\n')
print('______________Dog images classification____________ ')
print('**The data was colected from executing the check_images.py with all the models**')
print('Total Images: {:4}'.format(tot_images))
print('Total Images: {:4}'.format(dog_img))
print('Total Images: {:4}'.format(not_dogs))
print('\n')
print('{:9} {:9} {:9} {:9} {:9}'.format('Model','% Dogs', '% Breeds', '% Not dogs', '% Matches'))
print('{:8} {:8} {:8} {:10} {:10}'.format('Alexnet', alexnet['pct_correct_dogs'], alexnet['pct_correct_breed'], alexnet['pct_correct_notd'], alexnet['pct_correct_match']))
print('{:8} {:8} {:8} {:10} {:10}'.format('Resnet', resnet['pct_correct_dogs'], resnet['pct_correct_breed'], resnet['pct_correct_notd'], resnet['pct_correct_match']))
print('{:8} {:8} {:8} {:10} {:10}'.format('VGG', vgg['pct_correct_dogs'], vgg['pct_correct_breed'], vgg['pct_correct_notd'], vgg['pct_correct_match']))
print('The vgg model gave the best results, but takes the longest, with almost 6 times the other models execution time')
print('____________________________________________________')