import pygame, sys
from pygame.locals import *
from random import*
from constantes import *
pygame.init()

font = pygame.display.set_mode((fontx,fonty))

pygame.key.set_repeat(delay,interval)
pygame.display.flip()


def collision(self, collider):
    if self.colliderect(collider):
        return True


while continuer == True:
    while jeu == True : 
    	for event in pygame.event.get() :
        	keys = pygame.key.get_pressed()
        	if event.type == QUIT:
        		pygame.quit()


        	if keys[q] == 1 :
        		lead_x -= 10
        	if keys[d] == 1:
        		lead_x += 10
        	if keys[z] == 1:
        		lead_y -= 10
        	if keys[s] == 1:
        		lead_y += 10
        	if keys[LEFT] == 1:
        		lead_x2 -= 10
        	if keys[RIGHT] == 1:
        		lead_x2 += 10
        	if keys[UP] == 1:
        		lead_y2 -= 10
        	if keys[DOWN] == 1:
        		lead_y2 += 10



        	if lead_x > fontx :
        		lead_x = 0
        	if lead_x < 0:
        		lead_x = fontx
        	if lead_y > fonty:
        		lead_y = 0
        	if lead_y < 0:
        		lead_y = fonty

        	if lead_x2 > fontx :
        		lead_x2 = 0
        	if lead_x2 < 0:
        		lead_x2 = fontx
        	if lead_y2 > fonty:
        		lead_y2 = 0
        	if lead_y2 < 0:
        		lead_y2 = fonty


    	font.fill((grey))
    	snake = pygame.draw.rect(font,(white),[lead_x,lead_y,taille_héro,taille_héro])
    	snake2 = pygame.draw.rect(font,(yellow),[lead_x2,lead_y2,taille_héro,taille_héro])
    	cible = pygame.draw.rect(font,(black),[rx,ry,taille_cible,taille_cible])

    	score_display1 = police.render(aff_score1,False,(white))
    	score_display1_rect = score_display1.get_rect()
    	font.blit(score_display1,score_display1_rect)


    	score_display2 = police.render(aff_score2,False,(yellow))
    	score_display2_rect = score_display2.get_rect()
    	score_display2_rect.topright =(fontx,0)
    	font.blit(score_display2,score_display2_rect)


    	pygame.display.update()


    	if collision(snake,cible) == True:
        	rx = randint(taille_cible,fontx - taille_cible)
        	ry = randint(taille_cible,fonty - taille_cible)
        	score1 += 1
        	score_total += 1
        	print(score1)
        	aff_score1 = ("Score : {}").format(score1)
        	font.blit(score_display1,score_display1_rect)

    	if collision(snake2,cible) == True:
        	rx = randint(taille_cible,fontx - taille_cible)
        	ry = randint(taille_cible,fonty - taille_cible)
        	score2 += 1
        	score_total += 1
        	print(score2)
        	aff_score2 = ("Score : {}").format(score2)
        	font.blit(score_display2,score_display2_rect)


    	pygame.display.update()

    	if score_total == score_total_obj:
    		jeu = False
    		continuer = False



pygame.quit()
quit()








