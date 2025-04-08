from algorithms import load_data
from visualizer import linear_regression, kmeans_clustering

def line_graph_callback():
    df = load_data()
    linear_regression(df)

def clustering_callback():
    df = load_data()
    kmeans_clustering(df)

def display():
    print("Welcome to Climate Change Analyzer!")
    print("1. Line Graph")
    print("2. Clustering Analysis")
    print("3. Exit")

def Interface():
    while True:
        display()
        choice = input("Enter your choice: ")
        if choice == '1':
            line_graph_callback()
        elif choice == '2':
            clustering_callback()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

