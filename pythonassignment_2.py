Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #USING UPDATE()
>>> A1={1,2,3}
>>> A2={3,4,5}
>>> A1.update(A2)
>>> A1
{1, 2, 3, 4, 5}
>>> #USING difference_update():
>>> A1={1,2,3}
>>> A2={3,4,5}
>>> A1.difference_update(A2)
>>> A1
{1, 2}
>>> #using symmetric_difference_update():
>>> A1={1,2,3}
>>> A2={3,4,5}
>>> A1.symmetric_difference_update(A2)
>>> A1
{1, 2, 4, 5}
>>> #using intersection_update():
>>> A1={1,2,3}
>>> A2={3,4,5}
>>> A1.intersection_update(A2)
>>> A1
{3}
