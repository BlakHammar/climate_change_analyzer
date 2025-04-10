from algorithms import load_data, kmeans_clustering
from visualizer import scatter_plot, line_graph, bar_graph, linear_regression

def display_line():
    df = load_data()
    line_graph(df)

def display_bar():
    df = load_data()
    bar_graph(df)

def display_scatter():
    df = load_data()
    scatter_plot(df)

def display_linear_regression():
    df = load_data()
    linear_regression(df)

def clustering_callback():
    df = load_data()
    kmeans_clustering(df)

def display():
    print("Ocean Anomalies Analysis")
    print("1. Data Visualization")
    print("2. Algorithms")
    print("3. Exit")

def display_Visualizer():
    print("1. Line Graph")
    print("2. Bar Graph")
    print("3. Scatter Plot")
    print("4. Back")

def display_Algorithms():
    print("1. Linear Regression")
    print("2. K-means Clustering")
    print("3. Back")

def Interface():
    while True:
        display()
        choice = input("Enter your choice: ")
        if choice == '1':
            while True:
                display_Visualizer()
                choice = input("Enter your choice: ")
                if choice == '1':
                    display_line()
                elif choice == '2':
                    display_bar()
                elif choice == '3':
                    display_scatter()
                elif choice == '4':
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == '2':
            while True:
                display_Algorithms()
                choice = input("Enter your choice: ")
                if choice == '1':
                    display_linear_regression()
                elif choice == '2':
                    clustering_callback()
                elif choice == '3':
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

