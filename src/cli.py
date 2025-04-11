from data_processor import load_data
from algorithms import kmeans_clustering, linear_regression, detect_anomalies
from visualizer import scatter_plot, line_graph, bar_graph

def main_display(): #main options display
    print("Ocean Anomalies Analysis")
    print("1. Data Visualization")
    print("2. Algorithms")
    print("3. Exit")

def vis_display():  #visual options display
    print("1. Line Graph")
    print("2. Bar Graph")
    print("3. Scatter Plot")
    print("4. Back")

def algo_display(): #algorithm options display
    print("1. Linear Regression")
    print("2. K-means Clustering")
    print("3. Time Series Anomaly Detection")
    print("4. Back")

vis_choices = { #visual choices
    1: line_graph,
    2: bar_graph,
    3: scatter_plot, 
    4: "Exit"
}

algo_choices = { #algorithm choices
    1: linear_regression,
    2: kmeans_clustering,
    3: detect_anomalies,
    4: "Exit"
}

main_choices = { #main choice menu
    1: [vis_display, vis_choices], #holds display function and choice list
    2: [algo_display, algo_choices],
    3: "Exit"
}

def choice_loop(display_type, choice_list):
    while True:
        print("\n") #create line space before displaying options
        display_type() #Display options based on type (main, visual, algorithm)
        choice = int(input("\nEnter your choice: "))
        result = choice_list.get(choice) #Find result from choice list based on type
        if result:
            if result == "Exit":
                if choice_list == main_choices: #print goodbye if exiting the entire program
                    print("\nGoodbye!")

                break #break if exiting option or program
            else:
                if isinstance(result, list): #main choices are returned as a list to hold the display function and choice list
                    choice_loop(result[0], result[1]) #restart the loop using new display and choice list
                else:
                    result() #sub choices are returned as a single function
        else:
            print("\nInvalid choice, please try again.")
                
def Interface(): 
    choice_loop(main_display, main_choices) #Begin loop sending display type and choice list