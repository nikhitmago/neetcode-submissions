class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        target = 10,
        [4,1,0,7] // position
        [2,2,1,1] // speed

        after sorting:
        [7,4,1,0] // position
        [1,2,2,1] // speed
        [3,3,4.5,10] // time

        stack = [3,4.5,10] // monotonically increasing stack
        '''

        # Sort the tuple based on descending order of position
        # i.e. first car is the closest to the target
        pos_speed = list(zip(position, speed))
        pos_speed = sorted(pos_speed, key=lambda x: x[0], reverse=True)
        
        # Calculate time to get to the target [time = (target - pos) / speed]
        times = []
        for pos, speed in pos_speed:
            times.append(float(target - pos) / speed)
        
        # now maintain a monotonically increasing stack of times
        # the number of elements in this stack are the different fleets,
        # where the times <= get merged together and single car fleets are still fleets
        # for example, if stack is [3,2], these (3,2) get merged together as the car with 2
        # will get slowed down by the car with time 3, so we pop it out
        stack = []  # [3,3,4.5,10]
        for time in times:
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
            

            
