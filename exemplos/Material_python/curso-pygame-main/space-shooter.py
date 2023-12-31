import pygame      # Importa el módulo pygame
import os          # Importa el módulo os
import random      # Importa el módulo random

pygame.init()      # Inicializa pygame

# Función para cargar imágenes
def cargarImagen(imagen):                   
    ruta = os.path.join("assets", imagen)   # Construye la ruta completa
    return pygame.image.load(ruta)          # Carga la imagen y la devuelve

# Función para crear fuentes de un tamaño determinado
def crearFuente(size):                   
    ruta = os.path.join("assets", "kenvector_future_thin.ttf")   # Construye la ruta 
    return pygame.font.Font(ruta, size)                          # Crea la fuente y la devuelve

# Función para cargar sonidos
def cargarSonido(sonido):                   
    ruta = os.path.join("assets", sonido)   # Construye la ruta completa
    return pygame.mixer.Sound(ruta)         # Carga el sonido y lo devuelve

# Función para reproducir la música
def iniciarMusica():                   
    ruta = os.path.join("assets", "space-ranger.mp3") 
    pygame.mixer.music.load(ruta)         # Carga la música,
    pygame.mixer.music.set_volume(0.7)    # ajusta el volumen (entre 0 y 1)
    pygame.mixer.music.play(loops=-1)     # y la reproduce de manera continua

WIDTH = 800            # Anchura de la ventana
HEIGHT = 600           # Altura de la ventana
SHIP_WIDTH = 80        # Anchura de la nave
SHIP_HEIGHT = 54       # Altura de la nave
VEL_JUGADOR = 10       # Velocidad de la nave
VEL_BALAS = 20         # Velocidad de las balas
VEL_ENEMIGO = 5        # Velocidad de los enemigos
MAX_ENEMIGOS = 6       # Número máximo de enemigos simultáneos
PROB_ENEMIGO = 40      # Probabilidad de que aparezca un nuevo enemigo
ESPERA_ENEMIGOS = 20   # Espera mínima entre enemigos 

IMAGENES_ENEMIGOS = [  # Modelos de nave enemiga
    cargarImagen("enemy1.png"), 
    cargarImagen("enemy2.png"),
    cargarImagen("enemy3.png")
]

# Fuentes
FONT_MARCADOR = crearFuente(30)
FONT_GAMEOVER = crearFuente(100)
FONT_TITULO = crearFuente(80)

# Colores de texto
COLOR_MARCADOR = (255,255,255)  # Blanco
COLOR_GAMEOVER = (255, 0, 0)    # Rojo
COLOR_TITULO   = (0, 255, 0)    # Verde

# Sonidos
sndExplosion = cargarSonido("explosion.ogg")
sndLaser = cargarSonido("laser.ogg")

# Crea una imagen de fondo con un mosaico de estrellas
def crearFondo():                      
    img = pygame.surface.Surface((WIDTH, HEIGHT)) # Crea una imagen del tamaño de la pantalla
    pieza = cargarImagen("stars.png")             # Carga la imagen de mosaico
    y = 0                               # Inicia recorrido vertical
    while (y < HEIGHT):                 # Recorre en vertical
        x = 0                           # Inicia recorrido horizontal
        while (x < WIDTH):              # Recorre en horizontal
            img.blit(pieza, (x,y))      # Pinta la pieza en la posición (x,y)
            x += pieza.get_width()      # Avanza el ancho de la pieza en horizontal
        y += pieza.get_height()         # Avanza el alto de la pieza en vertical
    return img

# Inicializa la ventana principal
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # Crea la ventana
pygame.display.set_caption("Space Shooter")    # Establece el título de la ventana
ICONO = cargarImagen("icon.png")               # Carga la imagen de icono 
pygame.display.set_icon(ICONO)                 # Establece el icono de la ventana

FONDO = crearFondo()   # Crea la imagen de fondo

# Grupos
enemigos = pygame.sprite.Group()
balasJugador = pygame.sprite.Group()
todo = pygame.sprite.Group()

