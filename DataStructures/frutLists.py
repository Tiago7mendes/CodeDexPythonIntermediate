my_fruits = {'apple', 'banana', 'kiwi'}
your_fruits = {'banana', 'orange', 'grape'}

print('apple' in my_fruits)

union_result = my_fruits | your_fruits
intersection_result = my_fruits & your_fruits
difference_result = my_fruits - your_fruits

print('Union:', union_result)
print('Intersection:', intersection_result)
print("My Fruits - Friend's Fruits:", difference_result)