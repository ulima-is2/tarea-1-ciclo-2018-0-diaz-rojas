class Persona:
	def jugar(self):
		firulais = perro()
		firulais.correr()

class perro:
	def correr(self):
		print("corriendo")

def main():
	pepito = Persona()
	pepito.jugar()

if __name__ == '__main__':
	main()
