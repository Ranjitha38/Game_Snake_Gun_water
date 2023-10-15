import random
from fastapi import FastAPI,HTTPException, Request
from pydantic import BaseModel

class User_input(BaseModel):
    user: int

    


app = FastAPI()

@app.post("/game")
async def snake_gun_water_game(user_inp: User_input):
    def check(comp,user):
        if comp == user:
            return 0
        elif (comp == 0 and user == 1):
            return -1
        elif (comp == 1 and user == 2):
            return -1
        elif (comp ==2 and user == 0):
            return -1 

        return 1
    comp = random.randint(0,2)
    #user = print("Select 0 for snake, 1 for water, 2 for Gun :", user_inp)
    user_choice = user_inp.user
    
    
    score = check(comp,user_choice)

    if score == 0:
        
        return {"Select 0 for snake, 1 for water, 2 for Gun","computer choice is " + str(comp), "It's a draw"}
    elif score == -1:
       
        return {"Select 0 for snake, 1 for water, 2 for Gun","computer choice is " + str(comp), "You lose!!, Better luck next time"}
    else:
        
        return {"Select 0 for snake, 1 for water, 2 for Gun","computer choice is " + str(comp), "Congratulations !! You Won"}
        


