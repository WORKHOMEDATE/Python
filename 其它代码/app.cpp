#include <iostream>
#include <vector>
#include <algorithm>

class TodoList {
private:
    std::vector<std::string> tasks;

public:
    void addTask(const std::string& task) {
        tasks.push_back(task);
        std::cout << "Task added: " << task << std::endl;
    }

    void displayTasks() const {
        if (tasks.empty()) {
            std::cout << "No tasks in the to-do list." << std::endl;
        } else {
            std::cout << "To-Do List:" << std::endl;
            for (const auto& task : tasks) {
                std::cout << "- " << task << std::endl;
            }
        }
    }

    void removeTask(const std::string& task) {
        auto it = std::find(tasks.begin(), tasks.end(), task);
        if (it != tasks.end()) {
            tasks.erase(it);
            std::cout << "Task removed: " << task << std::endl;
        } else {
            std::cout << "Task not found." << std::endl;
        }
    }
};

int main() {
    TodoList todoList;

    while (true) {
        std::cout << "\n1. Add Task\n2. Display Tasks\n3. Remove Task\n4. Exit\n";
        int choice;
        std::cin >> choice;

        switch (choice) {
            case 1: {
                std::cout << "Enter task: ";
                std::string task;
                std::cin.ignore();  // Ignore the newline character left in the stream
                std::getline(std::cin, task);
                todoList.addTask(task);
                break;
            }
            case 2:
                todoList.displayTasks();
                break;
            case 3: {
                std::cout << "Enter task to remove: ";
                std::string task;
                std::cin.ignore();  // Ignore the newline character left in the stream
                std::getline(std::cin, task);
                todoList.removeTask(task);
                break;
            }
            case 4:
                std::cout << "Exiting the program.\n";
                return 0;
            default:
                std::cout << "Invalid choice. Try again.\n";
        }
    }

    return 0;
}
