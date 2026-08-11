class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # have to remember, cars behind each other
        cars = list(zip(position, speed))
        
        # sort by first part
        cars.sort(key=lambda x: x[0], reverse=True)

        # stack of fleets (array)
        fleets = []

        for i in range(len(cars)):
            hours_i = (target - cars[i][0]) / cars[i][1]
            if not fleets:
                fleets.append(hours_i)
            elif (fleets[-1]) < hours_i:
                fleets.append(hours_i)
        
        return len(fleets)
            