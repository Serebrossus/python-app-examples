import pygame.camera

pygame.camera.init()
# camera detected or no
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0], (640, 480))
cam.start()
img = cam.get_image()
pygame.image.save(img, 'pygame-screen.jpg')
pygame.camera.quit()
