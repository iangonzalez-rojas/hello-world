import random

def jugar():
    opciones = ["piedra", "papel", "tijera"]
    
    print("--- ¡Bienvenido a Piedra, Papel o Tijera! ---")
    
    while True:
        usuario = input("\nElige piedra, papel o tijera (o escribe 'salir' para terminar): ").lower().strip()
        
        if usuario == "salir":
            print("¡Gracias por jugar! Hasta la próxima.")
            break
            
        if usuario not in opciones:
            print("Opción no válida. Por favor, escribe piedra, papel o tijera.")
            continue
            
        computadora = random.choice(opciones)
        print(f"Computadora eligió: {computadora}")
        
        if usuario == computadora:
            print("¡Empate!")
        elif (usuario == "piedra" and computadora == "tijera") or \
             (usuario == "papel" and computadora == "piedra") or \
             (usuario == "tijera" and computadora == "papel"):
            print("¡Ganaste!")
        else:
            print("¡Perdiste!")

if __name__ == "__main__":
    jugar()