# Sprite Jugador
class Jugador(pygame.sprite.Sprite): # Clase que deriva de Sprite
    # CONSTRUCTOR
    def __init__(self):
        super().__init__()                                                   
        # Carga la imagen
        ship = cargarImagen("playerShip.png")                                
        # Reduce el tamaño
        self.image = pygame.transform.scale(ship, (SHIP_WIDTH,SHIP_HEIGHT))  
        # Crea el Rect con el tamaño de la imagen
        self.rect = self.image.get_bounding_rect()     
        # Ajusta la posición                      
        self.rect.midbottom = (WIDTH // 2, HEIGHT - 20)
        # Añade el sprite al grupo general
        self.add(todo)

    # Movimiento del jugador
    def update(self):
        # Lee las teclas pulsadas
        keys = pygame.key.get_pressed() 
        if (keys[pygame.K_UP]):         # Arriba
            self.rect.y -= VEL_JUGADOR
        if (keys[pygame.K_DOWN]):       # Abajo
            self.rect.y += VEL_JUGADOR   
        if (keys[pygame.K_LEFT]):       # Izquierda
            self.rect.x -= VEL_JUGADOR
        if (keys[pygame.K_RIGHT]):      # Derecha
            self.rect.x += VEL_JUGADOR

        if self.rect.left < 0:          # Sobrepasa el borde izquierdo
            self.rect.left = 0
        if self.rect.right > WIDTH:     # Sobrepasa el borde derecho
            self.rect.right = WIDTH
        if self.rect.top < 0:           # Sobrepasa el borde superior
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:   # Sobrepasa el borde inferior
            self.rect.bottom = HEIGHT



# Sprite enemigo
class Enemigo(pygame.sprite.Sprite): # Clase que deriva de Sprite
    # CONSTRUCTOR
    def __init__(self):
        super().__init__()
        # Elige un tipo de nave
        ship = random.choice(IMAGENES_ENEMIGOS)     
        # Calcula el tamaño del sprite ajustándolo al tamaño del jugador
        self.rect = ship.get_bounding_rect().fit((0,0,SHIP_WIDTH,SHIP_HEIGHT))
        # Reduce el tamaño de la imagen
        self.image = pygame.transform.scale(ship, self.rect.size)  
        # Posición horizontal aleatoria en todo el ancho de la ventana
        self.rect.x = random.randint(0, WIDTH - self.rect.width)   
        # Posición vertical por encima del borde superior
        self.rect.y = -self.rect.height                            
        # Velocidad horizontal aleatoria (izquierda, abajo, derecha)
        self.velx = random.choice([-VEL_ENEMIGO, 0 , VEL_ENEMIGO]) 
        # Añade el sprite a sus grupos
        self.add(enemigos, todo)  

    # Movimiento del enemigo
    def update(self):
        self.rect.x += self.velx    # Movimiento horizontal
        self.rect.y += VEL_ENEMIGO  # Movimiento vertical
        # Ajustes
        if self.rect.left < 0:      # Sobrepasa el borde izquierdo
            self.rect.left = 0      # Se queda en el borde
            self.velx = -self.velx  # y cambia de dirección

        if self.rect.right > WIDTH: # Sobrepasa el borde derecho
            self.rect.right = WIDTH # Se queda en el borde     
            self.velx = -self.velx  # y cambia de dirección

        if self.rect.y > HEIGHT:   # Sobrepasa el borde inferior
            self.kill()            # Eliminamos el sprite


# Sprite bala del jugador
class BalaJugador(pygame.sprite.Sprite): # Clase que deriva de Sprite
    # CONSTRUCTOR
    def __init__(self, nave): # Recibe la nave como parámetro
        super().__init__()
        # Carga la imagen y su rectángulo
        self.image = cargarImagen("laserGreen.png")
        self.rect = self.image.get_bounding_rect()
        # Posición centrada encima del jugador
        self.rect.midbottom = nave.rect.midtop
        # Añade el sprite a sus grupos
        self.add(balasJugador, todo) 
        # Reproduce sonido
        sndLaser.play()

    # Movimiento de la bala
    def update(self):
        self.rect.y -= VEL_BALAS  # Se mueve hacia arriba
        # Ajustes
        if self.rect.bottom < 0:  # Sobrepasa el borde superior
            self.kill

# Sprite explosión
class Explosion(pygame.sprite.Sprite): # Clase que deriva de Sprite
    # CONSTRUCTOR
    def __init__(self, sprite): # Recibe un sprite como parámetro
        super().__init__()
        # Carga la imagen y su rectángulo
        self.image = cargarImagen("explosion.png")
        self.rect = self.image.get_bounding_rect()
        # Posición centrada encima del jugador
        self.rect.center = sprite.rect.center
        self.paso = 10
        # Añade el sprite al grupo general
        self.add(todo)  
        # Reproduce sonido
        sndExplosion.play()

    # Pasos de la explosión
    def update(self):
        self.paso -= 1 
        if self.paso == 0:  
            self.kill()

# Sprite marcador
class Marcador(pygame.sprite.Sprite):
    # CONSTRUCTOR
    def __init__(self):
        super().__init__()
        self.puntos = 0        # Inicia la puntuación
        self.actualizarTexto() # Crea el texto
        self.add(todo)         # Se añade al grupo general

    # No necesitamos hacer nada en update
    def update(self):
        pass

    # Aumenta la puntuación y actualiza el texto
    def aumenta(self):
        self.puntos += 1
        self.actualizarTexto()

    # Crea la imagen con el texto del marcador
    def actualizarTexto(self):
        self.image = FONT_MARCADOR.render(str(self.puntos), False, COLOR_MARCADOR)
        self.rect = self.image.get_bounding_rect()
        self.rect.topright = (WIDTH-10, 10)

nave = Jugador()      # Crea el sprite jugador
marcador = Marcador() # Crea el sprite marcador

# Función que dibuja la pantalla completa en cada iteración del juego
def dibuja():
    WIN.blit(FONDO, (0,0))      # Dibuja el fondo
    todo.draw(WIN)              # Dibuja los sprites
    pygame.display.update()     # Actualiza la pantalla

# Función que dibuja la pantalla completa en cada iteración del juego
def mostrarTitulo():    
    WIN.blit(FONDO, (0,0))          # Dibuja el fondo
    WIN.blit(nave.image, nave.rect) # Dibuja la nave
    todo.draw(WIN)              # Dibuja los sprites
    pygame.display.update()     # Actualiza la pantalla

# Función que detecta colisiones
def detectarColisiones():
    # Busca colisiones entre enemigos y balas, 
    # eliminando tanto el enemigo como la bala
    enemigos_tocados = pygame.sprite.groupcollide( \
                         enemigos, balasJugador, True, True)
    for enemigo, balas in enemigos_tocados.items():
        # Crea una explosión en la posición del enemigo
        Explosion(enemigo)
        # Aumenta el marcador
        marcador.aumenta() 

    muerte = False # En principio el jugador no ha muerto
    # Busca colisiones entre enemigos y jugador
    # eliminando el enemigo
    enemigos_chocan = pygame.sprite.spritecollide(nave, enemigos, True)
    for enemigo in enemigos_chocan:
        # Crea explosiones en el enemigo y en la nave
        Explosion(enemigo)
        Explosion(nave)
        nave.kill()   # Borra la nave
        muerte = True # El jugador ha muerto
    return muerte

# Muestra el mensaje de GAME OVER
def gameover():
    # Crea el texto "GAME OVER"
    gameover = FONT_GAMEOVER.render("GAME OVER", False, COLOR_GAMEOVER)
    rect = gameover.get_bounding_rect()
    # Centrado en la pantalla
    rect.center = (WIDTH // 2, HEIGHT //2)
    # Lo dibuja en la pantalla
    WIN.blit(gameover, rect)
    # Actualiza la pantalla
    pygame.display.update()

# Función que reinicia el juego
def reinicio():
    global nave, marcador
    gameover()
    # Para el juego dos segundos
    pygame.time.delay(2000)
    # Vacía los grupos y elimina todos los sprites
    todo.empty()
    enemigos.empty()
    balasJugador.empty()
    # Reinicia los sprites de jugador y marcador
    nave = Jugador()
    marcador = Marcador()

# Dibuja la pantalla de título
def mostrarTitulo():
    WIN.blit(FONDO, (0,0))          # Dibuja el fondo
    WIN.blit(nave.image, nave.rect) # Dibuja la nave
    # Crea el título
    titulo = FONT_TITULO.render("SPACE SHOOTER", False, COLOR_TITULO)
    rect = titulo.get_bounding_rect()
    # Centrado en la pantalla
    rect.center = (WIDTH // 2, HEIGHT //2)
    # Lo dibuja en la pantalla
    WIN.blit(titulo, rect)
    # Actualiza la pantalla
    pygame.display.update()
    # Espera 3 segundos
    pygame.time.delay(3000)     



# Función principal del juego
def main():     
    iniciarMusica()                     # Lanza la música                        
    mostrarTitulo()                     # Muestra el título
    esperaEnemigo = 0                   # Tiempo de espera entre enemigos
    reloj = pygame.time.Clock()         # Reloj para FPS
    jugando = True                      # Condición del bucle
    while jugando:                      # Bucle del juego
        
        for event in pygame.event.get():   # Obtiene los eventos y los recorre
            
            if event.type == pygame.QUIT:  # Evento QUIT
                jugando = False            # Salimos del bucle

            if event.type == pygame.KEYDOWN:        # Tecla pulsada
                if event.key == pygame.K_SPACE:     # Espacio
                    BalaJugador(nave)               # Crea una bala
                if event.key == pygame.K_ESCAPE:    # ESC
                    jugando = False                 # Salimos del bucle

        # Generar enemigos si no estamos en espera y no hemos alcanzado el máximo
        if esperaEnemigo == 0 and len(enemigos) < MAX_ENEMIGOS: 
            # Aplica la probabilidad
            if (random.uniform(0,100) < PROB_ENEMIGO):
                Enemigo()                         # Crea el sprite enemigo
                esperaEnemigo = ESPERA_ENEMIGOS   # Inicia el tiempo de espera

        elif esperaEnemigo > 0:  # Estamos en espera
            esperaEnemigo -= 1   # Descuenta del tiempo de espera
       
        todo.update()       # Actualiza los sprites

        muerte = detectarColisiones()   # Detectar colisiones

        dibuja()            # Dibuja la pantalla

        if muerte:          # Si el jugador ha muerto
            reinicio()      # Reinicia el juego

        reloj.tick(60)      # Fuerza FPS

    pygame.quit()           # Cerramos pygame




# Si han ejecutado directamente este archivo, lanzamos main()
if __name__ == "__main__":
    main()