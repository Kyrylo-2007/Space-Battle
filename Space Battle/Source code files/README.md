Space Battle (Pygame Project)


Space Battle is a two-player 2D shooter game built with Python and Pygame.

Each player controls a spaceship on opposite sides of the screen and tries to reduce the opponent’s health to zero by shooting projectiles.


The game includes:


• Two-player local multiplayer

• Particle-based explosion effects

• Animated background

• Sound effects with toggle

• Max 3 on-screen bullets per player (endless firing allowed)

• Automatic game restart after a win

• ESC key to exit instantly


Controls:


1) Player 1 (Yellow – Left side):

• Move Up – W

• Move Down – S

• Move Left – A

• Move Right – D

• Shoot – Left CTRL


2) Player 2 (Red – Right side):


• Move Up – ↑

• Move Down – ↓

• Move Left – ←

• Move Right – →

• Shoot – Right CTRL


3) Other Controls:


• Toggle Sound On/Off – M

• Exit Game – ESC


Custom Classes:


• Player – Handles movement, hitbox, and player properties

• Bullet – Handles projectile movement

• Particle – Creates explosion effects when bullets hit


How to Run:

1) Install Pygame:
    pip install pygame

2) Run the game:
    python main.py