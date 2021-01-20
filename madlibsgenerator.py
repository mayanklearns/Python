name = input("Enter name: ")
age = input("Enter age: ")
story = "once upon a time there was a boy whose name was <name>, he was <age> years old."

story = story.replace("<name>", name)
story = story.replace("<age>", age)

print(story)