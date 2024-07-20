class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        """
         every time we meet a robot that goes to the right, 
         we add it to the stack and every time we meet a robot that goes to the left,
         we fight it with the last robot on the stack until 
         the last the robot on the stack does not go left
        """

        n = len(positions)
        robots = [[positions[index], healths[index], directions[index], index] for index in range(n)]
        robots.sort()
        stack = []

        for robot in robots:
            if robot[2] == 'R' or not stack or stack[-1][2] == 'L':
                stack.append(robot)
                
            elif robot[2] == 'L':
                add = True
                while stack and stack[-1][2] == 'R' and add:
                    last_robot_health = stack[-1][1]
                    if robot[1] > last_robot_health:
                        stack.pop()
                        robot[1] -= 1
                    elif robot[1] < last_robot_health:
                        stack[-1][1] -= 1
                        add = False
                    else:
                        stack.pop()
                        add = False
                    
                if add:
                    stack.append(robot)

        return [robot[1] for robot in sorted(stack, key=lambda robot: robot[3])]
