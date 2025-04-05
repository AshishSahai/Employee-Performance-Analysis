import pandas as pd
import matplotlib.pyplot as plt


employee_data = {}

while True:
    name = input("Enter name of the employee or type 'Done' to exit: ").strip().title()
    if name == "Done":
        break
    try:
        tasks = int(input(f"Enter the task completed by {name}: "))
        rating = float(input(f"Enter the rating of the {name} from 1-5: "))
        if tasks < 1 or not (1 <= rating <= 5):
            raise ValueError
        employee_data[name] = {"tasks_completed": tasks,"ratings": rating}
    except ValueError:
        print("Invalid input, please enter a valid input(numeric value)!")



#for employee, performance in employee_data.items():

def employees_data(data):
    emp_performance_data = {}
    task_data = {}
    rating_data = {}
    for employee, performance in data.items():

        #print(employee)
        perform = performance["tasks_completed"]*performance["ratings"]
        emp_performance_data[employee] = perform
        tasks_completed = performance["tasks_completed"]
        task_data[employee] = tasks_completed
        rating = performance["ratings"]
        rating_data[employee] = rating



    return emp_performance_data, task_data, rating_data


def top_performance(new_data, data, rat_data):



    top_performer = max(new_data, key=new_data.get)
    last_performer = min(new_data, key= new_data.get)
    total_tasks = sum(data.values())
    n= len(data)

    avg_tasks = round(total_tasks/n,2)
    total_rating = sum(rat_data.values())
    n = len(rat_data)
    avg_rating = round(total_rating/n,2)

    return top_performer, last_performer, avg_tasks, avg_rating


def generate_dataframe(data, tasks, rating):
    records = []
    for employee, performance in data.items():
        records.append({"Employee" : employee,
        "Performance points" : performance,
                       "Tasks Completed" : tasks[employee],
                        "Ratings" : rating[employee]})

    return pd.DataFrame(records)




def save_to_csv(df, filename="employee_performance.csv", index=False):
    df.to_csv(filename, index=index)
    print(f"Employee performance data saved as csv with name {filename}")


def visualize_sales(data):
    employee = list(data.keys())
    points = list(data.values())

    plt.figure(figsize=(10,5))

    #Bar Chart
    plt.subplot(1,2,1)
    bars= plt.bar(employee, points, color="skyblue")
    plt.title("Employees performance review")
    plt.xlabel("Employee")
    plt.ylabel("Performance")

    #Pie chart
    plt.subplot(1,2,2)
    plt.pie(points, labels=employee, autopct="%1.1f%%", startangle=90)
    plt.title("Performance share by employee")

    #highlight top performer
    top_performer = max(data, key=data.get)
    last_performer = min(data, key=data.get)
    for bar, name in zip(bars, data):
        if name == top_performer:
            bar.set_color("green")
        elif name == last_performer:
            bar.set_color("red")

    plt.tight_layout()
    plt.show()



#Main Program
def main():

    emp_performance_data, task_data, rating_data = employees_data(employee_data)
    top, last, avg_task, avg_rating  = top_performance(emp_performance_data, task_data, rating_data)


    print(f"Top performer: {top}")
    print(f"Last performer: {last}")
    print(f"Average tasks completed: {avg_task}")
    print(f"Average rating : {avg_rating}")

    df = generate_dataframe(emp_performance_data, task_data, rating_data)
    save_to_csv(df)
    visualize_sales(emp_performance_data)


if __name__ == "__main__":
    main()