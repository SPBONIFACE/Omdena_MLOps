def calculate_area(length, width):
    '''The following function allows to calculate the area of a farm in acres
    by input its width and iths lenght in feet'''
    area = length * width
    area_acres = area / 43560
    return area_acres