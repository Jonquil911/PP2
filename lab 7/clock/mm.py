import pygame
import datetime
import sys

pygame.init()
screen = pygame.display.set_mode((829, 836))
clock = pygame.image.load('dial.png')
second = pygame.image.load('second.png')
minute = pygame.image.load('minute.png')
center = (415, 418)

def update_hands():
    time = datetime.datetime.now()
    second_angle = - time.second * 6
    minute_angle = - time.minute * 6
    rotated_second_hand = pygame.transform.rotate(second, second_angle)
    rotated_minute_hand = pygame.transform.rotate(minute, minute_angle)
    second_rect = rotated_second_hand.get_rect(center=center)
    minute_rect = rotated_minute_hand.get_rect(center=center)
    screen.blit(clock, (0, 0))
    screen.blit(rotated_second_hand, second_rect.topleft)
    screen.blit(rotated_minute_hand, minute_rect.topleft)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    update_hands()
    pygame.display.flip()
    pygame.time.delay(1000)
