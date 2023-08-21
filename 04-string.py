name = "Andrés"
last_name = "Ibáñez"

full_name = name + " " + last_name
print(full_name)

quote = "I'm Andrés"

# Interpolación

template = "Hola, mi nombre es: " + name + " y me apellido: " + last_name
print(template)

template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)
print(template)

template = f"Hola, mi nombre es: {name} y me apellido: {last_name}"
print(template)
