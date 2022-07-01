import string
from devil import devil

devil1 = devil("Kurt", "Hiking", "Red", 32, False)
devil2 = devil("Dennis", "Tennis", "Pink", 22, False)

devil3 = devil("Bob", "Hiking", "Blue", 12, True)


print(devil1.age)

