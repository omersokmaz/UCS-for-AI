from queue import PriorityQueue
import pandas as pd


class CityNotFoundError(Exception):
    def __init__(self, city):
        print("%s does not exist" % city)


# Implement this function to read data into an appropriate data structure.
def build_graph(path):
    graph = {}

    with open(path) as fp: 
      fieldnames  = fp.readline() 
      for currentline in fp:
          line = currentline
          labels = line.split(',')
          node = labels[0]
          graph[node] = {}

          for i in range(1, len(labels)-1, 2):
              graph[node][labels[i]] = int(labels[i+1])
 
    return graph



# Implement this function to perform uniform cost search on the graph.
def uniform_cost_search(graph, start, end):
    if start not in graph: 
        raise CityNotFoundError(str(start))
        return

    if end not in graph:  
        raise CityNotFoundError(str(end))
        return
    q = PriorityQueue()
    q.put((0, [start]))

    while not q.empty():
        node = q.get()  
        current = node[1][len(node[1])- 1]

        if end in node[1]:
          print("Path found =  " + str(node[1]) + ", and Cost = " + str(node[0])) 
          break

        cost = node[0]
        for neighbor in graph[current]:
          temp = node[1][:]
          temp.append(neighbor)
          q.put((cost + graph[current][neighbor], temp))



def main():
    filepath =input("Enter your file path")
    graph =build_graph(filepath)
    begin =input("Enter your start point: ") 
    finish =input("Enter your end point: ") 
    uniform_cost_search(graph, begin, finish)
# Implement main to call functions with appropriate try-except blocks
if __name__ == "__main__":
    main()
    