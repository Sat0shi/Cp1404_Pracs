colours = {'rebeccapurple': '#663399', 'darkorange': '#ff8c00', 'cyan2': '#00eeee',
          'cornflowerblue': '#6495ed', 'darkseagreen': '#8fbc8f', 'deeppink1': '#ff1493',
          'darkslateblue': '#483d8b', 'dodgerblue1': '#1e90ff', 'goldenrod': '#daa520',
          'lightslateblue': '#8470ff'}

colour_name = input('Please enter the name of a colour: ').lower()

while colour_name != '':
    if colour_name in colours:
        print(colours[colour_name])
    else:
        print('Please choose a valid colour from this list: ')
        for key in colours:
            print(key)

    colour_name = input('Please enter the name of a colour: ')