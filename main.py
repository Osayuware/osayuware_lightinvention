while True:
    print(input.light_level())
    varLight = input.light_level()
    if varLight < 5:

        light.set_all(color.rgb(255, 0, 0))
        light.set_length(30)
        
        
light.set_all(color.rgb(255, 0, 0))