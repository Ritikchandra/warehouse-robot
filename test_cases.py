def easy():
    return dict(
        n=8,
        obstacles={(3,3)},
        items={(2,2):5,(6,1):8},
        start=(0,0),
        goal=(7,7),
        energy=30
    )


def medium():
    return dict(
        n=10,
        obstacles={(3,3),(3,4),(4,4)},
        items={(2,2):5,(7,7):10,(1,8):6},
        start=(0,0),
        goal=(9,9),
        energy=50
    )


def hard():
    return dict(
        n=15,
        obstacles={(5,i) for i in range(15) if i != 7},
        items={(2,2):5,(10,10):10,(7,3):8,(12,1):7},
        start=(0,0),
        goal=(14,14),
        energy=80
    )




def no_path():
    return dict(
        n=10,
        obstacles={(5,i) for i in range(10)},  # full wall
        items={(2,2):5,(7,7):10},
        start=(0,0),
        goal=(9,9),
        energy=50
    )


def low_energy():
    return dict(
        n=10,
        obstacles=set(),
        items={(2,2):5,(7,7):10},
        start=(0,0),
        goal=(9,9),
        energy=10
    )


def tradeoff():
    return dict(
        n=10,
        obstacles={(4,4),(4,5),(5,4)},
        items={
            (1,1):2,
            (8,8):15,
            (6,2):7
        },
        start=(0,0),
        goal=(9,9),
        energy=40
    )


def maze():
    obstacles = set()
    for i in range(1,9):
        if i != 5:
            obstacles.add((5,i))

    return dict(
        n=10,
        obstacles=obstacles,
        items={(2,7):5,(8,2):10,(7,7):8},
        start=(0,0),
        goal=(9,9),
        energy=60
    )


def many_items():
    return dict(
        n=10,
        obstacles={(3,3),(4,4),(5,5)},
        items={
            (1,1):3,(2,2):4,(3,7):5,
            (7,3):6
        },
        start=(0,0),
        goal=(9,9),
        energy=70
    )


def priority_trap():
    return dict(
        n=12,
        obstacles={(6,i) for i in range(12) if i != 3},
        items={
            (2,2):3,
            (10,2):20,
            (3,9):5
        },
        start=(0,0),
        goal=(11,11),
        energy=80
    )


def straight_vs_detour():
    return dict(
        n=10,
        obstacles=set(),
        items={
            (0,8):4,
            (5,5):12,
            (9,1):6
        },
        start=(0,0),
        goal=(9,9),
        energy=35
    )


# ================= SMALL FAST TEST CASES =================


def small_easy():
    return dict(
        n=5,
        obstacles=set(),
        items={(2,2):5},
        start=(0,0),
        goal=(4,4),
        energy=15
    )



def small_obstacle():
    return dict(
        n=6,
        obstacles={(2,2),(2,3),(3,2)},
        items={(1,4):5,(4,1):6},
        start=(0,0),
        goal=(5,5),
        energy=20
    )



def small_tradeoff():
    return dict(
        n=6,
        obstacles=set(),
        items={
            (1,1):2,   
            (4,4):10  
        },
        start=(0,0),
        goal=(5,5),
        energy=18
    )



def small_energy():
    return dict(
        n=6,
        obstacles=set(),
        items={(1,4):5,(4,1):6},
        start=(0,0),
        goal=(5,5),
        energy=12  
    )



def small_maze():
    return dict(
        n=7,
        obstacles={(3,1),(3,2),(3,3),(3,5)},
        items={(1,5):6,(5,1):7},
        start=(0,0),
        goal=(6,6),
        energy=25
    )



def small_no_path():
    return dict(
        n=6,
        obstacles={(3,i) for i in range(6)},  
        items={(1,1):5},
        start=(0,0),
        goal=(5,5),
        energy=20
    )



def small_many_items():
    return dict(
        n=7,
        obstacles={(3,3)},
        items={
            (1,1):3,
            (2,5):4,
            (5,2):6
        },
        start=(0,0),
        goal=(6,6),
        energy=30
    )
