import time
import webbrowser
import sys

# A simple timer script, with 3 parameter (interval, rest time, and link to open)
# This is Task 1 from https://github.com/josharsh/Learning-Object-Oriented-Python/blob/master/Lesson%202%20-%20Using%20Functions/functions.md

def main():
    def breaker(_interval, _rest=215, _youtube='https://www.youtube.com/watch?v=dQw4w9WgXcQ'):
        now = time.time()
        play = now + 3600 * _interval
        print(f"next play at {time.ctime(play)}")
        while now < play:
            now = time.time()
            print(f"{int(play-now)} seconds remaining, keep working!", end="\r")
            
            if now > play:
                break
            time.sleep(1)

        print("Enjoy your break time!")
        webbrowser.open(_youtube)
        time.sleep(_rest)

        breaker(_interval)

    #start of the script
    print("""Hello! Welcome to break timer!
Please enter your desired break interval in hours! e.g : '0.5' or '1' (default is 30 min or 0.5 hour):""")
    interval = float(input() or '0.5')

    print('Please enter your desired break duration (in seconds) (default is 212 seconds):')
    rest = float(input() or '212')

    print('Please enter your desired youtube / link to open in break time (e.g: https://www.youtube.com/watch?v=dQw4w9WgXcQ):')
    youtube = input() or 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

    try :
        print(f"Interval set at {interval} hour(s)")
        breaker(interval, rest, youtube)
    except :
        print("""Oops! Something wrong :/ 
Please make sure that you entered the correct break interval (in hours)""")

if __name__ =="__main__":
    main()
