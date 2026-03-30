import pygame

CELL = 40
WHITE=(255,255,255); BLACK=(0,0,0)
RED=(255,0,0); GREEN=(0,255,0)
BLUE=(0,0,255); LIGHT_BLUE=(173,216,230)
GREY=(200,200,200)

def animate(grid, explored, path):
    pygame.init()
    screen = pygame.display.set_mode((grid.n*CELL, grid.n*CELL + 50))
    pygame.display.set_caption("Warehouse Robot")

    font = pygame.font.SysFont(None, 30)
    big_font = pygame.font.SysFont(None, 40)

    pygame.time.delay(1000)

   
    if path is None:
        running = True

        while running:
            screen.fill(WHITE)

            # grid
            for x in range(grid.n):
                for y in range(grid.n):
                    pygame.draw.rect(screen, WHITE, (x*CELL,y*CELL,CELL,CELL))
                    pygame.draw.rect(screen, GREY, (x*CELL,y*CELL,CELL,CELL),1)

            # obstacles
            for (x,y) in grid.obstacles:
                pygame.draw.rect(screen, BLACK, (x*CELL,y*CELL,CELL,CELL))

            # items
            for (x,y) in grid.items:
                pygame.draw.rect(screen, RED, (x*CELL,y*CELL,CELL,CELL))

            # goal
            gx,gy = grid.goal
            pygame.draw.rect(screen, GREEN, (gx*CELL,gy*CELL,CELL,CELL))

            # message
            text = big_font.render("NO PATH EXISTS TO GOAL STATE", True, (200,0,0))
            screen.blit(text, (10, grid.n*CELL + 10))

            pygame.display.flip()

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    running = False

        pygame.quit()
        return  

 
    i = 0
    running = True

    while running:
        screen.fill(WHITE)

        # grid
        for x in range(grid.n):
            for y in range(grid.n):
                pygame.draw.rect(screen, WHITE, (x*CELL,y*CELL,CELL,CELL))
                pygame.draw.rect(screen, GREY, (x*CELL,y*CELL,CELL,CELL),1)

        current_priority = 0

        # explored
        for j in range(min(i, len(explored))):
            node = explored[j]

            if len(node) == 3:
                x, y, p = node
                current_priority = p
            else:
                x, y = node
                p = 0

            pygame.draw.rect(screen, LIGHT_BLUE, (x*CELL,y*CELL,CELL,CELL))

        # obstacles
        for (x,y) in grid.obstacles:
            pygame.draw.rect(screen, BLACK, (x*CELL,y*CELL,CELL,CELL))

        # items
        for (x,y) in grid.items:
            pygame.draw.rect(screen, RED, (x*CELL,y*CELL,CELL,CELL))

        # goal
        gx,gy = grid.goal
        pygame.draw.rect(screen, GREEN, (gx*CELL,gy*CELL,CELL,CELL))

        # path
        if i >= len(explored) and path:
            for (x,y) in path:
                pygame.draw.rect(screen, BLUE, (x*CELL,y*CELL,CELL,CELL))

        # info bar
        pygame.draw.rect(screen, (220,220,220), (0, grid.n*CELL, grid.n*CELL, 50))
        text = font.render(f"Collected Priority: {current_priority}", True, (0,0,0))
        screen.blit(text, (10, grid.n*CELL + 10))

        pygame.display.flip()

        if i < len(explored):
            i += 1
            pygame.time.delay(10)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

    pygame.quit()
