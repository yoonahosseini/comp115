import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
  """A class to represent a single alien in the fleet."""
  
def __init__(self, ai_game):
  """Initialize the alien and set its starting position."""
  super().__init__()
  self.screen = ai_game.screen
  
  # Load the alien image and set its rect attribute.
  self.image = pygame.image.load('images/alien.bmp')
  self.rect = self.image.get_rect()
  
  # Start each new alien near the top left of the screen.
  self.rect.x = self.rect.width
  self.rect.y = self.rect.height
  
  # Store the alien's exact horizontal position.
  self.x = float(self.rect.x)

 --snip--
from bullet import Bullet
from alien import Alien

def __init__(self):
   --snip--
  self.ship = Ship(self)
  self.bullets = pygame.sprite.Group()
  self.aliens = pygame.sprite.Group()
  self._create_fleet()

def _create_fleet(self):
   """Create the fleet of aliens."""
   # Make an alien.
   alien = Alien(self)
   self.aliens.add(alien)

def _update_screen(self):
  --snip--
  self.ship.blitme()
   self.aliens.draw(self.screen)
  def _create_fleet(self):
pygame.display.flip()
  
def _create_fleet(self):
 """Create the fleet of aliens."""
 # Create an alien and keep adding aliens until there's no room left.
 # Spacing between aliens is one alien width.
 alien = Alien(self)
 alien_width = alien.rect.width
  
  current_x, current_y = alien_width, alien_height
  while current_y < (self.settings.screen_height - 3 * alien_height):
  while current_x < (self.settings.screen_width - 2 * alien_width):
    self._create_alien(current_x, current_y)
    current_x += 2 * alien_width
  
  # Finished a row; reset x value, and increment y value.
   current_x = alien_width
   current_y += 2 * alien_height
  
def _create_alien(self, x_position, y_position):
   """Create an alien and place it in the row."""
   new_alien = Alien(self)
   new_alien.x = x_position
   new_alien.rect.x = x_position
   self.aliens.add(new_alien)
  
def __init__(self):
   --snip--
   # Alien settings
   self.alien_speed = 1.0
  
def __init__(self, ai_game):
   """Initialize the alien and set its starting position."""
  super().__init__()
  self.screen = ai_game.screen
  self.settings = ai_game.settings
  --snip--
  
def update(self):
 """Move the alien to the right."""
  self.x += self.settings.alien_speed
  self.rect.x = self.x
  
while True:
 self._check_events()
 self.ship.update()
 self._update_bullets()
 self._update_aliens()
 self._update_screen()
 self.clock.tick(60)

def _update_aliens(self):
   """Update the positions of all aliens in the fleet."""
   self.aliens.update()

  # Alien settings
   self.alien_speed = 1.0
   self.fleet_drop_speed = 10
   # fleet_direction of 1 represents right; -1 represents left.
   self.fleet_direction = 1

def check_edges(self):
   """Return True if alien is at edge of screen."""
   screen_rect = self.screen.get_rect()
   return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
  
def update(self):
   """Move the alien right or left."""
   self.x += self.settings.alien_speed * self.settings.fleet_direction
   self.rect.x = self.x

def _check_fleet_edges(self):
 """Respond appropriately if any aliens have reached an edge."""
for alien in self.aliens.sprites():
  if alien.check_edges():
    self._change_fleet_direction()
    break

 def _change_fleet_direction(self)

  """Drop the entire fleet and change the fleet's direction."""
   for alien in self.aliens.sprites():
   alien.rect.y += self.settings.fleet_drop_speed
   self.settings.fleet_direction *= -1
  
def _update_aliens(self):
   """Check if the fleet is at an edge, then update positions."""
   self._check_fleet_edges()
   self.aliens.update()

def _update_bullets(self):
 """Update position of bullets and get rid of old bullets."""
 --snip--
 # Check for any bullets that have hit aliens.
 # If so, get rid of the bullet and the alien.
 collisions = pygame.sprite.groupcollide(
     self.bullets, self.aliens, True, True)

def _update_bullets(self):
 --snip--
    if not self.aliens:

 # Destroy existing bullets and create new fleet.
    self.bullets.empty()
    self._create_fleet()

# Bullet settings
 self.bullet_speed = 3.0
 self.bullet_width = 2.5
 --snip--

def _update_bullets(self):
   --snip--
   # Get rid of bullets that have disappeared.
   for bullet in self.bullets.copy():
     if bullet.rect.bottom <= 0:
       self.bullets.remove(bullet)

   self._check_bullet_alien_collisions()
  
def _check_bullet_alien_collisions(self):
   """Respond to bullet-alien collisions."""
   # Remove any bullets and aliens that have collided.
   collisions = pygame.sprite.groupcollide(
      self.bullets, self.aliens, True, True)
   if not self.aliens:
   # Destroy existing bullets and create new fleet.
   self.bullets.empty()
   self._create_fleet()

def _update_aliens(self):
  --snip--
  self.aliens.update()

# Look for alien-ship collisions.
  if pygame.sprite.spritecollideany(self.ship, self.aliens):
  print("Ship hit!!!")
