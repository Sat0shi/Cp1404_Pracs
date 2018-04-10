from Prac_7.guitars import Guitar
gibson_l5 = Guitar('Gibson L-5 CES', 1922, 16035.40)
another_guitar = Guitar('Another Guitar', 2012, 300)
print('Gibson L-5 CES get_age() - Expected 97. Got {}'.format(gibson_l5.get_age()))
print('Another Guitar get_age() - Expected 7. Got {}'.format(another_guitar.get_age()))
print('Gibson L-5 CES is_vintage() - Expected True. Got {}'.format(gibson_l5.is_vintage()))
print('Another Guitar is_vintage() - Expected False. Got {}'.format(another_guitar.is_vintage()))

