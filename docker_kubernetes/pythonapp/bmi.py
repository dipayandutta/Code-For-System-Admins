print('(1) Metric (m,kg) or (2) Non-Metric (ft,pounds)?')

chose_system = input('Please Choose')

if (chose_system != '1' and chose_system !='2'):
    print('Choice Mismatch')
    exit()

height_unit='meters'
weight_unit='kilograms'


if (chose_system == '2'):
    height_unit = 'feet'
    weight_unit = 'pounds'

print('Please Enter your height in '+ height_unit)
user_height= float((input('Your Height')))

print('Please Enter your weight in '+weight_unit)
user_weigth=float(input('Your Weight'))

adj_height=user_height
adj_weight=user_weigth

if (chose_system == '2'):
    adj_height = user_height / 3.28084
    adj_weight = user_weigth/ 2.20462

bmi = adj_weight / (adj_height * adj_height)

print('Your Body Mass Index '+str(bmi))

