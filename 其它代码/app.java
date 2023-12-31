import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class TodoApp extends JFrame {
    private JTextField taskInput;
    private JTextArea taskList;

    public TodoApp() {
        // Set up the main frame
        super("Todo List App");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(400, 300);

        // Create components
        taskInput = new JTextField();
        JButton addButton = new JButton("Add Task");
        taskList = new JTextArea();
        taskList.setEditable(false);

        // Set up layout
        setLayout(new BorderLayout());
        add(taskInput, BorderLayout.NORTH);
        add(addButton, BorderLayout.CENTER);
        add(new JScrollPane(taskList), BorderLayout.SOUTH);

        // Add ActionListener for the Add Task button
        addButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                addTask();
            }
        });
    }

    private void addTask() {
        String task = taskInput.getText();
        if (!task.isEmpty()) {
            if (taskList.getText().isEmpty()) {
                taskList.setText(task);
            } else {
                taskList.append("\n" + task);
            }
            taskInput.setText("");
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new TodoApp().setVisible(true);
            }
        });
    }
}
