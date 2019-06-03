class Gracz(object):
    
    def __init__(self):
        
        # x i y - pozycja
        self.zycie = 3
        self.x = 335
        self.y = 450
        self.left = 0
        self.right = 0
        self.speed = 15
  
        
    def show(self):  # pokaż gracza
        fill(241, 196, 15)
        circle(self.x, self.y, 55)
   
    def update(self):  # aktualizuje pozycję gracza + ogranicznik przy krawędziach
       self.x = self.x + (self.right - self.left)  *self.speed
       
       if not (self.x <= (700 - 35)):
           self.x = (700 - 35) 
       
       if not (self.x >= 35):
           self.x = 35
   
   
    #def strac_zycie(self,zycie):
        #self.zycie -= 1
        
        #if self.zycie == 0:
            #print("Game over!")
            
            
class Bullet(object):
    
    def __init__(self):
        self.pl_x = 335
        self.y = 450
        self.speed = 20
        self.right = 0
        self.left = 0
        self.player_speed = 15
        
        
    def show_bullet(self):
        fill(255)
        rect(self.pl_x-2, self.y-27, 3, 12)
        
    def update_bullet(self):
        self.pl_x = self.pl_x + (self.right - self.left) * self.player_speed
        
        
    def shot(self):
        self.y = self.y - self.speed        


def setup():
    size(700, 500)
    
    global statek
    global pocisk
    
    statek = Gracz()
    pocisk = Bullet()
   
    
def draw():
    background(74, 35, 90)
    global statek
    global pocisk
    statek.show()
    statek.update()
    
    
    print(mouseX, mouseY)
    
def keyPressed():
    if keyCode == LEFT:
        statek.left = 1
        pocisk.left = 1
        pocisk.update_bullet()
        

        
    if keyCode == RIGHT:
        statek.right = 1
        pocisk.right = 1
        pocisk.update_bullet()

        
    if keyCode == 32:
        pocisk.show_bullet()
        
        
def keyReleased():
    if keyCode == LEFT:
        statek.left = 0
        pocisk.left = 0
            
    if keyCode == RIGHT:
        statek.right = 0
        pocisk.right = 0
        
    if keyCode == 32:
        pocisk.show_bullet()
        pocisk.shot
        




        

        
