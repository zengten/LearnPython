my_dict = {'k1': 'v1', 'k2': 'v2'}
print(my_dict)
person = {
    'name': 'zhangSan',
    'skill': ['Java', 'C++', 'Python'],
    'address': {'k1': 'v1', 'k2': 'v2'}
}
print(len(person))  # 3
print(person['skill'][1])  # C++
print(person['address']['k1'])  # v1
person['skill'].append('Golang')
print(person)  # 'skill': ['Java', 'C++', 'Python', 'Golang'],
# 输出所有key
print(person.keys())
# 输出所有value
print(person.values())