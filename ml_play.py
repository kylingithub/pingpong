from mlgame.communication import ml as comm

def ml_loop(side: str):
    print("For {}".format(side))
    comm.ml_ready()

    while True:
        scene_info = comm.recv_from_game()

        if (scene_info["status"] == "GAME_1P_WIN" or
            scene_info["status"] == "GAME_2P_WIN"):
            comm.ml_ready()
            continue

        comm.send_to_game({"frame": scene_info["frame"], "command": "MOVE_LEFT"})
